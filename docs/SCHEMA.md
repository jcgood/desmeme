# Desmeme TSV Schema Reference

This document is the technical reference for the TSV data format used to encode desmemes and their components. For theoretical background on the description language, see the book. For how to run the pipeline, see the README.

## Files

Each language has two TSV files under `data/{iso}/`:

| File | Content |
|------|---------|
| `{Name}Desmemes.tsv` | One record per desmeme (templatic construction) |
| `{Name}Components.tsv` | One record per component (position in the template) |

Schema files live in `schema/`:

| File | Purpose |
|------|---------|
| `DesmemeSchema.tsv` | Allowed features and types for desmeme records |
| `ComponentSchema.tsv` | Allowed features and types for component records |
| `GrammaticalCategories.tsv` | Closed vocabulary for `@grammaticalCategory` values |

---

## Record format

Records within a file are separated by a blank line. Every record begins with exactly two header lines, then zero or more feature-value lines:

```
IDENTIFIER	ChichewaAR-MOR
LANGUAGE	nya
CONDITIONING	lexicoconstructionalConditioning
	FILLER_POSITION	templateMultiple
	FILLED_COMPONENTS	filledComponentSet
		FILLED_COMPONENT	ChichewaApplicative
		FILLED_COMPONENT	ChichewaReciprocal
EX:FUNCTION	local:valency
VIOLABILITY	potentiallyViolable
	EXCEPTIONALITY	semantic
	REPARABILITY	morphosyntacticInsertion
...
```

### Tab-indentation

Nesting depth is encoded by leading tab characters. A feature at depth *n* is a sub-feature of the most recent value at depth *n*−1. The root level (no tabs) is depth 0.

```
ELASTICITY	elastic           ← depth 0: feature ELASTICITY, value elastic
	MINIMUM	0                 ← depth 1: sub-feature of elastic
	MAXIMUM	1                 ← depth 1: sub-feature of elastic
```

Each field on a line is tab-separated: `{tabs}{feature}\t{value}`.

---

## Type sigils

Terminal values in the schema are specified by a sigil indicating what kind of string is valid:

| Sigil | Meaning | Example value |
|-------|---------|---------------|
| `@id` | A locally unique identifier (no constraints on form) | `ChichewaAR-MOR` |
| `@lang` | An ISO 639-3 language code | `nya` |
| `@int` | A non-negative integer or `∞` | `3`, `∞` |
| `@ref` | A component IDENTIFIER (cross-reference) | `ChichewaApplicative` |
| `@str` | An arbitrary string | free text |
| `@grammaticalCategory` | A value from `GrammaticalCategories.tsv` | `gold:Verbal`, `local:valency` |

---

## Kleene operators

Features in the schema may be marked with a suffix indicating cardinality:

| Suffix | Meaning |
|--------|---------|
| *(none)* | Exactly one occurrence required |
| `*` | Zero or one occurrence (optional) |
| `+` | One or more occurrences (repeatable) |

Example: `FILLED_COMPONENT+` means the feature may appear multiple times within its parent `filledComponentSet` node.

---

## Namespace prefixes

Features are prefixed to indicate their role in the description language:

| Prefix | Namespace | Use |
|--------|-----------|-----|
| *(none)* | Core typological features | CONDITIONING, VIOLABILITY, STRICTURE, FOUNDATION, ELASTICITY, FILLEDNESS, STABILITY, and their sub-features |
| `MD:` | Metadata | Bibliographic source, external references — excluded from typological comparison |
| `AN:` | Annotation | Transcription strings and other surface annotations — excluded from typological comparison |
| `EX:` | Excluded-but-typological | Features not part of the core description language but potentially typologically relevant (function, liaison, filler class, conditions) |

The `skip_md`, `skip_an`, and `skip_ex` flags in `get_tabbed_desmemes()` control whether each namespace is included in the comparison graph.

---

## Desmeme features

### CONDITIONING *(required)*

How the template selects its filler(s).

| Value | Sub-features |
|-------|-------------|
| `constructionalConditioning` | — |
| `lexicoconstructionalConditioning` | `FILLER_POSITION*`, `FILLED_COMPONENTS*` |
| `prosodicConditioning` | — |

All conditioning types allow `EX:CONDITIONS*` (a free-text note).

**FILLER_POSITION** values: `templateInitial`, `templateFinal`, `templateMultiple`

**FILLED_COMPONENTS** has value `filledComponentSet`, containing one or more `FILLED_COMPONENT+` (@ref) lines naming the components that receive the filler.

### VIOLABILITY *(required)*

Whether the template ordering can be violated.

| Value | Sub-features |
|-------|-------------|
| `notViolable` | — |
| `potentiallyViolable` | `EXCEPTIONALITY`, `REPARABILITY` |

**EXCEPTIONALITY** values: `semantic`, `pragmatic`, `morphosyntactic`, `lexical`, `noKnownExceptions`

**REPARABILITY** values: `morphosyntacticInsertion`, `surfaceViolable`, `phonologicalInsertion`, `phonologicalRepair`

### STRICTURE *(required)*

The formal nature of the templatic constraint.

| Value | Sub-features |
|-------|-------------|
| `length` | `CONSTITUENT`, `COUNT` (@int) |
| `order` | `CONSTITUENT`, `COUNT` (@int), `RELATIONS` |

**CONSTITUENT** values for `length`: `Syllable`

**CONSTITUENT** values for `order`: `morphologicalConstituent`, `syntacticConstituent`, `morphosyntacticConstituent`, `prosodicPhrase`, `segment`

**RELATIONS** values: `simple`, `taxonomic`

### FOUNDATION *(required)*

The structural layout of the template — which positions exist and which components fill them.

#### `arch` foundation

An arch has up to five named positions:

| Feature | Cardinality | Meaning |
|---------|------------|---------|
| `LEFT_SUPPORT` | required | Leftmost element |
| `LEFT_VOUSSOIR*` | optional | Element just left of keystone |
| `KEYSTONE` | required | Central element |
| `RIGHT_VOUSSOIR*` | optional | Element just right of keystone |
| `RIGHT_SUPPORT` | required | Rightmost element |

#### `span` foundation

A span has two positions:

| Feature | Cardinality |
|---------|------------|
| `LEFT_SUPPORT` | required |
| `RIGHT_SUPPORT` | required |

#### RESTKOMPONENTEN

Both foundation types allow `RESTKOMPONENTEN*` (value: `restkomponentenSet`), containing one or more `RESTKOMPONENTE+` (@ref) lines for components that appear in the template but are not assigned to a named position.

### EX:FUNCTION *(optional)*

The grammatical function of the template. Value is a `@grammaticalCategory`.

### MD:HAS_SOURCE *(optional)*

Bibliographic provenance. Value is a source identifier (@ref). Sub-features:

| Feature | Cardinality | Content |
|---------|------------|---------|
| `MD:bibliographicCitation` | optional | Full citation string (@str) |
| `MD:EXTERNALREFERENCE*` | optional | URL or page reference (@str) |

---

## Component features

### ELASTICITY *(required)*

Whether the component has a fixed or variable slot count.

| Value | Sub-features |
|-------|-------------|
| `elastic` | `MINIMUM` (@int), `MAXIMUM` (@int) |
| `inelastic` | `COUNT` (@int) |

A COUNT of `0` encodes a null position. `MAXIMUM` of `∞` encodes an unbounded slot.

### FILLEDNESS *(required)*

What kind of content fills the component's slot(s).

| Value | Sub-features | Meaning |
|-------|-------------|---------|
| `open` | `COHERENCE*` | Slot is filled by any filler of the right type |
| `filled` | `FORM`, `EX:FILLER_CLASS*` | Slot has a fixed phonological form |
| `partiallyFilled` | `FILLER_PLACEMENT`, `FORM*`, `COHERENCE*`, `EX:FILLER_CLASS*` | Slot constrains the filler's position relative to fixed material |
| `null` | — | No phonological content |

**FORM** values: `canonicalLineate`, `embeddedDesmeme`, `reduplicant`

**FORM sub-features:**
- `AN:TRANSCRIPTION_STRING*` — phonological transcription (@str)
- `EX:LIAISON*` — how the form attaches to neighbours (@str; values: `sinistrous`, `dextrous`, `independent`)

**COHERENCE** values: `coherent`, `incoherent`

**COHERENCE sub-features:**
- `EX:CLASS*` — grammatical category for a coherent slot (@grammaticalCategory)
- `EX:CLASSES*` — one or more categories for an incoherent slot (@grammaticalCategory, repeatable)

**FILLER_PLACEMENT** values: `componentFinal`

**EX:FILLER_CLASS*** — grammatical category of the filler for filled/partiallyFilled slots (@grammaticalCategory)

### STABILITY *(required)*

Whether the component's position in the template is fixed.

| Value | Sub-features |
|-------|-------------|
| `stable` | — |
| `unstable` | `ASSOCIATE_POSITION`, `ASSOCIATE` |

**ASSOCIATE_POSITION** values: `left`, `right` — which side of the associate the unstable component appears on.

**ASSOCIATE** — @ref to the component this position is defined relative to.

---

## GrammaticalCategories.tsv

A flat list of valid `@grammaticalCategory` values, one per line. Values use three namespaces:

| Prefix | Source | Examples |
|--------|--------|---------|
| `gold:` | [GOLD ontology](http://linguistics-ontology.org/) | `gold:Verbal`, `gold:Noun`, `gold:Syllable` |
| `local:` | Project-specific categories | `local:valency`, `local:focus`, `local:imperative` |
| *(none)* | General cross-linguistic categories | `Adverbial`, `grammaticalCategory`, `prosodicWord` |

New values must be added to this file before they can be used in data; the validator will reject unknown grammatical categories.

---

## Validation

The validator (`tdag/validator.py`) checks:

1. **Feature allowed** — every feature at a given type is listed in the schema for that type
2. **Value valid** — terminal values match their sigil constraint or enumerated value list
3. **Required features present** — non-`*`/`+` features must appear
4. **Cross-file consistency** — every component referenced by `@ref` in a desmeme file must exist in the companion component file, and all components in the component file must be referenced by at least one desmeme

Run validation via the regression tests:
```bash
python -m pytest tests/test_regression.py::test_validation_smoke
```
