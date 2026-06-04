import argparse
import glob
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tdag.tdag import tdag
from tdag.validator import schema
from tdag.avm import avm
from tdag.tabbed import get_tabbed_desmemes
from tdag.comparison import draw_graphs

parser = argparse.ArgumentParser(description="Read and display desmeme data.")
parser.add_argument("--lang", default="nya", help="ISO 639-3 language code (default: nya)")
args = parser.parse_args()

data_dir = os.path.join("data", args.lang)
des_matches  = glob.glob(os.path.join(data_dir, "*Desmemes.tsv"))
comp_matches = glob.glob(os.path.join(data_dir, "*Components.tsv"))
if not des_matches or not comp_matches:
    raise FileNotFoundError(f"No TSV data files found in {data_dir}/")

desmemeFileName   = des_matches[0]
componentFileName = comp_matches[0]
graphfolder       = "output/Graphs_full/"
desmemeSchemaFileName   = "schema/DesmemeSchema.tsv"
componentSchemaFileName = "schema/ComponentSchema.tsv"

desdags = get_tabbed_desmemes(desmemeFileName, componentFileName, desmemeSchemaFileName, componentSchemaFileName)

for desdag in desdags:
	
	name = desdag.name
		
	templateAVM = avm(name, "desmeme")
	templateAVM.graph_toAVM(desdag)

	# to_ASCII prints to STDOUT
	print("ID:\t" + name)
	templateAVM.to_ASCII()
	print()

	# expects a list of graphs; so construct a list of one element
	# maybe make a draw_graph function at some point?
	#draw_graphs([desdag], graphfolder)

# This breaks on full templates with metadata, etc.
#draw_graphs(desdags, graphfolder)
