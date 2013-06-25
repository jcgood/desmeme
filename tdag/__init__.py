# Import graphviz
import sys
sys.path.append('..')
sys.path.append('/usr/local/lib/graphviz/python/')
sys.path.append('.')
#import gv

# Import pygraph
from pygraph.classes.graph import graph as pygraph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
from pygraph.readwrite.dot import write

from rdflib import Graph as rdfGraph
from rdflib import URIRef, Literal, BNode, Namespace, RDF, RDFS

from despecification import *
from tdag import *
from comparison import *