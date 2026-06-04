"""
Regression tests for pairwise simUI distance calculations.

Ground truth: groundTruth2024/templateNoComp.nex, computed from template-CHx.rdf
in 2024 and used in a published paper.

The noComp test verifies that structural desmeme distances (ignoring component
internals) match the published values to within 0.01 (the stored precision).

The with-components test is a TODO: the RDF pipeline collapsed all component
instances to a single "component" node, while the TSV pipeline uses unique
component IDs. Matching that ground truth requires a despecification step not
yet implemented for the TSV pipeline.
"""

import os
import sys
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from tdag.tabbed import get_tabbed_desmemes
from tdag.comparison import get_distances

GROUND_TRUTH_NOCOMP = os.path.join(ROOT, "groundTruth2024", "templateNoComp.nex")
DESMEME_TSV = os.path.join(ROOT, "ChichewaDesmemes.tsv")
COMPONENT_TSV = os.path.join(ROOT, "ChichewaComponents.tsv")
DESMEME_SCHEMA = os.path.join(ROOT, "DesmemeSchema.tsv")
COMPONENT_SCHEMA = os.path.join(ROOT, "ComponentSchema.tsv")

TOLERANCE = 0.01

# Desmeme identifiers that were renamed after the 2024 ground truth was generated.
# Maps current TSV short name → ground truth name.
#
# CompoundStem-PHON was previously coded as CompoundStem-PhMOR (phonological-
# morphological interface). It was reclassified as purely phonological (-PHON)
# because its components (ChichewaVerbalReduplicant, ChichewaProsodicDerivational-
# StemEmbedded) indicate the constraint is phonologically rather than morpho-
# logically driven. The feature structure (CONDITIONING, VIOLABILITY, STRICTURE,
# FOUNDATION) did not change, so the noComp distances are unaffected by the
# reclassification.
RENAMES = {
    "CompoundStem-PHON": "CompoundStem-PhMOR",
}


def parse_nex_distances(nex_path):
    """Parse a lower-triangular NEXUS distance matrix into a dict-of-dicts."""
    distances = {}
    labels = []
    in_matrix = False
    with open(nex_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.upper().startswith("MATRIX"):
                in_matrix = True
                continue
            if not in_matrix:
                continue
            if line == ";":
                break
            parts = line.split()
            label = parts[0]
            vals = [float(x) for x in parts[1:]]
            labels.append(label)
            for j, val in enumerate(vals):
                other = labels[j]
                distances.setdefault(label, {})[other] = val
                distances.setdefault(other, {})[label] = val
    return distances


def test_validation_smoke():
    """Loading all 34 Chichewa desmemes with components passes validation."""
    desmemes = get_tabbed_desmemes(
        DESMEME_TSV, COMPONENT_TSV, DESMEME_SCHEMA, COMPONENT_SCHEMA
    )
    assert len(desmemes) == 34, f"Expected 34 desmemes, got {len(desmemes)}"


def test_nocomp_distances():
    """TSV-based noComp pairwise distances match 2024 ground truth within 0.01."""
    ground_truth = parse_nex_distances(GROUND_TRUTH_NOCOMP)
    assert len(ground_truth) == 34, f"Expected 34 taxa in ground truth, got {len(ground_truth)}"

    desmemes = get_tabbed_desmemes(
        DESMEME_TSV, COMPONENT_TSV, DESMEME_SCHEMA, COMPONENT_SCHEMA,
        skip_components=True
    )
    assert len(desmemes) == 34

    distances = get_distances(desmemes)

    # TSV names are "ChichewaX"; ground truth uses short names, some of which
    # have been renamed since the ground truth was generated (see RENAMES).
    def gt_name(tsv_name):
        short = tsv_name.replace("Chichewa", "", 1)
        return RENAMES.get(short, short)

    failures = []
    for t1, row in distances.items():
        g1 = gt_name(t1)
        if g1 not in ground_truth:
            failures.append(f"Name not found in ground truth: {t1!r} → {g1!r}")
            continue
        for t2, dist in row.items():
            if t1 == t2:
                continue
            g2 = gt_name(t2)
            if g2 not in ground_truth[g1]:
                failures.append(f"Pair not in ground truth: {g1!r} vs {g2!r}")
                continue
            expected = ground_truth[g1][g2]
            if abs(dist - expected) > TOLERANCE:
                failures.append(
                    f"{g1} vs {g2}: got {dist:.4f}, expected {expected:.2f} "
                    f"(diff {abs(dist - expected):.4f})"
                )

    assert not failures, f"{len(failures)} distance mismatch(es):\n" + "\n".join(failures[:20])
