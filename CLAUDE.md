# desmeme

Data and code repository for *The Linguistic Typology of Templates* (Cambridge University Press, Jeff Good). The book develops a cross-linguistic typology of **templatic constructions** — grammatical patterns where linguistic elements appear in a stipulated fixed order or length.

## Core concept

A **desmeme** is the formal typological description of a single templatic construction in a language. Desmemes are encoded as attribute-value matrices (AVMs) modeled as directed acyclic graphs (DAGs). The description language uses an architectural metaphor for the structural "foundation" of a template.

## Repository structure

```
template-CHx.rdf / .rdfs   # Source data (OWL/RDF, edited in Protégé)
RDFtoTabbed.py              # Converts RDF → TSV flat files
ReadDesmemes.py             # Reads TSV, validates, renders ASCII AVMs / graphs
DesmemeSchema.tsv           # Schema for desmeme feature-value structure
ComponentSchema.tsv         # Schema for component feature-value structure
ChichewaDesmemes*.tsv       # Desmeme data for Chichewa (ISO: nya)
ChichewaComponents*.tsv     # Component data for Chichewa
Graphs_full/                # Generated .dot and .pdf graph visualizations
tdag/                       # Main Python package (current)
tdag_orig/                  # Older package version (still used by RDFtoTabbed.py)
tempTex/                    # Book chapter LaTeX source (for context; not committed)
```

## Data pipeline

1. **Author** encodes desmemes in `template-CHx.rdf` using Protégé
2. **`RDFtoTabbed.py`** reads the RDF and writes TSV flat files (`*_full.tsv`)
3. **`ReadDesmemes.py`** reads TSV files, validates against schema, reconstructs graphs, outputs ASCII AVMs or graph visualizations

The TSV format is the working representation; the RDF is the authoritative source.

## `tdag` package modules

- **`tdag.py`** — `tdag` class: DAG wrapper around `pygraph.digraph`, handles re-entrancy (one node pointed to by two labeled arcs)
- **`tabbed.py`** — `tabbed` class: converts graph ↔ TSV; `featval` class for feature-value pairs; `get_tabbed_desmemes()` for reading TSV with validation
- **`avm.py`** — Renders a `tdag` as an ASCII or LaTeX AVM
- **`comparison.py`** — Graph similarity (simUI distance metric), nexus output for SplitsTree, `.dot`/PDF visualization via `pydot` + Graphviz
- **`despecification.py`** — Strips bibliographic/metadata/instance nodes before typological comparison
- **`validator.py`** — Schema validation: checks allowed features, required features, and value types against `DesmemeSchema.tsv` / `ComponentSchema.tsv`

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
- `rdflib` — RDF parsing (used in `tdag_orig`)
- Graphviz (`dot`, `pdf2ps`, `ps2eps`) — graph rendering, called via `os.system()`

## Running the scripts

```bash
# Read TSV data, validate, and print ASCII AVMs to stdout
python ReadDesmemes.py

# Export RDF to TSV (requires template-CHx.rdf)
python RDFtoTabbed.py
```

Both scripts are run from the repo root. They expect the TSV files and schema files to be present in the root directory.

## Known issues / notes

- `tdag_orig` and `tdag` are parallel implementations; `RDFtoTabbed.py` uses `tdag_orig` for RDF reading and `tdag` for graph visualization
- `draw_graphs()` in `comparison.py` is currently commented out in both main scripts because it breaks on full templates with metadata
- The `pygraph` library may need to be replaced with NetworkX at some point
- Some workarounds in `tabbed.py` are explicitly noted as hacks (e.g., Nimboran RK re-entrancy, Tiene criss-crossing associates)
