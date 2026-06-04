# desmeme

Data and code repository for *The Linguistic Typology of Templates* (Cambridge University Press, Jeff Good). The book develops a cross-linguistic typology of **templatic constructions** — grammatical patterns where linguistic elements appear in a stipulated fixed order or length.

## Core concept

A **desmeme** is the formal typological description of a single templatic construction in a language. Desmemes are encoded as attribute-value matrices (AVMs) modeled as directed acyclic graphs (DAGs). The description language uses an architectural metaphor for the structural "foundation" of a template.

## Provenance and history

Provenance and historical record are first-class concerns in this repository. This is a linguistics research project whose data will be cited in published work; decisions, corrections, and the reasoning behind them must be traceable.

- **RDF files in `rdf/` are never deleted.** They are the original authoritative source from which TSV files were derived. Even after TSV becomes the primary working format, the RDF files remain as the historical record of how the data was first encoded.
- **Intermediate TSV variants** (e.g. `_full`, `_run2`) may be retired from the working tree once superseded, but their history is preserved in git.
- **Data gap patches** (e.g. `COMPONENT_PATCHES` in migration scripts) must be documented with issue references so that corrections to the underlying data can be traced back to the original encoding decision.
- **Commit messages** should explain *why* a change was made (constraint, correction, reclassification) not just *what* changed, so the reasoning survives long after the code context is gone.

## Repository structure

```
tdag/                       # Main Python package
schema/                     # DesmemeSchema.tsv, ComponentSchema.tsv, GrammaticalCategories.tsv
data/
  nya/                      # Chichewa (ISO 639-3: nya); future languages get sibling dirs
    ChichewaDesmemes.tsv
    ChichewaComponents.tsv
rdf/                        # RDF/OWL source files (Protégé); historical record, never deleted
scripts/                    # ReadDesmemes.py, RDFtoTabbed2.py (run from repo root)
output/                     # Generated outputs: graphs, nexus files, ground truth
tests/                      # Regression tests
```

## Data pipeline

1. **Author** encodes desmemes in `rdf/template-CHx.rdf` using Protégé
2. **`scripts/RDFtoTabbed2.py`** reads the RDF and writes TSV files to `data/nya/`
3. **`scripts/ReadDesmemes.py`** reads TSV files, validates against schema, renders ASCII AVMs or graph visualizations

The TSV files are the primary working representation. The RDF is the historical source of record.

## `tdag` package modules

- **`tdag.py`** — `tdag` class: DAG wrapper around `pygraph.digraph`, handles re-entrancy (one node pointed to by two labeled arcs)
- **`tabbed.py`** — `tabbed` class: converts graph ↔ TSV; `featval` class for feature-value pairs; `get_tabbed_desmemes()` for reading TSV with validation
- **`avm.py`** — Renders a `tdag` as an ASCII or LaTeX AVM
- **`comparison.py`** — Graph similarity (simUI distance metric), nexus output for SplitsTree, `.dot`/PDF visualization via `pydot` + Graphviz
- **`despecification.py`** — Strips bibliographic/metadata/instance nodes before typological comparison
- **`validator.py`** — Schema validation: checks allowed features, required features, and value types against `schema/DesmemeSchema.tsv` / `schema/ComponentSchema.tsv`

## Schema / description language key concepts

**Foundation types:**
- `arch` — has LEFT_SUPPORT, LEFT_VOUSSOIR, KEYSTONE, RIGHT_VOUSSOIR, RIGHT_SUPPORT, optional RESTKOMPONENTEN
- `span` — has LEFT_SUPPORT, RIGHT_SUPPORT, optional RESTKOMPONENTEN

**Component properties (ComponentSchema.tsv):**
- `ELASTICITY`: elastic (MINIMUM/MAXIMUM) | inelastic (COUNT)
- `FILLEDNESS`: open | filled (FORM) | partiallyFilled (FILLER_PLACEMENT, FORM, COHERENCE) | null
- `STABILITY`: stable | unstable (ASSOCIATE_POSITION, ASSOCIATE)

**Desmeme properties (DesmemeSchema.tsv):**
- `CONDITIONING`: constructionalConditioning | lexicoconstructionalConditioning (FILLER_POSITION, FILLED_COMPONENTS) | prosodicConditioning
- `VIOLABILITY`: notViolable | potentiallyViolable (EXCEPTIONALITY, REPARABILITY)
- `STRICTURE`: length (CONSTITUENT, COUNT) | order (CONSTITUENT, COUNT, RELATIONS)

## Dependencies

- `pygraph` (python-graph, via [Shoobx fork](https://github.com/Shoobx/python-graph)) — graph data structures; **no longer maintained**, migration to NetworkX noted as future work
- `pydot` — dot file generation
- `rdflib` — RDF parsing
- Graphviz (`dot`, `pdf2ps`, `ps2eps`) — graph rendering, called via `os.system()`

## Running the scripts

```bash
# Read TSV data, validate, and print ASCII AVMs to stdout
python scripts/ReadDesmemes.py

# Re-export RDF to TSV (requires rdf/template-CHx.rdf)
python scripts/RDFtoTabbed2.py
```

Both scripts are run from the repo root.

## Known issues / notes

- `draw_graphs()` in `comparison.py` is currently commented out in both main scripts because it breaks on full templates with metadata
- The `pygraph` library may need to be replaced with NetworkX at some point
- Some workarounds in `tabbed.py` are explicitly noted as hacks (e.g., Nimboran RK re-entrancy, Tiene criss-crossing associates)
- Data gaps patched during migration are tracked in issues #14 and #15
