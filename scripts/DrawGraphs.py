"""
Generate graph visualizations and LaTeX AVMs from TSV data.

Usage (run from repo root):
  python scripts/DrawGraphs.py --lang nya
  python scripts/DrawGraphs.py --lang cao --format pdf --no-components

Arguments:
  --lang           ISO 639-3 language code (default: nya)
  --format         Output format for rendered graphs (default: pdf)
  --no-components  Exclude component internals from desmeme graphs
  --skip-md        Exclude MD: nodes from desmeme graphs
  --skip-an        Exclude AN: nodes from desmeme graphs
  --skip-ex        Exclude EX: nodes from desmeme graphs

Outputs (all under output/{lang}/):
  graphs/           Full desmeme graphs (.dot + rendered)
  component_graphs/ Component-only subgraphs (.dot + rendered)
  avms/             LaTeX AVM files (.tex)
"""

import argparse
import glob
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tdag.tabbed import get_tabbed_desmemes
from tdag.avm import avm
from tdag.comparison import draw_graphs, draw_components

parser = argparse.ArgumentParser(description="Generate graphs and AVMs from TSV data.")
parser.add_argument("--lang",          default="nya",  help="ISO 639-3 language code (default: nya)")
parser.add_argument("--format",        default="pdf",  help="Rendered graph format (default: pdf)")
parser.add_argument("--no-components", action="store_true", help="Exclude component internals from desmeme graphs")
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

out_base = os.path.join("output", args.lang)

graph_dir = os.path.join(out_base, "graphs")
print(f"Drawing desmeme graphs → {graph_dir}/")
draw_graphs(desmemes, graph_dir, format=args.format)

comp_dir = os.path.join(out_base, "component_graphs")
print(f"Drawing component graphs → {comp_dir}/")
draw_components(desmemes, comp_dir, format=args.format)

avm_dir = os.path.join(out_base, "avms")
os.makedirs(avm_dir, exist_ok=True)
print(f"Writing LaTeX AVMs → {avm_dir}/")
for desdag in desmemes:
    name = desdag.name
    template_avm = avm(name, "desmeme")
    template_avm.graph_toAVM(desdag)
    avm_path = os.path.join(avm_dir, name + ".tex")
    with open(avm_path, "w") as f:
        template_avm.to_latex(outfile=f)

print(f"Done: {len(desmemes)} desmemes → {out_base}/")
