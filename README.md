desmeme
=======

This repository contains data and tools for exploring the linguistic typology of templatic constructions described in the form of graphs representing attribute-value matrices. It is associated with *The Linguistic Typology of Templates* (Cambridge University Press), authored by Jeff Good, who can be contacted at jcgood@buffalo.edu.

The book contains detailed theoretical discussion motivating the database and scripts here. These materials are made available for those wishing to verify the results described in the book or to adapt the methods and data for their own purposes. They were not formally reviewed as part of the publication process and are not intended for out-of-the-box deployment on new projects. The author welcomes contact from anyone interested in testing or collaborative use.

The software and associated materials have been released into the public domain to the extent legally permitted. This release does not relieve users of the responsibility to follow accepted scholarly norms of citation.

## Repository structure

```
tdag/              Python package for working with templatic DAGs
schema/            DesmemeSchema.tsv, ComponentSchema.tsv, GrammaticalCategories.tsv
data/
  nya/             Chichewa (ISO 639-3) desmeme and component data
rdf/               RDF/OWL source files (Protégé); historical record, never deleted
scripts/           Active scripts (run from repo root)
  earlier/         Archived earlier-generation scripts (Perl, older Python)
output/            Generated files: graphs (.dot, .pdf), AVMs (.tex), nexus files
tests/             Regression tests
docs/
  notes/           Working notes preserved for provenance
```

## Data pipeline

1. Desmemes are encoded in `rdf/template-CHx.rdf` using Protégé
2. `scripts/RDFtoTabbed2.py` exports from RDF to TSV (`data/nya/`)
3. `scripts/ReadDesmemes.py` reads TSV, validates against schema, renders AVMs or graphs

The TSV files in `data/nya/` are the primary working representation. The RDF files in `rdf/` are the historical source of record and are never deleted.

## Running the scripts

```bash
# Validate TSV data and print ASCII AVMs to stdout
python scripts/ReadDesmemes.py

# Re-export from RDF to TSV (requires rdf/template-CHx.rdf)
python scripts/RDFtoTabbed2.py

# Run regression tests
python -m pytest tests/
```

All scripts are run from the repo root.

## `tdag` package

- **`tdag.py`** — `tdag` class: DAG wrapper around `pygraph.digraph`, handles re-entrancy and repeated node types
- **`tabbed.py`** — reads TSV files into `tdag` graphs; `get_tabbed_desmemes()` with schema validation and configurable skip flags (`skip_components`, `skip_md`, `skip_an`, `skip_ex`) for controlling what enters the comparison graph
- **`avm.py`** — renders a `tdag` as an ASCII or LaTeX AVM
- **`comparison.py`** — simUI graph similarity metric, nexus output for SplitsTree, graph visualization via `pydot` + Graphviz
- **`despecification.py`** — strips metadata/instance nodes before typological comparison (currently RDF-pipeline-dependent; see issue #5)
- **`validator.py`** — schema validation against `schema/DesmemeSchema.tsv` and `schema/ComponentSchema.tsv`

## Schema

Desmemes and their components are described using a typed attribute-value language. See **[docs/SCHEMA.md](docs/SCHEMA.md)** for the full technical reference, including the tab-indentation format, type sigils, namespace prefixes, and all feature definitions.

Quick orientation:

- `MD:` — metadata (bibliographic source, external references)
- `AN:` — annotations (transcription strings)
- `EX:` — excluded from core typology but potentially typological (function, liaison, filler class)

Type sigils: `@id`, `@lang`, `@int`, `@ref`, `@str`, `@grammaticalCategory`

## Earlier materials

`scripts/earlier/` archives the earlier-generation pipeline: Perl Similarity Flooding scripts (`GraphFlooding*.pl`, `GraphJG/`) and older Python export scripts (`RDFtoAVM.py`, `RDFtoNexus.py`, etc.). These predate the current TSV-based pipeline and are preserved for provenance. A reimplementation of Similarity Flooding in Python is planned (issue #16).

## Dependencies

- `pygraph` ([Shoobx fork](https://github.com/Shoobx/python-graph)) — graph data structures
- `pydot` — dot file generation
- `rdflib` — RDF parsing (migration script)
- Graphviz (`dot`, `pdf2ps`, `ps2eps`) — graph rendering
- `pytest` — regression tests

```bash
pip install -r requirements.txt
```
