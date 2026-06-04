"""
Compute pairwise simUI distances from TSV data and write a NEXUS file for SplitsTree.

Usage (run from repo root):
  python scripts/MakeNexus.py --lang nya
  python scripts/MakeNexus.py --lang cao --output output/cao.nex
  python scripts/MakeNexus.py --lang nya --no-components --skip-md --skip-an --skip-ex

Arguments:
  --lang            ISO 639-3 language code (default: nya)
  --output          Output path (default: output/{lang}.nex)
  --no-components   Exclude component internals from distance graph
  --skip-md         Exclude MD: (metadata) nodes from distance graph
  --skip-an         Exclude AN: (annotation) nodes from distance graph
  --skip-ex         Exclude EX: (excluded-but-typological) nodes from distance graph
"""

import argparse
import glob
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tdag.tabbed import get_tabbed_desmemes
from tdag.comparison import get_distances, to_nex

parser = argparse.ArgumentParser(description="Compute pairwise distances and write NEXUS file.")
parser.add_argument("--lang",          default="nya",  help="ISO 639-3 language code (default: nya)")
parser.add_argument("--output",        default=None,   help="Output path (default: output/{lang}.nex)")
parser.add_argument("--no-components", action="store_true", help="Exclude component internals")
parser.add_argument("--skip-md",       action="store_true", help="Exclude MD: nodes")
parser.add_argument("--skip-an",       action="store_true", help="Exclude AN: nodes")
parser.add_argument("--skip-ex",       action="store_true", help="Exclude EX: nodes")
args = parser.parse_args()

data_dir     = os.path.join("data", args.lang)
des_matches  = glob.glob(os.path.join(data_dir, "*Desmemes.tsv"))
comp_matches = glob.glob(os.path.join(data_dir, "*Components.tsv"))
if not des_matches or not comp_matches:
    raise FileNotFoundError(f"No TSV data files found in {data_dir}/")

desmemes = get_tabbed_desmemes(
    des_matches[0], comp_matches[0],
    "schema/DesmemeSchema.tsv", "schema/ComponentSchema.tsv",
    skip_components=args.no_components,
    skip_md=args.skip_md,
    skip_an=args.skip_an,
    skip_ex=args.skip_ex,
)

distances = get_distances(desmemes)

outpath = args.output or os.path.join("output", f"{args.lang}.nex")
os.makedirs(os.path.dirname(outpath), exist_ok=True)
to_nex(distances, outpath)
print(f"Wrote {len(desmemes)} x {len(desmemes)} distance matrix to {outpath}")
