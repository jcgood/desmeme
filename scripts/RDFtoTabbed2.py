"""
Migration script: reads an RDF template file and writes corrected TSV files.

Usage (run from repo root):
  python scripts/RDFtoTabbed2.py --lang nya --name Chichewa
  python scripts/RDFtoTabbed2.py --lang cao --name Chacobo --rdf rdf/template-cao.rdf

Arguments:
  --lang   ISO 639-3 language code (required); determines output directory data/{lang}/
  --name   Language name prefix for output filenames (required), e.g. Chichewa, Chacobo
  --rdf    Path to RDF source file (default: rdf/template-CHx.rdf)

Improvements over the original RDFtoTabbed.py:
- NT: prefixes replaced by MD:/AN:/EX: per the three-prefix scheme
- EX:CONDITIONS written under CONDITIONING (not under HAS_SOURCE)
- All previously dropped fields now exported:
    EX:FUNCTION (desmeme level)
    EX:FILLER_CLASS (component FILLEDNESS level)
    EX:CLASS / EX:CLASSES (component COHERENCE level)
    AN:TRANSCRIPTION_STRING (via FORM → TRANSCRIPTION node)
    EX:LIAISON (on FORM nodes)
    MD:EXTERNALREFERENCE (under MD:HAS_SOURCE)
- Grammatical category URIs converted to namespace-prefixed values
  (gold:Verbal, local:valency, Adverbial, grammaticalCategory, etc.)
- LIAISON values exported as bare local names (sinistrous, independent, dextrous)
"""

import argparse
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rdflib
from rdflib import URIRef, Literal, Namespace, RDF, RDFS

# Instance namespace
TEMPLATES  = Namespace("http://linguistics-ontology.org/jcgood/templates#")

# Predicate namespaces (verified against template-CHx.rdf)
SPECGEN    = Namespace("http://purl.org/linguistics/jcgood/specgeneral#")   # CONDITIONING
SPECTEMP   = Namespace("http://purl.org/linguistics/jcgood/spectemplate#")  # FOUNDATION, STRICTURE, foundation positions, RESTKOMPONENTEN(E), FILLED_COMPONENTS(T)
TEMPLATE   = Namespace("http://purl.org/linguistics/jcgood/template#")      # VIOLABILITY, FILLER_POSITION, EXCEPTIONALITY, REPARABILITY; type values: desmeme, order, length, span, arch, notViolable, potentiallyViolable, embeddedDesmeme
GENERAL    = Namespace("http://purl.org/linguistics/jcgood/general#")        # COUNT, CONSTITUENT, RELATIONS, MINIMUM, MAXIMUM; type values: conditioning types, simple, taxonomic, constituent types
COMPONENT  = Namespace("http://purl.org/linguistics/jcgood/component#")      # component type value; FILLER_PLACEMENT predicate; type values: elastic, inelastic, filled, open, partiallyFilled, null, coherent, incoherent, stable, unstable, restkomponentenSet, filledComponentSet
SPECCOMP   = Namespace("http://purl.org/linguistics/jcgood/speccomponent#")  # ELASTICITY, FILLEDNESS, STABILITY, COHERENCE, FORM, ASSOCIATE, ASSOCIATE_POSITION
FUNCTION   = Namespace("http://purl.org/linguistics/jcgood/function#")       # FUNCTION, FILLER_CLASS, CLASS, CLASSES
FORM_NS    = Namespace("http://purl.org/linguistics/jcgood/form#")           # LIAISON predicate; form type values: canonicalLineate, sinistrous, etc.
SPECFORM   = Namespace("http://purl.org/linguistics/jcgood/specform#")       # TRANSCRIPTION predicate, TRANSCRIPTION_STRING predicate
NOTES      = Namespace("http://purl.org/linguistics/jcgood/notes#")          # HAS_SOURCE, EXTERNALREFERENCE, CONDITIONS
DCTERMS    = Namespace("http://purl.org/dc/terms#")                           # bibliographicCitation (note: # not /)
GOLD_NS    = "http://purl.org/linguistics/gold#"
GENERAL_NS = "http://purl.org/linguistics/jcgood/general#"
LOCAL_NS   = "http://purl.org/linguistics/jcgood/localcategory#"

parser = argparse.ArgumentParser(description="Export RDF template data to TSV.")
parser.add_argument("--lang", required=True, help="ISO 639-3 language code (e.g. nya, cao)")
parser.add_argument("--name", required=True, help="Language name prefix for filenames (e.g. Chichewa, Chacobo)")
parser.add_argument("--rdf",  default="rdf/template-CHx.rdf", help="Path to RDF source file")
args = parser.parse_args()

LANGUAGE = args.lang

g = rdflib.Graph()
g.parse(args.rdf, format="xml")

# Known data gaps in the RDF that must be patched during migration.
# Each entry is (component_label, feature, value) to be written if the feature
# is absent from the RDF. Tracked in issues #14 and #15.
COMPONENT_PATCHES = {
    "ChichewaNPRightVoussoir": [("STABILITY", "stable")],
}


def gramcat(uri):
    """Convert a grammatical category URI to its namespace-prefixed TSV value."""
    uri = str(uri)
    if uri.startswith(GOLD_NS):    return "gold:" + uri[len(GOLD_NS):]
    if uri.startswith(LOCAL_NS):   return "local:" + uri[len(LOCAL_NS):]
    if uri.startswith(GENERAL_NS): return uri[len(GENERAL_NS):]
    return uri


def get(node, pred):
    return g.value(node, pred)


def getall(node, pred):
    return list(g.objects(node, pred))


def lname(node):
    """Local name after # in a URI node."""
    return str(node).split("#")[-1]


def rlabel(node):
    """rdfs:label of a node, falling back to local name."""
    v = g.value(node, RDFS.label)
    return str(v) if v else lname(node)


def write_component(comp, out, seen, first=False):
    comp_id = rlabel(comp)
    if comp_id in seen:
        return
    seen.add(comp_id)

    if not first:
        out.write("\n")
    out.write(f"IDENTIFIER\t{comp_id}\n")
    out.write(f"LANGUAGE\t{LANGUAGE}\n")

    elasticity = get(comp, SPECCOMP["ELASTICITY"])
    if elasticity:
        etype = lname(get(elasticity, RDF.type))
        out.write(f"ELASTICITY\t{etype}\n")
        if etype == "elastic":
            mn = get(elasticity, GENERAL["MINIMUM"])
            mx = get(elasticity, GENERAL["MAXIMUM"])
            if mn is not None: out.write(f"\tMINIMUM\t{mn}\n")
            if mx is not None: out.write(f"\tMAXIMUM\t{mx}\n")
        elif etype == "inelastic":
            cnt = get(elasticity, GENERAL["COUNT"])
            if cnt is not None: out.write(f"\tCOUNT\t{cnt}\n")

    filledness = get(comp, SPECCOMP["FILLEDNESS"])
    if filledness:
        ftype = lname(get(filledness, RDF.type))
        out.write(f"FILLEDNESS\t{ftype}\n")

        filler_class = get(filledness, FUNCTION["FILLER_CLASS"])
        if filler_class:
            out.write(f"\tEX:FILLER_CLASS\t{gramcat(filler_class)}\n")

        if ftype in ("open", "partiallyFilled"):
            if ftype == "partiallyFilled":
                placement = get(filledness, COMPONENT["FILLER_PLACEMENT"])
                if placement:
                    out.write(f"\tFILLER_PLACEMENT\t{lname(placement)}\n")
                form = get(filledness, SPECCOMP["FORM"])
                if form:
                    form_type = lname(get(form, RDF.type))
                    out.write(f"\tFORM\t{form_type}\n")
                    trans = get(form, SPECFORM["TRANSCRIPTION"])
                    if trans:
                        ts = get(trans, SPECFORM["TRANSCRIPTION_STRING"])
                        if ts: out.write(f"\t\tAN:TRANSCRIPTION_STRING\t{ts}\n")
                    liaison = get(form, FORM_NS["LIAISON"])
                    if liaison:
                        out.write(f"\t\tEX:LIAISON\t{lname(liaison)}\n")

            coherence = get(filledness, SPECCOMP["COHERENCE"])
            if coherence:
                ctype = lname(get(coherence, RDF.type))
                out.write(f"\tCOHERENCE\t{ctype}\n")
                cls = get(coherence, FUNCTION["CLASS"])
                if cls:
                    out.write(f"\t\tEX:CLASS\t{gramcat(cls)}\n")
                for c in sorted(getall(coherence, FUNCTION["CLASSES"]), key=str):
                    out.write(f"\t\tEX:CLASSES\t{gramcat(c)}\n")

        elif ftype == "filled":
            form = get(filledness, SPECCOMP["FORM"])
            if form:
                form_type = lname(get(form, RDF.type))
                out.write(f"\tFORM\t{form_type}\n")
                trans = get(form, SPECFORM["TRANSCRIPTION"])
                if trans:
                    ts = get(trans, SPECFORM["TRANSCRIPTION_STRING"])
                    if ts: out.write(f"\t\tAN:TRANSCRIPTION_STRING\t{ts}\n")
                liaison = get(form, FORM_NS["LIAISON"])
                if liaison:
                    out.write(f"\t\tEX:LIAISON\t{lname(liaison)}\n")

    stability = get(comp, SPECCOMP["STABILITY"])
    if stability:
        stype = lname(get(stability, RDF.type))
        out.write(f"STABILITY\t{stype}\n")
        if stype == "unstable":
            assoc_pos_node = get(stability, SPECCOMP["ASSOCIATE_POSITION"])
            if assoc_pos_node:
                out.write(f"\tASSOCIATE_POSITION\t{lname(get(assoc_pos_node, RDF.type))}\n")
            assoc = get(stability, SPECCOMP["ASSOCIATE"])
            if assoc:
                out.write(f"\tASSOCIATE\t{rlabel(assoc)}\n")
    else:
        for feat, val in COMPONENT_PATCHES.get(comp_id, []):
            if feat == "STABILITY":
                out.write(f"STABILITY\t{val}\n")


def write_desmeme(d, out, first=False):
    d_id = rlabel(d)
    if not first:
        out.write("\n")
    out.write(f"IDENTIFIER\t{d_id}\n")
    out.write(f"LANGUAGE\t{LANGUAGE}\n")

    # CONDITIONING
    cond_node = get(d, SPECGEN["CONDITIONING"])
    if cond_node:
        ctype = lname(get(cond_node, RDF.type))
        out.write(f"CONDITIONING\t{ctype}\n")
        if ctype == "lexicoconstructionalConditioning":
            fpos = get(cond_node, TEMPLATE["FILLER_POSITION"])
            if fpos:
                out.write(f"\tFILLER_POSITION\t{lname(fpos)}\n")
            fcomps_node = get(cond_node, SPECTEMP["FILLED_COMPONENTS"])
            if fcomps_node:
                out.write(f"\tFILLED_COMPONENTS\tfilledComponentSet\n")
                for fc in sorted(getall(fcomps_node, SPECTEMP["FILLED_COMPONENT"]), key=rlabel):
                    out.write(f"\t\tFILLED_COMPONENT\t{rlabel(fc)}\n")
        conditions = get(cond_node, NOTES["CONDITIONS"])
        if conditions:
            out.write(f"\tEX:CONDITIONS\t{conditions}\n")

    # EX:FUNCTION
    func = get(d, FUNCTION["FUNCTION"])
    if func:
        out.write(f"EX:FUNCTION\t{gramcat(func)}\n")

    # VIOLABILITY
    viol_node = get(d, TEMPLATE["VIOLABILITY"])
    if viol_node:
        vtype = lname(get(viol_node, RDF.type))
        out.write(f"VIOLABILITY\t{vtype}\n")
        if vtype == "potentiallyViolable":
            exc = get(viol_node, TEMPLATE["EXCEPTIONALITY"])
            if exc: out.write(f"\tEXCEPTIONALITY\t{lname(exc)}\n")
            rep = get(viol_node, TEMPLATE["REPARABILITY"])
            if rep: out.write(f"\tREPARABILITY\t{lname(rep)}\n")

    # STRICTURE
    strict_node = get(d, SPECTEMP["STRICTURE"])
    if strict_node:
        stype = lname(get(strict_node, RDF.type))
        out.write(f"STRICTURE\t{stype}\n")
        constituent = get(strict_node, GENERAL["CONSTITUENT"])
        if constituent: out.write(f"\tCONSTITUENT\t{lname(constituent)}\n")
        count = get(strict_node, GENERAL["COUNT"])
        if count is not None: out.write(f"\tCOUNT\t{count}\n")
        relations = get(strict_node, GENERAL["RELATIONS"])
        if relations: out.write(f"\tRELATIONS\t{lname(relations)}\n")

    # FOUNDATION
    found_node = get(d, SPECTEMP["FOUNDATION"])
    if found_node:
        ftype = lname(get(found_node, RDF.type))
        out.write(f"FOUNDATION\t{ftype}\n")
        if ftype == "arch":
            for feat, pred in [
                ("LEFT_SUPPORT",   SPECTEMP["LEFT_SUPPORT"]),
                ("LEFT_VOUSSOIR",  SPECTEMP["LEFT_VOUSSOIR"]),
                ("KEYSTONE",       SPECTEMP["KEYSTONE"]),
                ("RIGHT_VOUSSOIR", SPECTEMP["RIGHT_VOUSSOIR"]),
                ("RIGHT_SUPPORT",  SPECTEMP["RIGHT_SUPPORT"]),
            ]:
                comp = get(found_node, pred)
                if comp: out.write(f"\t{feat}\t{rlabel(comp)}\n")
        elif ftype == "span":
            ls = get(found_node, SPECTEMP["LEFT_SUPPORT"])
            rs = get(found_node, SPECTEMP["RIGHT_SUPPORT"])
            if ls: out.write(f"\tLEFT_SUPPORT\t{rlabel(ls)}\n")
            if rs: out.write(f"\tRIGHT_SUPPORT\t{rlabel(rs)}\n")

        rk_set = get(found_node, SPECTEMP["RESTKOMPONENTEN"])
        if rk_set:
            out.write(f"\tRESTKOMPONENTEN\trestkomponentenSet\n")
            for rk in sorted(getall(rk_set, SPECTEMP["RESTKOMPONENTE"]), key=rlabel):
                out.write(f"\t\tRESTKOMPONENTE\t{rlabel(rk)}\n")

    # MD:HAS_SOURCE
    source = get(d, NOTES["HAS_SOURCE"])
    if source:
        out.write(f"MD:HAS_SOURCE\t{rlabel(source)}\n")
        bib = get(source, DCTERMS["bibliographicCitation"])
        if bib: out.write(f"\tMD:bibliographicCitation\t{bib}\n")
        extref = get(source, NOTES["EXTERNALREFERENCE"])
        if extref: out.write(f"\tMD:EXTERNALREFERENCE\t{extref}\n")


def collect_referenced_components(desmemes):
    """Return all component nodes reachable from the given desmemes."""
    comp_type = COMPONENT["component"]
    referenced = set()
    queue = list(desmemes)
    visited_nodes = set()
    while queue:
        node = queue.pop()
        if node in visited_nodes:
            continue
        visited_nodes.add(node)
        for p, o in g.predicate_objects(node):
            if isinstance(o, URIRef) and o not in visited_nodes:
                if (o, RDF.type, comp_type) in g:
                    referenced.add(o)
                queue.append(o)
    return referenced


def main():
    desmeme_type = TEMPLATE["desmeme"]
    desmemes = sorted(g.subjects(RDF.type, desmeme_type), key=rlabel)
    all_comps = sorted(collect_referenced_components(desmemes), key=rlabel)

    print(f"Found {len(desmemes)} desmemes, {len(all_comps)} components")

    out_dir = os.path.join("data", args.lang)
    os.makedirs(out_dir, exist_ok=True)
    des_path  = os.path.join(out_dir, f"{args.name}Desmemes.tsv")
    comp_path = os.path.join(out_dir, f"{args.name}Components.tsv")

    with open(des_path, "w") as out:
        for i, d in enumerate(desmemes):
            write_desmeme(d, out, first=(i == 0))

    seen = set()
    with open(comp_path, "w") as out:
        first = True
        for comp in all_comps:
            if rlabel(comp) not in seen:
                write_component(comp, out, seen, first=first)
                first = False

    print(f"Wrote {des_path} and {comp_path}")


if __name__ == "__main__":
    main()
