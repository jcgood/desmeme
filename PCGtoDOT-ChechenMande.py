from pygraph.classes.digraph import digraph
from pygraph.readwrite.markup import write
import pydot
import tdag
from tdag import draw_graphs

pcgweighted = tdag.tdag("ChechenMande-weighted")
pcglabels = tdag.tdag("ChechenMande-labels")
ChechenPreverbalA = tdag.tdag("ChechenPreverbalA")
MandeClause = tdag.tdag("MandeClause")

try: pcgweighted.add_node("count1-c2/count1-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count1-c2/count1-m1", "inelastic-c2/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-c2/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count1-c2/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/inelastic-m1", "count1-c2/count1-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("potentiallyViolable/notViolable", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "potentiallyViolable/notViolable"), label=" 0.25")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m2", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m2", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m2", "component-c1/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-c1/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/elastic-m1", "component-c1/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-c2/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-c2/stable-m2", "component-c2/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m4", "")
except: pass
try: pcgweighted.add_node("incoherent-c1/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m4", "incoherent-c1/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("prosodicWord/syntacticConstituent", "")
except: pass
try: pcgweighted.add_node("length/order", "")
except: pass

try: pcgweighted.add_edge(("prosodicWord/syntacticConstituent", "length/order"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-c1/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m2", "stable-c1/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c1/component-m3", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m3", "inelastic-c1/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-c1/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-c1/coherent-m4", "open-c1/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m5", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m5", "inelastic-c1/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c2/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-c2/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m5", "stable-c2/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c2/component-m3", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m3", "inelastic-c2/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-c1/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count1-c1/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/inelastic-m1", "count1-c1/count1-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-c1/open-m4", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m4", "component-c2/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-c1/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-c1/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m4", "stable-c1/stable-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-c2/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m4", "stable-c2/stable-m4"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-c1/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m3", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/elastic-m2", "component-c1/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-c1/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-c1/coherent-m3", "open-c1/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("open-c1/open-m1", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m1", "component-c2/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m5", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m5", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m5", "component-c1/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m5", "")
except: pass
try: pcgweighted.add_node("incoherent-c1/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m5", "incoherent-c1/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-c1/component-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m2", "inelastic-c1/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("incoherent-c1/coherent-m4", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m5", "")
except: pass

try: pcgweighted.add_edge(("incoherent-c1/coherent-m4", "partiallyFilled-c1/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("open-c1/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-c1/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m4", "coherent-c1/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("incoherent-c1/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m4", "")
except: pass

try: pcgweighted.add_edge(("incoherent-c1/incoherent-m1", "partiallyFilled-c1/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-c1/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-c1/stable-m3", "component-c1/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m2", "inelastic-c2/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("count1-c2/count5-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/order", "")
except: pass

try: pcgweighted.add_edge(("count1-c2/count5-m1", "inelastic-c2/order"), label=" 1")
except: pass

try: pcgweighted.add_node("count2-c1/count1-m2", "")
except: pass
try: pcgweighted.add_node("length/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count2-c1/count1-m2", "length/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-c2/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/elastic-m1", "component-c2/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("potentiallyViolable/notViolable", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("potentiallyViolable/notViolable", "desmeme/desmeme"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-c2/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m3", "stable-c2/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("incoherent-c1/coherent-m1", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m1", "")
except: pass

try: pcgweighted.add_edge(("incoherent-c1/coherent-m1", "partiallyFilled-c1/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("span/arch", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "span/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("stable-c1/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-c1/stable-m1", "component-c1/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-c1/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-c1/incoherent-m1", "open-c1/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-c2/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-c2/stable-m1", "component-c2/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m1", "")
except: pass
try: pcgweighted.add_node("incoherent-c1/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m1", "incoherent-c1/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m4", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m4", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m4", "component-c1/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("count1-c2/count1-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count1-c2/count1-m2", "inelastic-c2/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m5", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m5", "open-c1/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("count2-c1/count1-m1", "")
except: pass
try: pcgweighted.add_node("length/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count2-c1/count1-m1", "length/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m4", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m4", "partiallyFilled-c1/open-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-c1/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-c1/coherent-m1", "open-c1/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m3", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m3", "open-c1/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("count1-c1/count1-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count1-c1/count1-m2", "inelastic-c1/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m4", "inelastic-c2/elastic-m3"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-c2/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/inelastic-m1", "component-c2/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-c1/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-c1/stable-m2", "component-c1/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m2", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m2", "open-c1/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c1/component-m5", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m5", "partiallyFilled-c1/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c2/component-m1", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m1", "open-c1/open-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-c1/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-c1/coherent-m2", "open-c1/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-c2/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-c2/stable-m5", "component-c2/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m1", "partiallyFilled-c1/open-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("count1-c1/count1-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count1-c1/count1-m1", "inelastic-c1/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-c1/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m1", "stable-c1/stable-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-c2/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-c2/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m1", "stable-c2/stable-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-c1/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m5", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/inelastic-m2", "component-c1/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-c1/component-m2", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m2", "partiallyFilled-c1/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass
try: pcgweighted.add_node("open-c1/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m4", "open-c1/open-m4"), label=" 0.25")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m1", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m1", "component-c1/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-c2/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-c2/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m2", "stable-c2/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c1/component-m3", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m3", "partiallyFilled-c1/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("span/arch", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("span/arch", "component-c2/component-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-c2/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m3", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/elastic-m2", "component-c2/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass
try: pcgweighted.add_node("span/arch", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m1", "span/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-c1/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-c1/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m3", "stable-c1/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-c2/order", "")
except: pass
try: pcgweighted.add_node("count1-c2/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/order", "count1-c2/count5-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-c1/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-c1/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m2", "coherent-c1/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m2", "")
except: pass
try: pcgweighted.add_node("incoherent-c1/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m2", "incoherent-c1/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-c1/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-c1/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m5", "stable-c1/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-c1/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/inelastic-m1", "component-c1/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-c2/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count1-c2/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/inelastic-m2", "count1-c2/count1-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-c1/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-c1/stable-m5", "component-c1/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-c2/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-c2/stable-m4", "component-c2/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-c1/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count1-c1/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/inelastic-m2", "count1-c1/count1-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-c2/component-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m1", "inelastic-c2/inelastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m3", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m3", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m3", "component-c1/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-c1/open-m3", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m3", "component-c2/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("span/arch", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("span/arch", "desmeme/desmeme"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m1", "inelastic-c1/inelastic-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("partiallyFilled-c1/open-m3", "")
except: pass
try: pcgweighted.add_node("incoherent-c1/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("partiallyFilled-c1/open-m3", "incoherent-c1/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-c1/open-m2", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m2", "component-c2/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-c2/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-c2/stable-m3", "component-c2/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c1/component-m4", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-c1/component-m4", "inelastic-c1/elastic-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-c1/order", "")
except: pass
try: pcgweighted.add_node("count1-c1/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/order", "count1-c1/count5-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("span/arch", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("span/arch", "component-c1/component-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("lexicoconstructionalConditioning/constructionalConditioning", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "lexicoconstructionalConditioning/constructionalConditioning"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-c1/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m4", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c1/elastic-m3", "component-c1/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-c2/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/elastic-m3", "component-c2/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("incoherent-c1/coherent-m3", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m3", "")
except: pass

try: pcgweighted.add_edge(("incoherent-c1/coherent-m3", "partiallyFilled-c1/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("open-c1/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-c1/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m1", "coherent-c1/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("length/order", "")
except: pass
try: pcgweighted.add_node("prosodicWord/syntacticConstituent", "")
except: pass

try: pcgweighted.add_edge(("length/order", "prosodicWord/syntacticConstituent"), label=" 0.33")
except: pass

try: pcgweighted.add_node("stable-c1/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-c1/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-c1/stable-m4", "component-c1/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m4", "")
except: pass
try: pcgweighted.add_node("span/arch", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m4", "span/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("length/order", "")
except: pass
try: pcgweighted.add_node("count2-c1/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("length/order", "count2-c1/count5-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-c1/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-c1/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m3", "coherent-c1/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("incoherent-c1/coherent-m2", "")
except: pass
try: pcgweighted.add_node("partiallyFilled-c1/open-m2", "")
except: pass

try: pcgweighted.add_edge(("incoherent-c1/coherent-m2", "partiallyFilled-c1/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-c2/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m5", "")
except: pass

try: pcgweighted.add_edge(("inelastic-c2/inelastic-m2", "component-c2/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-c1/open-m5", "")
except: pass
try: pcgweighted.add_node("component-c2/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m5", "component-c2/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("lexicoconstructionalConditioning/constructionalConditioning", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("lexicoconstructionalConditioning/constructionalConditioning", "desmeme/desmeme"), label=" 1")
except: pass

try: pcgweighted.add_node("component-c2/component-m5", "")
except: pass
try: pcgweighted.add_node("inelastic-c2/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-c2/component-m5", "inelastic-c2/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("length/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count2-c1/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("length/inelastic-m1", "count2-c1/count1-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-c1/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-c1/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-c1/open-m5", "coherent-c1/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("length/order", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "length/order"), label=" 0.25")
except: pass

try: pcgweighted.add_node("length/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count2-c1/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("length/inelastic-m2", "count2-c1/count1-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("count2-c1/count5-m1", "")
except: pass
try: pcgweighted.add_node("length/order", "")
except: pass

try: pcgweighted.add_edge(("count2-c1/count5-m1", "length/order"), label=" 1")
except: pass

try: pcgweighted.add_node("count1-c1/count5-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-c1/order", "")
except: pass

try: pcgweighted.add_edge(("count1-c1/count5-m1", "inelastic-c1/order"), label=" 1")
except: pass

try: pcgweighted.add_node("length/order", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("length/order", "desmeme/desmeme"), label=" 0.33")
except: pass

try: pcglabels.add_node("count1-c2/count1-m1", "")
except: pass
try: pcglabels.add_node("inelastic-c2/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count1-c2/count1-m1", "inelastic-c2/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("inelastic-c2/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count1-c2/count1-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/inelastic-m1", "count1-c2/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("potentiallyViolable/notViolable", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "potentiallyViolable/notViolable"), label="VIOLABILITY")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m2", "")
except: pass
try: pcglabels.add_node("component-c1/component-m2", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m2", "component-c1/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic-c1/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-c1/component-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/elastic-m1", "component-c1/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-c2/stable-m2", "")
except: pass
try: pcglabels.add_node("component-c2/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-c2/stable-m2", "component-c2/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m4", "")
except: pass
try: pcglabels.add_node("incoherent-c1/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m4", "incoherent-c1/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("prosodicWord/syntacticConstituent", "")
except: pass
try: pcglabels.add_node("length/order", "")
except: pass

try: pcglabels.add_edge(("prosodicWord/syntacticConstituent", "length/order"), label="CONSTITUENT")
except: pass

try: pcglabels.add_node("component-c1/component-m2", "")
except: pass
try: pcglabels.add_node("stable-c1/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m2", "stable-c1/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c1/component-m3", "")
except: pass
try: pcglabels.add_node("inelastic-c1/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m3", "inelastic-c1/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("coherent-c1/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-c1/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-c1/coherent-m4", "open-c1/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-c1/component-m5", "")
except: pass
try: pcglabels.add_node("inelastic-c1/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m5", "inelastic-c1/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-c2/component-m5", "")
except: pass
try: pcglabels.add_node("stable-c2/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m5", "stable-c2/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m3", "")
except: pass
try: pcglabels.add_node("inelastic-c2/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m3", "inelastic-c2/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-c1/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count1-c1/count1-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/inelastic-m1", "count1-c1/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("open-c1/open-m4", "")
except: pass
try: pcglabels.add_node("component-c2/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m4", "component-c2/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-c1/component-m4", "")
except: pass
try: pcglabels.add_node("stable-c1/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m4", "stable-c1/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m4", "")
except: pass
try: pcglabels.add_node("stable-c2/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m4", "stable-c2/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-c1/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-c1/component-m3", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/elastic-m2", "component-c1/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("coherent-c1/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-c1/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-c1/coherent-m3", "open-c1/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-c1/open-m1", "")
except: pass
try: pcglabels.add_node("component-c2/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m1", "component-c2/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m5", "")
except: pass
try: pcglabels.add_node("component-c1/component-m5", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m5", "component-c1/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m5", "")
except: pass
try: pcglabels.add_node("incoherent-c1/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m5", "incoherent-c1/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-c1/component-m2", "")
except: pass
try: pcglabels.add_node("inelastic-c1/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m2", "inelastic-c1/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("incoherent-c1/coherent-m4", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m5", "")
except: pass

try: pcglabels.add_edge(("incoherent-c1/coherent-m4", "partiallyFilled-c1/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-c1/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-c1/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m4", "coherent-c1/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("incoherent-c1/incoherent-m1", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m4", "")
except: pass

try: pcglabels.add_edge(("incoherent-c1/incoherent-m1", "partiallyFilled-c1/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-c1/stable-m3", "")
except: pass
try: pcglabels.add_node("component-c1/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-c1/stable-m3", "component-c1/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m2", "")
except: pass
try: pcglabels.add_node("inelastic-c2/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m2", "inelastic-c2/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("count1-c2/count5-m1", "")
except: pass
try: pcglabels.add_node("inelastic-c2/order", "")
except: pass

try: pcglabels.add_edge(("count1-c2/count5-m1", "inelastic-c2/order"), label="COUNT")
except: pass

try: pcglabels.add_node("count2-c1/count1-m2", "")
except: pass
try: pcglabels.add_node("length/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count2-c1/count1-m2", "length/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("inelastic-c2/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-c2/component-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/elastic-m1", "component-c2/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("potentiallyViolable/notViolable", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("potentiallyViolable/notViolable", "desmeme/desmeme"), label="VIOLABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m3", "")
except: pass
try: pcglabels.add_node("stable-c2/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m3", "stable-c2/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("incoherent-c1/coherent-m1", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m1", "")
except: pass

try: pcglabels.add_edge(("incoherent-c1/coherent-m1", "partiallyFilled-c1/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("span/arch", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "span/arch"), label="FOUNDATION")
except: pass

try: pcglabels.add_node("stable-c1/stable-m1", "")
except: pass
try: pcglabels.add_node("component-c1/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-c1/stable-m1", "component-c1/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-c1/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-c1/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-c1/incoherent-m1", "open-c1/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-c2/stable-m1", "")
except: pass
try: pcglabels.add_node("component-c2/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-c2/stable-m1", "component-c2/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m1", "")
except: pass
try: pcglabels.add_node("incoherent-c1/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m1", "incoherent-c1/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m4", "")
except: pass
try: pcglabels.add_node("component-c1/component-m4", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m4", "component-c1/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count1-c2/count1-m2", "")
except: pass
try: pcglabels.add_node("inelastic-c2/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count1-c2/count1-m2", "inelastic-c2/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("component-c2/component-m5", "")
except: pass
try: pcglabels.add_node("open-c1/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m5", "open-c1/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count2-c1/count1-m1", "")
except: pass
try: pcglabels.add_node("length/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count2-c1/count1-m1", "length/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-c1/component-m4", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m4", "partiallyFilled-c1/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("coherent-c1/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-c1/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-c1/coherent-m1", "open-c1/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-c2/component-m3", "")
except: pass
try: pcglabels.add_node("open-c1/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m3", "open-c1/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count1-c1/count1-m2", "")
except: pass
try: pcglabels.add_node("inelastic-c1/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count1-c1/count1-m2", "inelastic-c1/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("component-c2/component-m4", "")
except: pass
try: pcglabels.add_node("inelastic-c2/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m4", "inelastic-c2/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-c2/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-c2/component-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/inelastic-m1", "component-c2/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-c1/stable-m2", "")
except: pass
try: pcglabels.add_node("component-c1/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-c1/stable-m2", "component-c1/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m2", "")
except: pass
try: pcglabels.add_node("open-c1/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m2", "open-c1/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-c1/component-m5", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m5", "partiallyFilled-c1/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-c2/component-m1", "")
except: pass
try: pcglabels.add_node("open-c1/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m1", "open-c1/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("coherent-c1/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-c1/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-c1/coherent-m2", "open-c1/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-c2/stable-m5", "")
except: pass
try: pcglabels.add_node("component-c2/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-c2/stable-m5", "component-c2/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c1/component-m1", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m1", "partiallyFilled-c1/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count1-c1/count1-m1", "")
except: pass
try: pcglabels.add_node("inelastic-c1/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count1-c1/count1-m1", "inelastic-c1/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-c1/component-m1", "")
except: pass
try: pcglabels.add_node("stable-c1/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m1", "stable-c1/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m1", "")
except: pass
try: pcglabels.add_node("stable-c2/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m1", "stable-c2/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-c1/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-c1/component-m5", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/inelastic-m2", "component-c1/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-c1/component-m2", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m2", "partiallyFilled-c1/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-c2/component-m4", "")
except: pass
try: pcglabels.add_node("open-c1/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m4", "open-c1/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m1", "")
except: pass
try: pcglabels.add_node("component-c1/component-m1", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m1", "component-c1/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-c2/component-m2", "")
except: pass
try: pcglabels.add_node("stable-c2/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m2", "stable-c2/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c1/component-m3", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m3", "partiallyFilled-c1/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("span/arch", "")
except: pass
try: pcglabels.add_node("component-c2/component-m4", "")
except: pass

try: pcglabels.add_edge(("span/arch", "component-c2/component-m4"), label="RIGHT_SUPPORT")
except: pass

try: pcglabels.add_node("inelastic-c2/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-c2/component-m3", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/elastic-m2", "component-c2/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-c1/component-m1", "")
except: pass
try: pcglabels.add_node("span/arch", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m1", "span/arch"), label="LEFT_SUPPORT")
except: pass

try: pcglabels.add_node("component-c1/component-m3", "")
except: pass
try: pcglabels.add_node("stable-c1/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m3", "stable-c1/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-c2/order", "")
except: pass
try: pcglabels.add_node("count1-c2/count5-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/order", "count1-c2/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("open-c1/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-c1/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m2", "coherent-c1/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m2", "")
except: pass
try: pcglabels.add_node("incoherent-c1/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m2", "incoherent-c1/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-c1/component-m5", "")
except: pass
try: pcglabels.add_node("stable-c1/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m5", "stable-c1/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-c1/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-c1/component-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/inelastic-m1", "component-c1/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-c2/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count1-c2/count1-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/inelastic-m2", "count1-c2/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("stable-c1/stable-m5", "")
except: pass
try: pcglabels.add_node("component-c1/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-c1/stable-m5", "component-c1/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("stable-c2/stable-m4", "")
except: pass
try: pcglabels.add_node("component-c2/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-c2/stable-m4", "component-c2/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-c1/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count1-c1/count1-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/inelastic-m2", "count1-c1/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("component-c2/component-m1", "")
except: pass
try: pcglabels.add_node("inelastic-c2/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m1", "inelastic-c2/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m3", "")
except: pass
try: pcglabels.add_node("component-c1/component-m3", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m3", "component-c1/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-c1/open-m3", "")
except: pass
try: pcglabels.add_node("component-c2/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m3", "component-c2/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("span/arch", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("span/arch", "desmeme/desmeme"), label="FOUNDATION")
except: pass

try: pcglabels.add_node("component-c1/component-m1", "")
except: pass
try: pcglabels.add_node("inelastic-c1/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m1", "inelastic-c1/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("partiallyFilled-c1/open-m3", "")
except: pass
try: pcglabels.add_node("incoherent-c1/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("partiallyFilled-c1/open-m3", "incoherent-c1/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-c1/open-m2", "")
except: pass
try: pcglabels.add_node("component-c2/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m2", "component-c2/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("stable-c2/stable-m3", "")
except: pass
try: pcglabels.add_node("component-c2/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-c2/stable-m3", "component-c2/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c1/component-m4", "")
except: pass
try: pcglabels.add_node("inelastic-c1/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-c1/component-m4", "inelastic-c1/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-c1/order", "")
except: pass
try: pcglabels.add_node("count1-c1/count5-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/order", "count1-c1/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("span/arch", "")
except: pass
try: pcglabels.add_node("component-c1/component-m1", "")
except: pass

try: pcglabels.add_edge(("span/arch", "component-c1/component-m1"), label="LEFT_SUPPORT")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("lexicoconstructionalConditioning/constructionalConditioning", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "lexicoconstructionalConditioning/constructionalConditioning"), label="CONDITIONING")
except: pass

try: pcglabels.add_node("inelastic-c1/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-c1/component-m4", "")
except: pass

try: pcglabels.add_edge(("inelastic-c1/elastic-m3", "component-c1/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-c2/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-c2/component-m4", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/elastic-m3", "component-c2/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("incoherent-c1/coherent-m3", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m3", "")
except: pass

try: pcglabels.add_edge(("incoherent-c1/coherent-m3", "partiallyFilled-c1/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-c1/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-c1/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m1", "coherent-c1/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("length/order", "")
except: pass
try: pcglabels.add_node("prosodicWord/syntacticConstituent", "")
except: pass

try: pcglabels.add_edge(("length/order", "prosodicWord/syntacticConstituent"), label="CONSTITUENT")
except: pass

try: pcglabels.add_node("stable-c1/stable-m4", "")
except: pass
try: pcglabels.add_node("component-c1/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-c1/stable-m4", "component-c1/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-c2/component-m4", "")
except: pass
try: pcglabels.add_node("span/arch", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m4", "span/arch"), label="RIGHT_SUPPORT")
except: pass

try: pcglabels.add_node("length/order", "")
except: pass
try: pcglabels.add_node("count2-c1/count5-m1", "")
except: pass

try: pcglabels.add_edge(("length/order", "count2-c1/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("open-c1/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-c1/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m3", "coherent-c1/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("incoherent-c1/coherent-m2", "")
except: pass
try: pcglabels.add_node("partiallyFilled-c1/open-m2", "")
except: pass

try: pcglabels.add_edge(("incoherent-c1/coherent-m2", "partiallyFilled-c1/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("inelastic-c2/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-c2/component-m5", "")
except: pass

try: pcglabels.add_edge(("inelastic-c2/inelastic-m2", "component-c2/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-c1/open-m5", "")
except: pass
try: pcglabels.add_node("component-c2/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m5", "component-c2/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("lexicoconstructionalConditioning/constructionalConditioning", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("lexicoconstructionalConditioning/constructionalConditioning", "desmeme/desmeme"), label="CONDITIONING")
except: pass

try: pcglabels.add_node("component-c2/component-m5", "")
except: pass
try: pcglabels.add_node("inelastic-c2/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-c2/component-m5", "inelastic-c2/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("length/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count2-c1/count1-m1", "")
except: pass

try: pcglabels.add_edge(("length/inelastic-m1", "count2-c1/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("open-c1/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-c1/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-c1/open-m5", "coherent-c1/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("length/order", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "length/order"), label="STRICTURE")
except: pass

try: pcglabels.add_node("length/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count2-c1/count1-m2", "")
except: pass

try: pcglabels.add_edge(("length/inelastic-m2", "count2-c1/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("count2-c1/count5-m1", "")
except: pass
try: pcglabels.add_node("length/order", "")
except: pass

try: pcglabels.add_edge(("count2-c1/count5-m1", "length/order"), label="COUNT")
except: pass

try: pcglabels.add_node("count1-c1/count5-m1", "")
except: pass
try: pcglabels.add_node("inelastic-c1/order", "")
except: pass

try: pcglabels.add_edge(("count1-c1/count5-m1", "inelastic-c1/order"), label="COUNT")
except: pass

try: pcglabels.add_node("length/order", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("length/order", "desmeme/desmeme"), label="STRICTURE")
except: pass

try: ChechenPreverbalA.add_node("component-c1", "")
except: pass
try: ChechenPreverbalA.add_node("stable-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("component-c1", "stable-c1"), label=" STABILITY")
except: pass

try: ChechenPreverbalA.add_node("lexicoconstructionalConditioning", "")
except: pass
try: ChechenPreverbalA.add_node("medial", "")
except: pass

try: ChechenPreverbalA.add_edge(("lexicoconstructionalConditioning", "medial"), label=" FILLER_POSITION")
except: pass

try: ChechenPreverbalA.add_node("component-c1", "")
except: pass
try: ChechenPreverbalA.add_node("partiallyFilled-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("component-c1", "partiallyFilled-c1"), label=" FILLEDNESS")
except: pass

try: ChechenPreverbalA.add_node("component-c2", "")
except: pass
try: ChechenPreverbalA.add_node("stable-c2", "")
except: pass

try: ChechenPreverbalA.add_edge(("component-c2", "stable-c2"), label=" STABILITY")
except: pass

try: ChechenPreverbalA.add_node("length", "")
except: pass
try: ChechenPreverbalA.add_node("count2-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("length", "count2-c1"), label=" COUNT")
except: pass

try: ChechenPreverbalA.add_node("desmeme", "")
except: pass
try: ChechenPreverbalA.add_node("potentiallyViolable", "")
except: pass

try: ChechenPreverbalA.add_edge(("desmeme", "potentiallyViolable"), label=" VIOLABILITY")
except: pass

try: ChechenPreverbalA.add_node("length", "")
except: pass
try: ChechenPreverbalA.add_node("prosodicWord", "")
except: pass

try: ChechenPreverbalA.add_edge(("length", "prosodicWord"), label=" CONSTITUENT")
except: pass

try: ChechenPreverbalA.add_node("desmeme", "")
except: pass
try: ChechenPreverbalA.add_node("lexicoconstructionalConditioning", "")
except: pass

try: ChechenPreverbalA.add_edge(("desmeme", "lexicoconstructionalConditioning"), label=" CONDITIONING")
except: pass

try: ChechenPreverbalA.add_node("desmeme", "")
except: pass
try: ChechenPreverbalA.add_node("length", "")
except: pass

try: ChechenPreverbalA.add_edge(("desmeme", "length"), label=" STRICTURE")
except: pass

try: ChechenPreverbalA.add_node("potentiallyViolable", "")
except: pass
try: ChechenPreverbalA.add_node("morphosyntacticInsertion", "")
except: pass

try: ChechenPreverbalA.add_edge(("potentiallyViolable", "morphosyntacticInsertion"), label=" REPARABILITY")
except: pass

try: ChechenPreverbalA.add_node("open-c1", "")
except: pass
try: ChechenPreverbalA.add_node("coherent-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("open-c1", "coherent-c1"), label=" COHERENCE")
except: pass

try: ChechenPreverbalA.add_node("component-c2", "")
except: pass
try: ChechenPreverbalA.add_node("inelastic-c2", "")
except: pass

try: ChechenPreverbalA.add_edge(("component-c2", "inelastic-c2"), label=" ELASTICITY")
except: pass

try: ChechenPreverbalA.add_node("inelastic-c1", "")
except: pass
try: ChechenPreverbalA.add_node("count1-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("inelastic-c1", "count1-c1"), label=" COUNT")
except: pass

try: ChechenPreverbalA.add_node("desmeme", "")
except: pass
try: ChechenPreverbalA.add_node("span", "")
except: pass

try: ChechenPreverbalA.add_edge(("desmeme", "span"), label=" FOUNDATION")
except: pass

try: ChechenPreverbalA.add_node("partiallyFilled-c1", "")
except: pass
try: ChechenPreverbalA.add_node("incoherent-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("partiallyFilled-c1", "incoherent-c1"), label=" COHERENCE")
except: pass

try: ChechenPreverbalA.add_node("span", "")
except: pass
try: ChechenPreverbalA.add_node("component-c2", "")
except: pass

try: ChechenPreverbalA.add_edge(("span", "component-c2"), label=" RIGHT_SUPPORT")
except: pass

try: ChechenPreverbalA.add_node("filledComponentSet", "")
except: pass
try: ChechenPreverbalA.add_node("component-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("filledComponentSet", "component-c1"), label=" FILLED_COMPONENT")
except: pass

try: ChechenPreverbalA.add_node("inelastic-c2", "")
except: pass
try: ChechenPreverbalA.add_node("count1-c2", "")
except: pass

try: ChechenPreverbalA.add_edge(("inelastic-c2", "count1-c2"), label=" COUNT")
except: pass

try: ChechenPreverbalA.add_node("component-c2", "")
except: pass
try: ChechenPreverbalA.add_node("open-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("component-c2", "open-c1"), label=" FILLEDNESS")
except: pass

try: ChechenPreverbalA.add_node("partiallyFilled-c1", "")
except: pass
try: ChechenPreverbalA.add_node("final-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("partiallyFilled-c1", "final-c1"), label=" FILLER_PLACEMENT")
except: pass

try: ChechenPreverbalA.add_node("span", "")
except: pass
try: ChechenPreverbalA.add_node("component-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("span", "component-c1"), label=" LEFT_SUPPORT")
except: pass

try: ChechenPreverbalA.add_node("potentiallyViolable", "")
except: pass
try: ChechenPreverbalA.add_node("noKnownExceptions", "")
except: pass

try: ChechenPreverbalA.add_edge(("potentiallyViolable", "noKnownExceptions"), label=" EXCEPTIONALITY")
except: pass

try: ChechenPreverbalA.add_node("lexicoconstructionalConditioning", "")
except: pass
try: ChechenPreverbalA.add_node("filledComponentSet", "")
except: pass

try: ChechenPreverbalA.add_edge(("lexicoconstructionalConditioning", "filledComponentSet"), label=" FILLED_COMPONENTS")
except: pass

try: ChechenPreverbalA.add_node("partiallyFilled-c1", "")
except: pass
try: ChechenPreverbalA.add_node("canonicalLineate-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("partiallyFilled-c1", "canonicalLineate-c1"), label=" FORM")
except: pass

try: ChechenPreverbalA.add_node("component-c1", "")
except: pass
try: ChechenPreverbalA.add_node("inelastic-c1", "")
except: pass

try: ChechenPreverbalA.add_edge(("component-c1", "inelastic-c1"), label=" ELASTICITY")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m5", "")
except: pass

try: MandeClause.add_edge(("arch", "component-m5"), label=" KEYSTONE")
except: pass

try: MandeClause.add_node("component-m4", "")
except: pass
try: MandeClause.add_node("stable-m4", "")
except: pass

try: MandeClause.add_edge(("component-m4", "stable-m4"), label=" STABILITY")
except: pass

try: MandeClause.add_node("elastic-m2", "")
except: pass
try: MandeClause.add_node("minimum0-m2", "")
except: pass

try: MandeClause.add_edge(("elastic-m2", "minimum0-m2"), label=" MINIMUM")
except: pass

try: MandeClause.add_node("inelastic-m1", "")
except: pass
try: MandeClause.add_node("count1-m1", "")
except: pass

try: MandeClause.add_edge(("inelastic-m1", "count1-m1"), label=" COUNT")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m4", "")
except: pass

try: MandeClause.add_edge(("arch", "component-m4"), label=" RIGHT_SUPPORT")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m4", "")
except: pass

try: MandeClause.add_edge(("arch", "component-m4"), label=" RIGHT_VOUSSOIR")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m4", "")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m4", "")
except: pass

try: MandeClause.add_node("open-m2", "")
except: pass
try: MandeClause.add_node("coherent-m2", "")
except: pass

try: MandeClause.add_edge(("open-m2", "coherent-m2"), label=" COHERENCE")
except: pass

try: MandeClause.add_node("order", "")
except: pass
try: MandeClause.add_node("simple", "")
except: pass

try: MandeClause.add_edge(("order", "simple"), label=" RELATIONS")
except: pass

try: MandeClause.add_node("order", "")
except: pass
try: MandeClause.add_node("syntacticConstituent", "")
except: pass

try: MandeClause.add_edge(("order", "syntacticConstituent"), label=" CONSTITUENT")
except: pass

try: MandeClause.add_node("component-m2", "")
except: pass
try: MandeClause.add_node("stable-m2", "")
except: pass

try: MandeClause.add_edge(("component-m2", "stable-m2"), label=" STABILITY")
except: pass

try: MandeClause.add_node("component-m4", "")
except: pass
try: MandeClause.add_node("open-m4", "")
except: pass

try: MandeClause.add_edge(("component-m4", "open-m4"), label=" FILLEDNESS")
except: pass

try: MandeClause.add_node("component-m2", "")
except: pass
try: MandeClause.add_node("open-m2", "")
except: pass

try: MandeClause.add_edge(("component-m2", "open-m2"), label=" FILLEDNESS")
except: pass

try: MandeClause.add_node("component-m4", "")
except: pass
try: MandeClause.add_node("elastic-m3", "")
except: pass

try: MandeClause.add_edge(("component-m4", "elastic-m3"), label=" ELASTICITY")
except: pass

try: MandeClause.add_node("component-m3", "")
except: pass
try: MandeClause.add_node("stable-m3", "")
except: pass

try: MandeClause.add_edge(("component-m3", "stable-m3"), label=" STABILITY")
except: pass

try: MandeClause.add_node("elastic-m3", "")
except: pass
try: MandeClause.add_node("minimum0-m3", "")
except: pass

try: MandeClause.add_edge(("elastic-m3", "minimum0-m3"), label=" MINIMUM")
except: pass

try: MandeClause.add_node("desmeme", "")
except: pass
try: MandeClause.add_node("notViolable", "")
except: pass

try: MandeClause.add_edge(("desmeme", "notViolable"), label=" VIOLABILITY")
except: pass

try: MandeClause.add_node("component-m3", "")
except: pass
try: MandeClause.add_node("elastic-m2", "")
except: pass

try: MandeClause.add_edge(("component-m3", "elastic-m2"), label=" ELASTICITY")
except: pass

try: MandeClause.add_node("elastic-m1", "")
except: pass
try: MandeClause.add_node("minimum0-m1", "")
except: pass

try: MandeClause.add_edge(("elastic-m1", "minimum0-m1"), label=" MINIMUM")
except: pass

try: MandeClause.add_node("open-m3", "")
except: pass
try: MandeClause.add_node("coherent-m3", "")
except: pass

try: MandeClause.add_edge(("open-m3", "coherent-m3"), label=" COHERENCE")
except: pass

try: MandeClause.add_node("component-m1", "")
except: pass
try: MandeClause.add_node("stable-m1", "")
except: pass

try: MandeClause.add_edge(("component-m1", "stable-m1"), label=" STABILITY")
except: pass

try: MandeClause.add_node("open-m4", "")
except: pass
try: MandeClause.add_node("incoherent-m1", "")
except: pass

try: MandeClause.add_edge(("open-m4", "incoherent-m1"), label=" COHERENCE")
except: pass

try: MandeClause.add_node("inelastic-m2", "")
except: pass
try: MandeClause.add_node("count1-m2", "")
except: pass

try: MandeClause.add_edge(("inelastic-m2", "count1-m2"), label=" COUNT")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("restkomponentenSet", "")
except: pass

try: MandeClause.add_edge(("arch", "restkomponentenSet"), label=" RESTKOMPONENTEN")
except: pass

try: MandeClause.add_node("elastic-m2", "")
except: pass
try: MandeClause.add_node("maximum1-m2", "")
except: pass

try: MandeClause.add_edge(("elastic-m2", "maximum1-m2"), label=" maximum")
except: pass

try: MandeClause.add_node("desmeme", "")
except: pass
try: MandeClause.add_node("order", "")
except: pass

try: MandeClause.add_edge(("desmeme", "order"), label=" STRICTURE")
except: pass

try: MandeClause.add_node("component-m2", "")
except: pass
try: MandeClause.add_node("elastic-m1", "")
except: pass

try: MandeClause.add_edge(("component-m2", "elastic-m1"), label=" ELASTICITY")
except: pass

try: MandeClause.add_node("component-m3", "")
except: pass
try: MandeClause.add_node("open-m3", "")
except: pass

try: MandeClause.add_edge(("component-m3", "open-m3"), label=" FILLEDNESS")
except: pass

try: MandeClause.add_node("elastic-m3", "")
except: pass
try: MandeClause.add_node("maximum100-m1", "")
except: pass

try: MandeClause.add_edge(("elastic-m3", "maximum100-m1"), label=" maximum")
except: pass

try: MandeClause.add_node("component-m1", "")
except: pass
try: MandeClause.add_node("inelastic-m1", "")
except: pass

try: MandeClause.add_edge(("component-m1", "inelastic-m1"), label=" ELASTICITY")
except: pass

try: MandeClause.add_node("desmeme", "")
except: pass
try: MandeClause.add_node("constructionalConditioning", "")
except: pass

try: MandeClause.add_edge(("desmeme", "constructionalConditioning"), label=" CONDITIONING")
except: pass

try: MandeClause.add_node("component-m5", "")
except: pass
try: MandeClause.add_node("open-m5", "")
except: pass

try: MandeClause.add_edge(("component-m5", "open-m5"), label=" FILLEDNESS")
except: pass

try: MandeClause.add_node("order", "")
except: pass
try: MandeClause.add_node("count5-m1", "")
except: pass

try: MandeClause.add_edge(("order", "count5-m1"), label=" COUNT")
except: pass

try: MandeClause.add_node("open-m1", "")
except: pass
try: MandeClause.add_node("coherent-m1", "")
except: pass

try: MandeClause.add_edge(("open-m1", "coherent-m1"), label=" COHERENCE")
except: pass

try: MandeClause.add_node("restkomponentenSet", "")
except: pass
try: MandeClause.add_node("component-m2", "")
except: pass

try: MandeClause.add_edge(("restkomponentenSet", "component-m2"), label=" RESTKOMPONENT")
except: pass

try: MandeClause.add_node("elastic-m1", "")
except: pass
try: MandeClause.add_node("maximum1-m1", "")
except: pass

try: MandeClause.add_edge(("elastic-m1", "maximum1-m1"), label=" MAXIMUM")
except: pass

try: MandeClause.add_node("component-m5", "")
except: pass
try: MandeClause.add_node("stable-m5", "")
except: pass

try: MandeClause.add_edge(("component-m5", "stable-m5"), label=" STABILITY")
except: pass

try: MandeClause.add_node("component-m1", "")
except: pass
try: MandeClause.add_node("open-m1", "")
except: pass

try: MandeClause.add_edge(("component-m1", "open-m1"), label=" FILLEDNESS")
except: pass

try: MandeClause.add_node("desmeme", "")
except: pass
try: MandeClause.add_node("arch", "")
except: pass

try: MandeClause.add_edge(("desmeme", "arch"), label=" FOUNDATION")
except: pass

try: MandeClause.add_node("component-m5", "")
except: pass
try: MandeClause.add_node("inelastic-m2", "")
except: pass

try: MandeClause.add_edge(("component-m5", "inelastic-m2"), label=" ELASTICITY")
except: pass

try: MandeClause.add_node("open-m5", "")
except: pass
try: MandeClause.add_node("coherent-m4", "")
except: pass

try: MandeClause.add_edge(("open-m5", "coherent-m4"), label=" COHERENCE")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m3", "")
except: pass

try: MandeClause.add_edge(("arch", "component-m3"), label=" LEFT_VOUSSOIR")
except: pass

try: MandeClause.add_node("arch", "")
except: pass
try: MandeClause.add_node("component-m1", "")
except: pass

try: MandeClause.add_edge(("arch", "component-m1"), label=" LEFT_SUPPORT")
except: pass

# To self: I spent a long time working out why .dot files had attributes
# such as width and pos that I didn't have in my representation.
# This "write_dot" function is a special pydot feature that doesn't
# exist as an actual method but is, rather, generated automatically based on the extension (sort of).
# The internal representation is passed through the dot program and the output adds these extra features.
# This seems to be the same as the "default" ones if they aren't added.
# I looked into this to see how I should be customizing node placement.
# I guess I'd have to delve deep into dot to find out at this point.
# See comparison method in tdag for where this write_dot function is called.
pcgfolder = "/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/PCGs/"
draw_graphs([pcgweighted, pcglabels, ChechenPreverbalA, MandeClause], pcgfolder)
