from pygraph.classes.digraph import digraph
from pygraph.readwrite.markup import write
import pydot
import tdag
from tdag import draw_graphs

pcgweighted = tdag.tdag("AghemMande-weighted")
pcglabels = tdag.tdag("AghemMande-labels")
AghemClause = tdag.tdag("AghemClause")
MandeClause = tdag.tdag("MandeClause")

try: pcgweighted.add_node("open-a1/open-m4", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m4", "component-a1/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a6/component-m5", "")
except: pass
try: pcgweighted.add_node("elastic-a3/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m5", "elastic-a3/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a3/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-a3/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m5", "coherent-a3/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a2/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count1-a2/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/inelastic-m2", "count1-a2/count1-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a3/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-a3/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m1", "stable-a3/stable-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "arch/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-a3/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m3", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/elastic-m2", "component-a5/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m2", "")
except: pass
try: pcgweighted.add_node("minimum0-a1/minimum0-m2", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m2", "minimum0-a1/minimum0-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a1/component-m4", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m4", "inelastic-a1/elastic-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m1", "component-a2/component-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("order/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count6-a1/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("order/inelastic-m2", "count6-a1/count1-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a2/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-a2/stable-m5", "component-a2/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a4/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-a4/coherent-m2", "open-a4/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a1/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-a1/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m4", "stable-a1/stable-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m3", "component-a2/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m2", "")
except: pass
try: pcgweighted.add_node("unstable-a1/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m2", "unstable-a1/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a2/open-m5", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m5", "component-a2/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("count6-a1/count1-m1", "")
except: pass
try: pcgweighted.add_node("order/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count6-a1/count1-m1", "order/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a5/open-m2", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m2", "component-a5/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m2", "component-a3/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m2", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m1", "component-a6/component-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("syntacticConstituent/syntacticConstituent", "")
except: pass
try: pcgweighted.add_node("order/order", "")
except: pass

try: pcgweighted.add_edge(("syntacticConstituent/syntacticConstituent", "order/order"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-a3/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m3", "stable-a3/stable-m3"), label=" 0.25")
except: pass

try: pcgweighted.add_node("count1-a2/count5-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/order", "")
except: pass

try: pcgweighted.add_edge(("count1-a2/count5-m1", "inelastic-a2/order"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a1/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-a1/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m3", "coherent-a1/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a2/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/inelastic-m1", "component-a3/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a1/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-a1/incoherent-m1", "open-a1/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a1/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-a1/stable-m3", "component-a1/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m2", "")
except: pass
try: pcgweighted.add_node("minimum0-a3/minimum0-m2", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m2", "minimum0-a3/minimum0-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m1", "")
except: pass
try: pcgweighted.add_node("unstable-a1/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m1", "unstable-a1/stable-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a2/component-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a1/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m1", "elastic-a1/inelastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("stable-a5/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-a5/stable-m2", "component-a6/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a4/open-m5", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m5", "component-a4/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a1/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/elastic-m1", "component-a1/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("minimum0-a1/minimum0-m3", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a1/minimum0-m3", "elastic-a1/elastic-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("count1-a1/count1-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count1-a1/count1-m2", "inelastic-a1/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-a1/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count1-a1/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/inelastic-m1", "count1-a1/count1-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("potentiallyViolable/notViolable", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("potentiallyViolable/notViolable", "desmeme/desmeme"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m5", "inelastic-a3/inelastic-m2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-a3/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m4", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/elastic-m3", "component-a5/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a4/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-a4/stable-m2", "component-a5/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a1/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-a1/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m3", "stable-a1/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a3/open-m1", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m1", "component-a3/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a1/open-m1", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m1", "component-a1/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a5/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-a5/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m4", "coherent-a5/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a3/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-a3/coherent-m3", "open-a3/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a2/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-a2/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m1", "stable-a2/stable-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("stable-a4/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-a4/stable-m3", "component-a5/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-a5/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m3", "stable-a5/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a3/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-a3/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m5", "stable-a3/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a2/component-m1", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m1", "open-a2/open-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m1", "")
except: pass
try: pcgweighted.add_node("maximum1-a1/maximum1-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m1", "maximum1-a1/maximum1-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a3/open-m2", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m2", "component-a3/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a1/component-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m2", "inelastic-a1/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a6/open-m2", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m2", "component-a6/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a2/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/inelastic-m1", "component-a4/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a5/component-m1", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m1", "open-a5/open-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a3/component-m2", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m2", "elastic-a2/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-a5/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-a5/coherent-m1", "open-a5/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m3", "open-a3/open-m3"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a1/component-m2", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m2", "open-a1/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m1", "")
except: pass
try: pcgweighted.add_node("minimum0-a1/minimum0-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m1", "minimum0-a1/minimum0-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a1/open-m3", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m3", "component-a1/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a5/open-m3", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m3", "component-a5/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a2/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-a2/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m4", "stable-a2/stable-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-a2/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-a2/coherent-m4", "open-a2/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a4/component-m2", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m2", "open-a4/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "component-a1/component-m1"), label=" 0.14")
except: pass

try: pcgweighted.add_node("elastic-a2/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m5", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/inelastic-m2", "component-a3/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("constructionalConditioning/constructionalConditioning", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "constructionalConditioning/constructionalConditioning"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open-a4/open-m1", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m1", "component-a4/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m3", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m3", "open-a4/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-a2/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/elastic-m3", "component-a4/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("order/order", "")
except: pass
try: pcgweighted.add_node("simple/simple", "")
except: pass

try: pcgweighted.add_edge(("order/order", "simple/simple"), label=" 0.25")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "component-a3/component-m3"), label=" 0.14")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m3", "component-a6/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a2/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m5", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/inelastic-m2", "component-a4/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a3/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-a3/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m4", "coherent-a3/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-a1/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-a1/stable-m4", "component-a1/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("order/order", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("order/order", "desmeme/desmeme"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-a1/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m3", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/elastic-m2", "component-a1/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a5/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-a5/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m2", "coherent-a5/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-a1/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-a1/stable-m5", "component-a1/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "desmeme/desmeme"), label=" 0.14")
except: pass

try: pcgweighted.add_node("component-a5/component-m3", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m3", "open-a5/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a5/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-a4/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m4", "stable-a4/stable-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a2/component-m5", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m5", "open-a2/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a5/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-a4/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m1", "stable-a4/stable-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a5/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-a4/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m2", "stable-a4/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-a1/order", "")
except: pass
try: pcgweighted.add_node("count1-a1/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/order", "count1-a1/count5-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m3", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m2", "component-a2/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-a2/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m2", "stable-a2/stable-m2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("coherent-a1/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-a1/coherent-m2", "open-a1/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("minimum0-a3/minimum0-m2", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a3/minimum0-m2", "elastic-a3/elastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("minimum0-a1/minimum0-m2", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a1/minimum0-m2", "elastic-a1/elastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a3/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-a3/stable-m2", "component-a3/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("minimum0-a3/minimum0-m3", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a3/minimum0-m3", "elastic-a3/elastic-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a4/component-m5", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m5", "open-a4/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("maximum100-a2/maximum1-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("maximum100-a2/maximum1-m1", "elastic-a3/elastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a1/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-a1/coherent-m1", "open-a1/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a6/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-a6/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m5", "coherent-a6/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("count1-a2/count1-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count1-a2/count1-m2", "inelastic-a2/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("minimum0-a2/minimum0-m3", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a2/minimum0-m3", "elastic-a2/elastic-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("count6-a1/count5-m1", "")
except: pass
try: pcgweighted.add_node("order/order", "")
except: pass

try: pcgweighted.add_edge(("count6-a1/count5-m1", "order/order"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a5/component-m2", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m2", "open-a5/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("count1-a1/count1-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count1-a1/count1-m1", "inelastic-a1/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-a5/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m4", "stable-a5/stable-m4"), label=" 0.25")
except: pass

try: pcgweighted.add_node("unstable-a1/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m2", "")
except: pass

try: pcgweighted.add_edge(("unstable-a1/stable-m2", "component-a4/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("elastic-a3/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/inelastic-m1", "component-a6/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a5/component-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m2", "inelastic-a3/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("constructionalConditioning/constructionalConditioning", "")
except: pass
try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass

try: pcgweighted.add_edge(("constructionalConditioning/constructionalConditioning", "desmeme/desmeme"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a1/component-m5", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m5", "inelastic-a1/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m3", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m2", "component-a6/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a2/component-m5", "")
except: pass
try: pcgweighted.add_node("elastic-a1/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m5", "elastic-a1/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "component-a4/component-m4"), label=" 0.14")
except: pass

try: pcgweighted.add_node("open-a2/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-a2/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m3", "coherent-a2/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("unstable-a1/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m3", "")
except: pass

try: pcgweighted.add_edge(("unstable-a1/stable-m3", "component-a4/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-a2/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/elastic-m1", "component-a4/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a6/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-a6/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m4", "coherent-a6/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-a2/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-a2/stable-m1", "component-a2/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a2/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-a2/coherent-m2", "open-a2/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m1", "")
except: pass
try: pcgweighted.add_node("maximum100-a2/maximum1-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m1", "maximum100-a2/maximum1-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a5/component-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m1", "inelastic-a3/inelastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m1", "arch/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a3/component-m4", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m4", "open-a3/open-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m1", "")
except: pass
try: pcgweighted.add_node("minimum0-a3/minimum0-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m1", "minimum0-a3/minimum0-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a6/component-m2", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m2", "open-a6/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a1/elastic-m3", "")
except: pass
try: pcgweighted.add_node("minimum0-a1/minimum0-m3", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/elastic-m3", "minimum0-a1/minimum0-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a2/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-a2/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m4", "coherent-a2/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m5", "")
except: pass
try: pcgweighted.add_node("unstable-a1/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m5", "unstable-a1/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m2", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m1", "component-a3/component-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a5/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-a5/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m5", "coherent-a5/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("restkomponentenSet/restkomponentenSet", "component-a2/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("count1-a3/count1-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count1-a3/count1-m1", "inelastic-a3/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a2/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-a2/coherent-m1", "open-a2/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a2/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-a2/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m2", "coherent-a2/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a4/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-a4/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m1", "coherent-a4/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a5/open-m4", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m4", "component-a5/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("stable-a5/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-a5/stable-m1", "component-a6/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a2/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-a2/stable-m3", "component-a2/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a1/component-m5", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m5", "open-a1/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a6/open-m5", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m5", "component-a6/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a5/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-a5/incoherent-m1", "open-a5/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a6/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-a6/coherent-m2", "open-a6/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a3/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-a3/stable-m4", "component-a3/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a4/component-m1", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m1", "open-a4/open-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a4/component-m5", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m5", "inelastic-a2/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a3/component-m5", "")
except: pass
try: pcgweighted.add_node("elastic-a2/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m5", "elastic-a2/inelastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m4", "inelastic-a2/elastic-m3"), label=" 0.25")
except: pass

try: pcgweighted.add_node("stable-a2/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-a2/stable-m4", "component-a2/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a2/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-a2/incoherent-m1", "open-a2/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "component-a5/component-m5"), label=" 0.14")
except: pass

try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m4", "elastic-a3/elastic-m3"), label=" 0.25")
except: pass

try: pcgweighted.add_node("stable-a5/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-a5/stable-m5", "component-a6/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("restkomponentenSet/restkomponentenSet", "arch/arch"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a2/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count1-a2/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/inelastic-m1", "count1-a2/count1-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a2/elastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m3", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/elastic-m2", "component-a4/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a1/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-a1/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m5", "coherent-a1/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a6/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-a6/coherent-m1", "open-a6/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a2/open-m1", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m1", "component-a2/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a3/component-m5", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m5", "open-a3/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a2/open-m3", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m3", "component-a2/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a3/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-a3/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m2", "stable-a3/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m1", "inelastic-a1/inelastic-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open-a1/open-m2", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m2", "component-a1/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m2", "inelastic-a2/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m4", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m3", "component-a3/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a3/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-a3/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m3", "coherent-a3/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a4/open-m3", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m3", "component-a4/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a1/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-a1/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m2", "stable-a1/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a1/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-a1/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m2", "coherent-a1/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("count1-a2/count1-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("count1-a2/count1-m1", "inelastic-a2/inelastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m4", "arch/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a1/component-m3", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m3", "inelastic-a1/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("minimum0-a2/minimum0-m2", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a2/minimum0-m2", "elastic-a2/elastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a2/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-a2/stable-m2", "component-a2/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a4/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-a4/stable-m5", "component-a5/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a6/open-m3", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m3", "component-a6/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a6/component-m1", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m1", "open-a6/open-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-a5/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-a5/coherent-m4", "open-a5/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-a3/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count1-a3/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/inelastic-m2", "count1-a3/count1-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a1/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-a1/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m1", "coherent-a1/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m3", "")
except: pass
try: pcgweighted.add_node("minimum0-a2/minimum0-m3", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m3", "minimum0-a2/minimum0-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a3/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-a3/coherent-m1", "open-a3/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a4/open-m4", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m4", "component-a4/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a3/elastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/elastic-m1", "component-a5/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a1/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-a1/stable-m1", "component-a1/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a3/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m5", "")
except: pass

try: pcgweighted.add_edge(("stable-a3/stable-m5", "component-a3/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a6/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-a6/incoherent-m1", "open-a6/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m1", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m1", "open-a3/open-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("count1-a3/count5-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/order", "")
except: pass

try: pcgweighted.add_edge(("count1-a3/count5-m1", "inelastic-a3/order"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a3/open-m4", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m4", "component-a3/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a2/component-m3", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m3", "elastic-a1/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a5/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-a5/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m1", "coherent-a5/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("order/order", "")
except: pass
try: pcgweighted.add_node("count6-a1/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("order/order", "count6-a1/count5-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("stable-a4/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-a4/stable-m1", "component-a5/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m4", "")
except: pass
try: pcgweighted.add_node("stable-a3/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m4", "stable-a3/stable-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-a5/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-a5/coherent-m2", "open-a5/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a2/open-m2", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m2", "component-a2/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a1/elastic-m3", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m4", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/elastic-m3", "component-a1/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "component-a6/component-m4"), label=" 0.14")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m1", "")
except: pass
try: pcgweighted.add_node("maximum100-a1/maximum1-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m1", "maximum100-a1/maximum1-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-a3/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count1-a3/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/inelastic-m1", "count1-a3/count1-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m1", "")
except: pass
try: pcgweighted.add_node("minimum0-a2/minimum0-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m1", "minimum0-a2/minimum0-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a6/open-m4", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m4", "component-a6/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m3", "")
except: pass
try: pcgweighted.add_node("unstable-a1/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m3", "unstable-a1/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a6/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-a6/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m2", "coherent-a6/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("inelastic-a3/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/inelastic-m1", "component-a5/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a3/elastic-m3", "")
except: pass
try: pcgweighted.add_node("minimum0-a3/minimum0-m3", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/elastic-m3", "minimum0-a3/minimum0-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m5", "open-a5/open-m5"), label=" 0.25")
except: pass

try: pcgweighted.add_node("stable-a1/stable-m2", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m2", "")
except: pass

try: pcgweighted.add_edge(("stable-a1/stable-m2", "component-a1/component-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass
try: pcgweighted.add_node("unstable-a1/stable-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m4", "unstable-a1/stable-m4"), label=" 0.25")
except: pass

try: pcgweighted.add_node("maximum100-a1/maximum1-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("maximum100-a1/maximum1-m1", "elastic-a2/elastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("unstable-a1/stable-m5", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m5", "")
except: pass

try: pcgweighted.add_edge(("unstable-a1/stable-m5", "component-a4/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a5/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-a5/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m3", "coherent-a5/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a6/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-a6/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m3", "coherent-a6/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("count1-a3/count1-m2", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count1-a3/count1-m2", "inelastic-a3/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass
try: pcgweighted.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m2", "restkomponentenSet/restkomponentenSet"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a6/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-a5/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m5", "stable-a5/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a1/component-m4", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m4", "open-a1/open-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a2/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-a2/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m3", "stable-a2/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-a4/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-a4/incoherent-m1", "open-a4/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a4/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-a4/coherent-m3", "open-a4/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a3/coherent-m2", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m2", "")
except: pass

try: pcgweighted.add_edge(("coherent-a3/coherent-m2", "open-a3/open-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a5/component-m4", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m4", "open-a5/open-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("stable-a3/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-a3/stable-m3", "component-a3/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-a5/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m1", "stable-a5/stable-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a4/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-a4/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m5", "coherent-a4/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("minimum0-a3/minimum0-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a3/minimum0-m1", "elastic-a3/elastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a2/component-m3", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m3", "open-a2/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("elastic-a3/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m5", "")
except: pass

try: pcgweighted.add_edge(("elastic-a3/inelastic-m2", "component-a6/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-a3/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/inelastic-m2", "component-a5/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m5", "arch/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-a3/order", "")
except: pass
try: pcgweighted.add_node("count1-a3/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a3/order", "count1-a3/count5-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m4", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m4", "elastic-a2/elastic-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("unstable-a1/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m1", "")
except: pass

try: pcgweighted.add_edge(("unstable-a1/stable-m1", "component-a4/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m3", "arch/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic-a1/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("count1-a1/count1-m2", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/inelastic-m2", "count1-a1/count1-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a5/open-m1", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m1", "component-a5/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a6/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-a6/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m1", "coherent-a6/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a4/coherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m1", "")
except: pass

try: pcgweighted.add_edge(("coherent-a4/coherent-m1", "open-a4/open-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a1/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-a1/coherent-m4", "open-a1/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("arch/arch", "")
except: pass
try: pcgweighted.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass

try: pcgweighted.add_edge(("arch/arch", "restkomponentenSet/restkomponentenSet"), label=" 0.14")
except: pass

try: pcgweighted.add_node("elastic-a2/elastic-m2", "")
except: pass
try: pcgweighted.add_node("minimum0-a2/minimum0-m2", "")
except: pass

try: pcgweighted.add_edge(("elastic-a2/elastic-m2", "minimum0-a2/minimum0-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a3/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-a3/coherent-m4", "open-a3/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-a2/order", "")
except: pass
try: pcgweighted.add_node("count1-a2/count5-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a2/order", "count1-a2/count5-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a2/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-a2/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m5", "stable-a2/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("order/order", "")
except: pass
try: pcgweighted.add_node("syntacticConstituent/syntacticConstituent", "")
except: pass

try: pcgweighted.add_edge(("order/order", "syntacticConstituent/syntacticConstituent"), label=" 0.25")
except: pass

try: pcgweighted.add_node("unstable-a1/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass

try: pcgweighted.add_edge(("unstable-a1/stable-m4", "component-a4/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m5", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m5", "open-a6/open-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("stable-a3/stable-m1", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m1", "")
except: pass

try: pcgweighted.add_edge(("stable-a3/stable-m1", "component-a3/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a6/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-a6/coherent-m3", "open-a6/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a2/open-m4", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m4", "component-a2/component-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m1", "inelastic-a2/inelastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a3/open-m5", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m5", "component-a3/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a1/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-a1/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m4", "coherent-a1/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a1/open-m5", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-a1/open-m5", "component-a1/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a6/open-m1", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a6/open-m1", "component-a6/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a2/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-a2/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m1", "coherent-a2/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a4/component-m3", "")
except: pass
try: pcgweighted.add_node("inelastic-a2/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m3", "inelastic-a2/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a6/component-m2", "")
except: pass
try: pcgweighted.add_node("stable-a5/stable-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m2", "stable-a5/stable-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a4/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-a4/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m2", "coherent-a4/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a5/open-m5", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass

try: pcgweighted.add_edge(("open-a5/open-m5", "component-a5/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a2/component-m4", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m4", "elastic-a1/elastic-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a5/component-m4", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/elastic-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m4", "inelastic-a3/elastic-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("inelastic-a1/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/inelastic-m1", "component-a1/component-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a1/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-a1/coherent-m3", "open-a1/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m2", "elastic-a1/elastic-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open-a3/open-m1", "")
except: pass
try: pcgweighted.add_node("coherent-a3/coherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m1", "coherent-a3/coherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("open-a2/open-m5", "")
except: pass
try: pcgweighted.add_node("coherent-a2/coherent-m4", "")
except: pass

try: pcgweighted.add_edge(("open-a2/open-m5", "coherent-a2/coherent-m4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a5/component-m3", "")
except: pass
try: pcgweighted.add_node("inelastic-a3/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m3", "inelastic-a3/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a2/component-m4", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m4", "open-a2/open-m4"), label=" 0.33")
except: pass

try: pcgweighted.add_node("order/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("count6-a1/count1-m1", "")
except: pass

try: pcgweighted.add_edge(("order/inelastic-m1", "count6-a1/count1-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m3", "elastic-a2/elastic-m2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open-a3/open-m3", "")
except: pass
try: pcgweighted.add_node("component-a3/component-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m3", "component-a3/component-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m1", "open-a1/open-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open-a4/open-m3", "")
except: pass
try: pcgweighted.add_node("coherent-a4/coherent-m3", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m3", "coherent-a4/coherent-m3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a3/component-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a2/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m1", "elastic-a2/inelastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("potentiallyViolable/notViolable", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "potentiallyViolable/notViolable"), label=" 0.25")
except: pass

try: pcgweighted.add_node("coherent-a5/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-a5/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-a5/coherent-m3", "open-a5/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("count1-a1/count5-m1", "")
except: pass
try: pcgweighted.add_node("inelastic-a1/order", "")
except: pass

try: pcgweighted.add_edge(("count1-a1/count5-m1", "inelastic-a1/order"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m3", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m3", "elastic-a3/elastic-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a3/component-m2", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a3/component-m2", "open-a3/open-m2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a4/component-m4", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a4/component-m4", "open-a4/open-m4"), label=" 0.25")
except: pass

try: pcgweighted.add_node("coherent-a2/coherent-m3", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m3", "")
except: pass

try: pcgweighted.add_edge(("coherent-a2/coherent-m3", "open-a2/open-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a1/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-a1/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m5", "stable-a1/stable-m5"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a4/open-m4", "")
except: pass
try: pcgweighted.add_node("coherent-a4/incoherent-m1", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m4", "coherent-a4/incoherent-m1"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a1/inelastic-m1", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m1", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/inelastic-m1", "component-a2/component-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a5/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-a5/stable-m4", "component-a6/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("open-a3/open-m2", "")
except: pass
try: pcgweighted.add_node("coherent-a3/coherent-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a3/open-m2", "coherent-a3/coherent-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component-a6/component-m3", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m3", "open-a6/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("coherent-a3/incoherent-m1", "")
except: pass
try: pcgweighted.add_node("open-a3/open-m4", "")
except: pass

try: pcgweighted.add_edge(("coherent-a3/incoherent-m1", "open-a3/open-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a1/component-m3", "")
except: pass
try: pcgweighted.add_node("open-a1/open-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m3", "open-a1/open-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open-a4/open-m2", "")
except: pass
try: pcgweighted.add_node("component-a4/component-m2", "")
except: pass

try: pcgweighted.add_edge(("open-a4/open-m2", "component-a4/component-m2"), label=" 0.5")
except: pass

try: pcgweighted.add_node("elastic-a1/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a2/component-m5", "")
except: pass

try: pcgweighted.add_edge(("elastic-a1/inelastic-m2", "component-a2/component-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a4/stable-m4", "")
except: pass
try: pcgweighted.add_node("component-a5/component-m4", "")
except: pass

try: pcgweighted.add_edge(("stable-a4/stable-m4", "component-a5/component-m4"), label=" 1")
except: pass

try: pcgweighted.add_node("coherent-a6/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-a6/coherent-m4", "open-a6/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("stable-a5/stable-m3", "")
except: pass
try: pcgweighted.add_node("component-a6/component-m3", "")
except: pass

try: pcgweighted.add_edge(("stable-a5/stable-m3", "component-a6/component-m3"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic-a1/inelastic-m2", "")
except: pass
try: pcgweighted.add_node("component-a1/component-m5", "")
except: pass

try: pcgweighted.add_edge(("inelastic-a1/inelastic-m2", "component-a1/component-m5"), label=" 0.5")
except: pass

try: pcgweighted.add_node("coherent-a4/coherent-m4", "")
except: pass
try: pcgweighted.add_node("open-a4/open-m5", "")
except: pass

try: pcgweighted.add_edge(("coherent-a4/coherent-m4", "open-a4/open-m5"), label=" 1")
except: pass

try: pcgweighted.add_node("minimum0-a1/minimum0-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a1/minimum0-m1", "elastic-a1/elastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("count6-a1/count1-m2", "")
except: pass
try: pcgweighted.add_node("order/inelastic-m2", "")
except: pass

try: pcgweighted.add_edge(("count6-a1/count1-m2", "order/inelastic-m2"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass
try: pcgweighted.add_node("arch/arch", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m4", "arch/arch"), label=" 0.25")
except: pass

try: pcgweighted.add_node("maximum1-a1/maximum1-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a1/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("maximum1-a1/maximum1-m1", "elastic-a1/elastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a5/component-m3", "")
except: pass
try: pcgweighted.add_node("stable-a4/stable-m3", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m3", "stable-a4/stable-m3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("minimum0-a2/minimum0-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a2/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("minimum0-a2/minimum0-m1", "elastic-a2/elastic-m1"), label=" 1")
except: pass

try: pcgweighted.add_node("simple/simple", "")
except: pass
try: pcgweighted.add_node("order/order", "")
except: pass

try: pcgweighted.add_edge(("simple/simple", "order/order"), label=" 1")
except: pass

try: pcgweighted.add_node("component-a6/component-m4", "")
except: pass
try: pcgweighted.add_node("open-a6/open-m4", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m4", "open-a6/open-m4"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a6/component-m1", "")
except: pass
try: pcgweighted.add_node("elastic-a3/inelastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m1", "elastic-a3/inelastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("desmeme/desmeme", "")
except: pass
try: pcgweighted.add_node("order/order", "")
except: pass

try: pcgweighted.add_edge(("desmeme/desmeme", "order/order"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a6/component-m2", "")
except: pass
try: pcgweighted.add_node("elastic-a3/elastic-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a6/component-m2", "elastic-a3/elastic-m1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component-a2/component-m2", "")
except: pass
try: pcgweighted.add_node("open-a2/open-m2", "")
except: pass

try: pcgweighted.add_edge(("component-a2/component-m2", "open-a2/open-m2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a1/component-m1", "")
except: pass
try: pcgweighted.add_node("stable-a1/stable-m1", "")
except: pass

try: pcgweighted.add_edge(("component-a1/component-m1", "stable-a1/stable-m1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component-a5/component-m5", "")
except: pass
try: pcgweighted.add_node("stable-a4/stable-m5", "")
except: pass

try: pcgweighted.add_edge(("component-a5/component-m5", "stable-a4/stable-m5"), label=" 0.25")
except: pass

try: pcglabels.add_node("open-a1/open-m4", "")
except: pass
try: pcglabels.add_node("component-a1/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m4", "component-a1/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a6/component-m5", "")
except: pass
try: pcglabels.add_node("elastic-a3/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m5", "elastic-a3/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a3/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-a3/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m5", "coherent-a3/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("inelastic-a2/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count1-a2/count1-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/inelastic-m2", "count1-a2/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a3/component-m1", "")
except: pass
try: pcglabels.add_node("stable-a3/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m1", "stable-a3/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "arch/arch"), label="FOUNDATION")
except: pass

try: pcglabels.add_node("inelastic-a3/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-a5/component-m3", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/elastic-m2", "component-a5/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m2", "")
except: pass
try: pcglabels.add_node("minimum0-a1/minimum0-m2", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m2", "minimum0-a1/minimum0-m2"), label="MINIMUM")
except: pass

try: pcglabels.add_node("component-a1/component-m4", "")
except: pass
try: pcglabels.add_node("inelastic-a1/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m4", "inelastic-a1/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-a2/component-m2", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m1", "component-a2/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("order/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count6-a1/count1-m2", "")
except: pass

try: pcglabels.add_edge(("order/inelastic-m2", "count6-a1/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("stable-a2/stable-m5", "")
except: pass
try: pcglabels.add_node("component-a2/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-a2/stable-m5", "component-a2/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a4/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-a4/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-a4/coherent-m2", "open-a4/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a1/component-m4", "")
except: pass
try: pcglabels.add_node("stable-a1/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m4", "stable-a1/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-a2/component-m4", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m3", "component-a2/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a4/component-m2", "")
except: pass
try: pcglabels.add_node("unstable-a1/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m2", "unstable-a1/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a2/open-m5", "")
except: pass
try: pcglabels.add_node("component-a2/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m5", "component-a2/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count6-a1/count1-m1", "")
except: pass
try: pcglabels.add_node("order/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count6-a1/count1-m1", "order/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("open-a5/open-m2", "")
except: pass
try: pcglabels.add_node("component-a5/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m2", "component-a5/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-a3/component-m3", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m2", "component-a3/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-a6/component-m2", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m1", "component-a6/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("syntacticConstituent/syntacticConstituent", "")
except: pass
try: pcglabels.add_node("order/order", "")
except: pass

try: pcglabels.add_edge(("syntacticConstituent/syntacticConstituent", "order/order"), label="CONSTITUENT")
except: pass

try: pcglabels.add_node("component-a3/component-m3", "")
except: pass
try: pcglabels.add_node("stable-a3/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m3", "stable-a3/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("count1-a2/count5-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a2/order", "")
except: pass

try: pcglabels.add_edge(("count1-a2/count5-m1", "inelastic-a2/order"), label="COUNT")
except: pass

try: pcglabels.add_node("open-a1/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-a1/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m3", "coherent-a1/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("elastic-a2/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-a3/component-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/inelastic-m1", "component-a3/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("coherent-a1/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-a1/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-a1/incoherent-m1", "open-a1/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-a1/stable-m3", "")
except: pass
try: pcglabels.add_node("component-a1/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-a1/stable-m3", "component-a1/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m2", "")
except: pass
try: pcglabels.add_node("minimum0-a3/minimum0-m2", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m2", "minimum0-a3/minimum0-m2"), label="MINIMUM")
except: pass

try: pcglabels.add_node("component-a4/component-m1", "")
except: pass
try: pcglabels.add_node("unstable-a1/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m1", "unstable-a1/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a2/component-m1", "")
except: pass
try: pcglabels.add_node("elastic-a1/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m1", "elastic-a1/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a5/stable-m2", "")
except: pass
try: pcglabels.add_node("component-a6/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-a5/stable-m2", "component-a6/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a4/open-m5", "")
except: pass
try: pcglabels.add_node("component-a4/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m5", "component-a4/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic-a1/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-a1/component-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/elastic-m1", "component-a1/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("minimum0-a1/minimum0-m3", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("minimum0-a1/minimum0-m3", "elastic-a1/elastic-m3"), label="MINIMUM")
except: pass

try: pcglabels.add_node("count1-a1/count1-m2", "")
except: pass
try: pcglabels.add_node("inelastic-a1/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count1-a1/count1-m2", "inelastic-a1/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("inelastic-a1/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count1-a1/count1-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/inelastic-m1", "count1-a1/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("potentiallyViolable/notViolable", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("potentiallyViolable/notViolable", "desmeme/desmeme"), label="VIOLABILITY")
except: pass

try: pcglabels.add_node("component-a5/component-m5", "")
except: pass
try: pcglabels.add_node("inelastic-a3/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m5", "inelastic-a3/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-a3/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-a5/component-m4", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/elastic-m3", "component-a5/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a4/stable-m2", "")
except: pass
try: pcglabels.add_node("component-a5/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-a4/stable-m2", "component-a5/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a1/component-m3", "")
except: pass
try: pcglabels.add_node("stable-a1/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m3", "stable-a1/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a3/open-m1", "")
except: pass
try: pcglabels.add_node("component-a3/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m1", "component-a3/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a1/open-m1", "")
except: pass
try: pcglabels.add_node("component-a1/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m1", "component-a1/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a5/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-a5/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m4", "coherent-a5/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a3/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-a3/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-a3/coherent-m3", "open-a3/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a2/component-m1", "")
except: pass
try: pcglabels.add_node("stable-a2/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m1", "stable-a2/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("stable-a4/stable-m3", "")
except: pass
try: pcglabels.add_node("component-a5/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-a4/stable-m3", "component-a5/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a6/component-m3", "")
except: pass
try: pcglabels.add_node("stable-a5/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m3", "stable-a5/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a3/component-m5", "")
except: pass
try: pcglabels.add_node("stable-a3/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m5", "stable-a3/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a2/component-m1", "")
except: pass
try: pcglabels.add_node("open-a2/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m1", "open-a2/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m1", "")
except: pass
try: pcglabels.add_node("maximum1-a1/maximum1-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m1", "maximum1-a1/maximum1-m1"), label="MAXIMUM")
except: pass

try: pcglabels.add_node("open-a3/open-m2", "")
except: pass
try: pcglabels.add_node("component-a3/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m2", "component-a3/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a1/component-m2", "")
except: pass
try: pcglabels.add_node("inelastic-a1/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m2", "inelastic-a1/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a6/open-m2", "")
except: pass
try: pcglabels.add_node("component-a6/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m2", "component-a6/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic-a2/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-a4/component-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/inelastic-m1", "component-a4/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a5/component-m1", "")
except: pass
try: pcglabels.add_node("open-a5/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m1", "open-a5/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a3/component-m2", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m2", "elastic-a2/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("coherent-a5/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-a5/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-a5/coherent-m1", "open-a5/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a3/component-m3", "")
except: pass
try: pcglabels.add_node("open-a3/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m3", "open-a3/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a1/component-m2", "")
except: pass
try: pcglabels.add_node("open-a1/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m2", "open-a1/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m1", "")
except: pass
try: pcglabels.add_node("minimum0-a1/minimum0-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m1", "minimum0-a1/minimum0-m1"), label="MINIMUM")
except: pass

try: pcglabels.add_node("open-a1/open-m3", "")
except: pass
try: pcglabels.add_node("component-a1/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m3", "component-a1/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a5/open-m3", "")
except: pass
try: pcglabels.add_node("component-a5/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m3", "component-a5/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a2/component-m4", "")
except: pass
try: pcglabels.add_node("stable-a2/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m4", "stable-a2/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a2/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-a2/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-a2/coherent-m4", "open-a2/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a4/component-m2", "")
except: pass
try: pcglabels.add_node("open-a4/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m2", "open-a4/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("component-a1/component-m1", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "component-a1/component-m1"), label="LEFT_SUPPORT")
except: pass

try: pcglabels.add_node("elastic-a2/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-a3/component-m5", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/inelastic-m2", "component-a3/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("constructionalConditioning/constructionalConditioning", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "constructionalConditioning/constructionalConditioning"), label="CONDITIONING")
except: pass

try: pcglabels.add_node("open-a4/open-m1", "")
except: pass
try: pcglabels.add_node("component-a4/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m1", "component-a4/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a4/component-m3", "")
except: pass
try: pcglabels.add_node("open-a4/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m3", "open-a4/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic-a2/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-a4/component-m4", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/elastic-m3", "component-a4/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("order/order", "")
except: pass
try: pcglabels.add_node("simple/simple", "")
except: pass

try: pcglabels.add_edge(("order/order", "simple/simple"), label="RELATIONS")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("component-a3/component-m3", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "component-a3/component-m3"), label="LEFT_VOUSSOIR")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-a6/component-m4", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m3", "component-a6/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-a2/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-a4/component-m5", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/inelastic-m2", "component-a4/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a3/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-a3/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m4", "coherent-a3/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-a1/stable-m4", "")
except: pass
try: pcglabels.add_node("component-a1/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-a1/stable-m4", "component-a1/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("order/order", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("order/order", "desmeme/desmeme"), label="STRICTURE")
except: pass

try: pcglabels.add_node("inelastic-a1/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-a1/component-m3", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/elastic-m2", "component-a1/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a5/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-a5/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m2", "coherent-a5/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-a1/stable-m5", "")
except: pass
try: pcglabels.add_node("component-a1/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-a1/stable-m5", "component-a1/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "desmeme/desmeme"), label="FOUNDATION")
except: pass

try: pcglabels.add_node("component-a5/component-m3", "")
except: pass
try: pcglabels.add_node("open-a5/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m3", "open-a5/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a5/component-m4", "")
except: pass
try: pcglabels.add_node("stable-a4/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m4", "stable-a4/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a2/component-m5", "")
except: pass
try: pcglabels.add_node("open-a2/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m5", "open-a2/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a5/component-m1", "")
except: pass
try: pcglabels.add_node("stable-a4/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m1", "stable-a4/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a5/component-m2", "")
except: pass
try: pcglabels.add_node("stable-a4/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m2", "stable-a4/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-a1/order", "")
except: pass
try: pcglabels.add_node("count1-a1/count5-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/order", "count1-a1/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-a2/component-m3", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m2", "component-a2/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a2/component-m2", "")
except: pass
try: pcglabels.add_node("stable-a2/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m2", "stable-a2/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a1/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-a1/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-a1/coherent-m2", "open-a1/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("minimum0-a3/minimum0-m2", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("minimum0-a3/minimum0-m2", "elastic-a3/elastic-m2"), label="MINIMUM")
except: pass

try: pcglabels.add_node("minimum0-a1/minimum0-m2", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("minimum0-a1/minimum0-m2", "elastic-a1/elastic-m2"), label="MINIMUM")
except: pass

try: pcglabels.add_node("stable-a3/stable-m2", "")
except: pass
try: pcglabels.add_node("component-a3/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-a3/stable-m2", "component-a3/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("minimum0-a3/minimum0-m3", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("minimum0-a3/minimum0-m3", "elastic-a3/elastic-m3"), label="MINIMUM")
except: pass

try: pcglabels.add_node("component-a4/component-m5", "")
except: pass
try: pcglabels.add_node("open-a4/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m5", "open-a4/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("maximum100-a2/maximum1-m1", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("maximum100-a2/maximum1-m1", "elastic-a3/elastic-m1"), label="MAXIMUM")
except: pass

try: pcglabels.add_node("coherent-a1/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-a1/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-a1/coherent-m1", "open-a1/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a6/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-a6/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m5", "coherent-a6/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("count1-a2/count1-m2", "")
except: pass
try: pcglabels.add_node("inelastic-a2/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count1-a2/count1-m2", "inelastic-a2/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("minimum0-a2/minimum0-m3", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("minimum0-a2/minimum0-m3", "elastic-a2/elastic-m3"), label="MINIMUM")
except: pass

try: pcglabels.add_node("count6-a1/count5-m1", "")
except: pass
try: pcglabels.add_node("order/order", "")
except: pass

try: pcglabels.add_edge(("count6-a1/count5-m1", "order/order"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a5/component-m2", "")
except: pass
try: pcglabels.add_node("open-a5/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m2", "open-a5/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count1-a1/count1-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a1/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count1-a1/count1-m1", "inelastic-a1/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a6/component-m4", "")
except: pass
try: pcglabels.add_node("stable-a5/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m4", "stable-a5/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("unstable-a1/stable-m2", "")
except: pass
try: pcglabels.add_node("component-a4/component-m2", "")
except: pass

try: pcglabels.add_edge(("unstable-a1/stable-m2", "component-a4/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("elastic-a3/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-a6/component-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/inelastic-m1", "component-a6/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a5/component-m2", "")
except: pass
try: pcglabels.add_node("inelastic-a3/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m2", "inelastic-a3/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("constructionalConditioning/constructionalConditioning", "")
except: pass
try: pcglabels.add_node("desmeme/desmeme", "")
except: pass

try: pcglabels.add_edge(("constructionalConditioning/constructionalConditioning", "desmeme/desmeme"), label="CONDITIONING")
except: pass

try: pcglabels.add_node("component-a1/component-m5", "")
except: pass
try: pcglabels.add_node("inelastic-a1/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m5", "inelastic-a1/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-a6/component-m3", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m2", "component-a6/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a2/component-m5", "")
except: pass
try: pcglabels.add_node("elastic-a1/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m5", "elastic-a1/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("component-a4/component-m4", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "component-a4/component-m4"), label="RIGHT_VOUSSOIR")
except: pass

try: pcglabels.add_node("open-a2/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-a2/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m3", "coherent-a2/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("unstable-a1/stable-m3", "")
except: pass
try: pcglabels.add_node("component-a4/component-m3", "")
except: pass

try: pcglabels.add_edge(("unstable-a1/stable-m3", "component-a4/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-a2/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-a4/component-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/elastic-m1", "component-a4/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a6/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-a6/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m4", "coherent-a6/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-a2/stable-m1", "")
except: pass
try: pcglabels.add_node("component-a2/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-a2/stable-m1", "component-a2/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a2/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-a2/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-a2/coherent-m2", "open-a2/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m1", "")
except: pass
try: pcglabels.add_node("maximum100-a2/maximum1-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m1", "maximum100-a2/maximum1-m1"), label="MAXIMUM")
except: pass

try: pcglabels.add_node("component-a5/component-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a3/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m1", "inelastic-a3/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a1/component-m1", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m1", "arch/arch"), label="LEFT_SUPPORT")
except: pass

try: pcglabels.add_node("component-a3/component-m4", "")
except: pass
try: pcglabels.add_node("open-a3/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m4", "open-a3/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m1", "")
except: pass
try: pcglabels.add_node("minimum0-a3/minimum0-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m1", "minimum0-a3/minimum0-m1"), label="MINIMUM")
except: pass

try: pcglabels.add_node("component-a6/component-m2", "")
except: pass
try: pcglabels.add_node("open-a6/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m2", "open-a6/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a1/elastic-m3", "")
except: pass
try: pcglabels.add_node("minimum0-a1/minimum0-m3", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/elastic-m3", "minimum0-a1/minimum0-m3"), label="MINIMUM")
except: pass

try: pcglabels.add_node("open-a2/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-a2/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m4", "coherent-a2/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a4/component-m5", "")
except: pass
try: pcglabels.add_node("unstable-a1/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m5", "unstable-a1/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-a3/component-m2", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m1", "component-a3/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a5/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-a5/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m5", "coherent-a5/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass
try: pcglabels.add_node("component-a2/component-m2", "")
except: pass

try: pcglabels.add_edge(("restkomponentenSet/restkomponentenSet", "component-a2/component-m2"), label="RESTKOMPONENT")
except: pass

try: pcglabels.add_node("count1-a3/count1-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a3/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count1-a3/count1-m1", "inelastic-a3/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("coherent-a2/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-a2/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-a2/coherent-m1", "open-a2/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a2/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-a2/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m2", "coherent-a2/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a4/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-a4/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m1", "coherent-a4/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a5/open-m4", "")
except: pass
try: pcglabels.add_node("component-a5/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m4", "component-a5/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("stable-a5/stable-m1", "")
except: pass
try: pcglabels.add_node("component-a6/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-a5/stable-m1", "component-a6/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("stable-a2/stable-m3", "")
except: pass
try: pcglabels.add_node("component-a2/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-a2/stable-m3", "component-a2/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a1/component-m5", "")
except: pass
try: pcglabels.add_node("open-a1/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m5", "open-a1/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a6/open-m5", "")
except: pass
try: pcglabels.add_node("component-a6/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m5", "component-a6/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("coherent-a5/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-a5/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-a5/incoherent-m1", "open-a5/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a6/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-a6/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-a6/coherent-m2", "open-a6/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-a3/stable-m4", "")
except: pass
try: pcglabels.add_node("component-a3/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-a3/stable-m4", "component-a3/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a4/component-m1", "")
except: pass
try: pcglabels.add_node("open-a4/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m1", "open-a4/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a4/component-m5", "")
except: pass
try: pcglabels.add_node("inelastic-a2/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m5", "inelastic-a2/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a3/component-m5", "")
except: pass
try: pcglabels.add_node("elastic-a2/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m5", "elastic-a2/inelastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a4/component-m4", "")
except: pass
try: pcglabels.add_node("inelastic-a2/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m4", "inelastic-a2/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a2/stable-m4", "")
except: pass
try: pcglabels.add_node("component-a2/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-a2/stable-m4", "component-a2/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a2/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-a2/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-a2/incoherent-m1", "open-a2/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("component-a5/component-m5", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "component-a5/component-m5"), label="KEYSTONE")
except: pass

try: pcglabels.add_node("component-a6/component-m4", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m4", "elastic-a3/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a5/stable-m5", "")
except: pass
try: pcglabels.add_node("component-a6/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-a5/stable-m5", "component-a6/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("restkomponentenSet/restkomponentenSet", "arch/arch"), label="RESTKOMPONENTEN")
except: pass

try: pcglabels.add_node("inelastic-a2/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count1-a2/count1-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/inelastic-m1", "count1-a2/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("inelastic-a2/elastic-m2", "")
except: pass
try: pcglabels.add_node("component-a4/component-m3", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/elastic-m2", "component-a4/component-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a1/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-a1/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m5", "coherent-a1/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a6/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-a6/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-a6/coherent-m1", "open-a6/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a2/open-m1", "")
except: pass
try: pcglabels.add_node("component-a2/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m1", "component-a2/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a3/component-m5", "")
except: pass
try: pcglabels.add_node("open-a3/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m5", "open-a3/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a2/open-m3", "")
except: pass
try: pcglabels.add_node("component-a2/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m3", "component-a2/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a3/component-m2", "")
except: pass
try: pcglabels.add_node("stable-a3/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m2", "stable-a3/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a1/component-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a1/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m1", "inelastic-a1/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a1/open-m2", "")
except: pass
try: pcglabels.add_node("component-a1/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m2", "component-a1/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a4/component-m2", "")
except: pass
try: pcglabels.add_node("inelastic-a2/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m2", "inelastic-a2/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-a3/component-m4", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m3", "component-a3/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a3/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-a3/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m3", "coherent-a3/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a4/open-m3", "")
except: pass
try: pcglabels.add_node("component-a4/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m3", "component-a4/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a1/component-m2", "")
except: pass
try: pcglabels.add_node("stable-a1/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m2", "stable-a1/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a1/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-a1/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m2", "coherent-a1/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("count1-a2/count1-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a2/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("count1-a2/count1-m1", "inelastic-a2/inelastic-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a4/component-m4", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m4", "arch/arch"), label="RIGHT_VOUSSOIR")
except: pass

try: pcglabels.add_node("component-a1/component-m3", "")
except: pass
try: pcglabels.add_node("inelastic-a1/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m3", "inelastic-a1/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("minimum0-a2/minimum0-m2", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("minimum0-a2/minimum0-m2", "elastic-a2/elastic-m2"), label="MINIMUM")
except: pass

try: pcglabels.add_node("stable-a2/stable-m2", "")
except: pass
try: pcglabels.add_node("component-a2/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-a2/stable-m2", "component-a2/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("stable-a4/stable-m5", "")
except: pass
try: pcglabels.add_node("component-a5/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-a4/stable-m5", "component-a5/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a6/open-m3", "")
except: pass
try: pcglabels.add_node("component-a6/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m3", "component-a6/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a6/component-m1", "")
except: pass
try: pcglabels.add_node("open-a6/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m1", "open-a6/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("coherent-a5/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-a5/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-a5/coherent-m4", "open-a5/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("inelastic-a3/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count1-a3/count1-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/inelastic-m2", "count1-a3/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("open-a1/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-a1/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m1", "coherent-a1/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m3", "")
except: pass
try: pcglabels.add_node("minimum0-a2/minimum0-m3", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m3", "minimum0-a2/minimum0-m3"), label="MINIMUM")
except: pass

try: pcglabels.add_node("coherent-a3/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-a3/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-a3/coherent-m1", "open-a3/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a4/open-m4", "")
except: pass
try: pcglabels.add_node("component-a4/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m4", "component-a4/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic-a3/elastic-m1", "")
except: pass
try: pcglabels.add_node("component-a5/component-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/elastic-m1", "component-a5/component-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a1/stable-m1", "")
except: pass
try: pcglabels.add_node("component-a1/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-a1/stable-m1", "component-a1/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("stable-a3/stable-m5", "")
except: pass
try: pcglabels.add_node("component-a3/component-m5", "")
except: pass

try: pcglabels.add_edge(("stable-a3/stable-m5", "component-a3/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a6/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-a6/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-a6/incoherent-m1", "open-a6/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a3/component-m1", "")
except: pass
try: pcglabels.add_node("open-a3/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m1", "open-a3/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("count1-a3/count5-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a3/order", "")
except: pass

try: pcglabels.add_edge(("count1-a3/count5-m1", "inelastic-a3/order"), label="COUNT")
except: pass

try: pcglabels.add_node("open-a3/open-m4", "")
except: pass
try: pcglabels.add_node("component-a3/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m4", "component-a3/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a2/component-m3", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m3", "elastic-a1/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a5/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-a5/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m1", "coherent-a5/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("order/order", "")
except: pass
try: pcglabels.add_node("count6-a1/count5-m1", "")
except: pass

try: pcglabels.add_edge(("order/order", "count6-a1/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("stable-a4/stable-m1", "")
except: pass
try: pcglabels.add_node("component-a5/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-a4/stable-m1", "component-a5/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a3/component-m4", "")
except: pass
try: pcglabels.add_node("stable-a3/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m4", "stable-a3/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a5/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-a5/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-a5/coherent-m2", "open-a5/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a2/open-m2", "")
except: pass
try: pcglabels.add_node("component-a2/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m2", "component-a2/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic-a1/elastic-m3", "")
except: pass
try: pcglabels.add_node("component-a1/component-m4", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/elastic-m3", "component-a1/component-m4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("component-a6/component-m4", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "component-a6/component-m4"), label="RIGHT_SUPPORT")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m1", "")
except: pass
try: pcglabels.add_node("maximum100-a1/maximum1-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m1", "maximum100-a1/maximum1-m1"), label="MAXIMUM")
except: pass

try: pcglabels.add_node("inelastic-a3/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count1-a3/count1-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/inelastic-m1", "count1-a3/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m1", "")
except: pass
try: pcglabels.add_node("minimum0-a2/minimum0-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m1", "minimum0-a2/minimum0-m1"), label="MINIMUM")
except: pass

try: pcglabels.add_node("open-a6/open-m4", "")
except: pass
try: pcglabels.add_node("component-a6/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m4", "component-a6/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a4/component-m3", "")
except: pass
try: pcglabels.add_node("unstable-a1/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m3", "unstable-a1/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a6/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-a6/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m2", "coherent-a6/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("inelastic-a3/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-a5/component-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/inelastic-m1", "component-a5/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("elastic-a3/elastic-m3", "")
except: pass
try: pcglabels.add_node("minimum0-a3/minimum0-m3", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/elastic-m3", "minimum0-a3/minimum0-m3"), label="MINIMUM")
except: pass

try: pcglabels.add_node("component-a5/component-m5", "")
except: pass
try: pcglabels.add_node("open-a5/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m5", "open-a5/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("stable-a1/stable-m2", "")
except: pass
try: pcglabels.add_node("component-a1/component-m2", "")
except: pass

try: pcglabels.add_edge(("stable-a1/stable-m2", "component-a1/component-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a4/component-m4", "")
except: pass
try: pcglabels.add_node("unstable-a1/stable-m4", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m4", "unstable-a1/stable-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("maximum100-a1/maximum1-m1", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("maximum100-a1/maximum1-m1", "elastic-a2/elastic-m1"), label="MAXIMUM")
except: pass

try: pcglabels.add_node("unstable-a1/stable-m5", "")
except: pass
try: pcglabels.add_node("component-a4/component-m5", "")
except: pass

try: pcglabels.add_edge(("unstable-a1/stable-m5", "component-a4/component-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a5/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-a5/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m3", "coherent-a5/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a6/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-a6/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m3", "coherent-a6/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("count1-a3/count1-m2", "")
except: pass
try: pcglabels.add_node("inelastic-a3/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count1-a3/count1-m2", "inelastic-a3/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a2/component-m2", "")
except: pass
try: pcglabels.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m2", "restkomponentenSet/restkomponentenSet"), label="RESTKOMPONENT")
except: pass

try: pcglabels.add_node("component-a6/component-m5", "")
except: pass
try: pcglabels.add_node("stable-a5/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m5", "stable-a5/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a1/component-m4", "")
except: pass
try: pcglabels.add_node("open-a1/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m4", "open-a1/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a2/component-m3", "")
except: pass
try: pcglabels.add_node("stable-a2/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m3", "stable-a2/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a4/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-a4/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-a4/incoherent-m1", "open-a4/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a4/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-a4/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-a4/coherent-m3", "open-a4/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a3/coherent-m2", "")
except: pass
try: pcglabels.add_node("open-a3/open-m2", "")
except: pass

try: pcglabels.add_edge(("coherent-a3/coherent-m2", "open-a3/open-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a5/component-m4", "")
except: pass
try: pcglabels.add_node("open-a5/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m4", "open-a5/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("stable-a3/stable-m3", "")
except: pass
try: pcglabels.add_node("component-a3/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-a3/stable-m3", "component-a3/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a6/component-m1", "")
except: pass
try: pcglabels.add_node("stable-a5/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m1", "stable-a5/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a4/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-a4/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m5", "coherent-a4/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("minimum0-a3/minimum0-m1", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("minimum0-a3/minimum0-m1", "elastic-a3/elastic-m1"), label="MINIMUM")
except: pass

try: pcglabels.add_node("component-a2/component-m3", "")
except: pass
try: pcglabels.add_node("open-a2/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m3", "open-a2/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a3/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-a6/component-m5", "")
except: pass

try: pcglabels.add_edge(("elastic-a3/inelastic-m2", "component-a6/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-a3/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-a5/component-m5", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/inelastic-m2", "component-a5/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a5/component-m5", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m5", "arch/arch"), label="KEYSTONE")
except: pass

try: pcglabels.add_node("inelastic-a3/order", "")
except: pass
try: pcglabels.add_node("count1-a3/count5-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a3/order", "count1-a3/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a3/component-m4", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m4", "elastic-a2/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("unstable-a1/stable-m1", "")
except: pass
try: pcglabels.add_node("component-a4/component-m1", "")
except: pass

try: pcglabels.add_edge(("unstable-a1/stable-m1", "component-a4/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a3/component-m3", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m3", "arch/arch"), label="LEFT_VOUSSOIR")
except: pass

try: pcglabels.add_node("inelastic-a1/inelastic-m2", "")
except: pass
try: pcglabels.add_node("count1-a1/count1-m2", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/inelastic-m2", "count1-a1/count1-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("open-a5/open-m1", "")
except: pass
try: pcglabels.add_node("component-a5/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m1", "component-a5/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a6/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-a6/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m1", "coherent-a6/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a4/coherent-m1", "")
except: pass
try: pcglabels.add_node("open-a4/open-m1", "")
except: pass

try: pcglabels.add_edge(("coherent-a4/coherent-m1", "open-a4/open-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("coherent-a1/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-a1/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-a1/coherent-m4", "open-a1/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("arch/arch", "")
except: pass
try: pcglabels.add_node("restkomponentenSet/restkomponentenSet", "")
except: pass

try: pcglabels.add_edge(("arch/arch", "restkomponentenSet/restkomponentenSet"), label="RESTKOMPONENTEN")
except: pass

try: pcglabels.add_node("elastic-a2/elastic-m2", "")
except: pass
try: pcglabels.add_node("minimum0-a2/minimum0-m2", "")
except: pass

try: pcglabels.add_edge(("elastic-a2/elastic-m2", "minimum0-a2/minimum0-m2"), label="MINIMUM")
except: pass

try: pcglabels.add_node("coherent-a3/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-a3/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-a3/coherent-m4", "open-a3/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("inelastic-a2/order", "")
except: pass
try: pcglabels.add_node("count1-a2/count5-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a2/order", "count1-a2/count5-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a2/component-m5", "")
except: pass
try: pcglabels.add_node("stable-a2/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m5", "stable-a2/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("order/order", "")
except: pass
try: pcglabels.add_node("syntacticConstituent/syntacticConstituent", "")
except: pass

try: pcglabels.add_edge(("order/order", "syntacticConstituent/syntacticConstituent"), label="CONSTITUENT")
except: pass

try: pcglabels.add_node("unstable-a1/stable-m4", "")
except: pass
try: pcglabels.add_node("component-a4/component-m4", "")
except: pass

try: pcglabels.add_edge(("unstable-a1/stable-m4", "component-a4/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a6/component-m5", "")
except: pass
try: pcglabels.add_node("open-a6/open-m5", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m5", "open-a6/open-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("stable-a3/stable-m1", "")
except: pass
try: pcglabels.add_node("component-a3/component-m1", "")
except: pass

try: pcglabels.add_edge(("stable-a3/stable-m1", "component-a3/component-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a6/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-a6/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-a6/coherent-m3", "open-a6/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a2/open-m4", "")
except: pass
try: pcglabels.add_node("component-a2/component-m4", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m4", "component-a2/component-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a4/component-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a2/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m1", "inelastic-a2/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a3/open-m5", "")
except: pass
try: pcglabels.add_node("component-a3/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m5", "component-a3/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a1/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-a1/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m4", "coherent-a1/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a1/open-m5", "")
except: pass
try: pcglabels.add_node("component-a1/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-a1/open-m5", "component-a1/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a6/open-m1", "")
except: pass
try: pcglabels.add_node("component-a6/component-m1", "")
except: pass

try: pcglabels.add_edge(("open-a6/open-m1", "component-a6/component-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a2/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-a2/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m1", "coherent-a2/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a4/component-m3", "")
except: pass
try: pcglabels.add_node("inelastic-a2/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m3", "inelastic-a2/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a6/component-m2", "")
except: pass
try: pcglabels.add_node("stable-a5/stable-m2", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m2", "stable-a5/stable-m2"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a4/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-a4/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m2", "coherent-a4/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a5/open-m5", "")
except: pass
try: pcglabels.add_node("component-a5/component-m5", "")
except: pass

try: pcglabels.add_edge(("open-a5/open-m5", "component-a5/component-m5"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a2/component-m4", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m4", "elastic-a1/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a5/component-m4", "")
except: pass
try: pcglabels.add_node("inelastic-a3/elastic-m3", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m4", "inelastic-a3/elastic-m3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic-a1/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-a1/component-m1", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/inelastic-m1", "component-a1/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("coherent-a1/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-a1/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-a1/coherent-m3", "open-a1/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a2/component-m2", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m2", "elastic-a1/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a3/open-m1", "")
except: pass
try: pcglabels.add_node("coherent-a3/coherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m1", "coherent-a3/coherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("open-a2/open-m5", "")
except: pass
try: pcglabels.add_node("coherent-a2/coherent-m4", "")
except: pass

try: pcglabels.add_edge(("open-a2/open-m5", "coherent-a2/coherent-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a5/component-m3", "")
except: pass
try: pcglabels.add_node("inelastic-a3/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m3", "inelastic-a3/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a2/component-m4", "")
except: pass
try: pcglabels.add_node("open-a2/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m4", "open-a2/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("order/inelastic-m1", "")
except: pass
try: pcglabels.add_node("count6-a1/count1-m1", "")
except: pass

try: pcglabels.add_edge(("order/inelastic-m1", "count6-a1/count1-m1"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a3/component-m3", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m3", "elastic-a2/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open-a3/open-m3", "")
except: pass
try: pcglabels.add_node("component-a3/component-m3", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m3", "component-a3/component-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a1/component-m1", "")
except: pass
try: pcglabels.add_node("open-a1/open-m1", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m1", "open-a1/open-m1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a4/open-m3", "")
except: pass
try: pcglabels.add_node("coherent-a4/coherent-m3", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m3", "coherent-a4/coherent-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a3/component-m1", "")
except: pass
try: pcglabels.add_node("elastic-a2/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m1", "elastic-a2/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("potentiallyViolable/notViolable", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "potentiallyViolable/notViolable"), label="VIOLABILITY")
except: pass

try: pcglabels.add_node("coherent-a5/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-a5/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-a5/coherent-m3", "open-a5/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("count1-a1/count5-m1", "")
except: pass
try: pcglabels.add_node("inelastic-a1/order", "")
except: pass

try: pcglabels.add_edge(("count1-a1/count5-m1", "inelastic-a1/order"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a6/component-m3", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m2", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m3", "elastic-a3/elastic-m2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a3/component-m2", "")
except: pass
try: pcglabels.add_node("open-a3/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-a3/component-m2", "open-a3/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a4/component-m4", "")
except: pass
try: pcglabels.add_node("open-a4/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-a4/component-m4", "open-a4/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("coherent-a2/coherent-m3", "")
except: pass
try: pcglabels.add_node("open-a2/open-m3", "")
except: pass

try: pcglabels.add_edge(("coherent-a2/coherent-m3", "open-a2/open-m3"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a1/component-m5", "")
except: pass
try: pcglabels.add_node("stable-a1/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m5", "stable-a1/stable-m5"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a4/open-m4", "")
except: pass
try: pcglabels.add_node("coherent-a4/incoherent-m1", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m4", "coherent-a4/incoherent-m1"), label="COHERENCE")
except: pass

try: pcglabels.add_node("elastic-a1/inelastic-m1", "")
except: pass
try: pcglabels.add_node("component-a2/component-m1", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/inelastic-m1", "component-a2/component-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a5/stable-m4", "")
except: pass
try: pcglabels.add_node("component-a6/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-a5/stable-m4", "component-a6/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("open-a3/open-m2", "")
except: pass
try: pcglabels.add_node("coherent-a3/coherent-m2", "")
except: pass

try: pcglabels.add_edge(("open-a3/open-m2", "coherent-a3/coherent-m2"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a6/component-m3", "")
except: pass
try: pcglabels.add_node("open-a6/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m3", "open-a6/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("coherent-a3/incoherent-m1", "")
except: pass
try: pcglabels.add_node("open-a3/open-m4", "")
except: pass

try: pcglabels.add_edge(("coherent-a3/incoherent-m1", "open-a3/open-m4"), label="COHERENCE")
except: pass

try: pcglabels.add_node("component-a1/component-m3", "")
except: pass
try: pcglabels.add_node("open-a1/open-m3", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m3", "open-a1/open-m3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open-a4/open-m2", "")
except: pass
try: pcglabels.add_node("component-a4/component-m2", "")
except: pass

try: pcglabels.add_edge(("open-a4/open-m2", "component-a4/component-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("elastic-a1/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-a2/component-m5", "")
except: pass

try: pcglabels.add_edge(("elastic-a1/inelastic-m2", "component-a2/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("stable-a4/stable-m4", "")
except: pass
try: pcglabels.add_node("component-a5/component-m4", "")
except: pass

try: pcglabels.add_edge(("stable-a4/stable-m4", "component-a5/component-m4"), label="STABILITY")
except: pass

try: pcglabels.add_node("coherent-a6/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-a6/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-a6/coherent-m4", "open-a6/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("stable-a5/stable-m3", "")
except: pass
try: pcglabels.add_node("component-a6/component-m3", "")
except: pass

try: pcglabels.add_edge(("stable-a5/stable-m3", "component-a6/component-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic-a1/inelastic-m2", "")
except: pass
try: pcglabels.add_node("component-a1/component-m5", "")
except: pass

try: pcglabels.add_edge(("inelastic-a1/inelastic-m2", "component-a1/component-m5"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("coherent-a4/coherent-m4", "")
except: pass
try: pcglabels.add_node("open-a4/open-m5", "")
except: pass

try: pcglabels.add_edge(("coherent-a4/coherent-m4", "open-a4/open-m5"), label="COHERENCE")
except: pass

try: pcglabels.add_node("minimum0-a1/minimum0-m1", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("minimum0-a1/minimum0-m1", "elastic-a1/elastic-m1"), label="MINIMUM")
except: pass

try: pcglabels.add_node("count6-a1/count1-m2", "")
except: pass
try: pcglabels.add_node("order/inelastic-m2", "")
except: pass

try: pcglabels.add_edge(("count6-a1/count1-m2", "order/inelastic-m2"), label="COUNT")
except: pass

try: pcglabels.add_node("component-a6/component-m4", "")
except: pass
try: pcglabels.add_node("arch/arch", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m4", "arch/arch"), label="RIGHT_SUPPORT")
except: pass

try: pcglabels.add_node("maximum1-a1/maximum1-m1", "")
except: pass
try: pcglabels.add_node("elastic-a1/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("maximum1-a1/maximum1-m1", "elastic-a1/elastic-m1"), label="MAXIMUM")
except: pass

try: pcglabels.add_node("component-a5/component-m3", "")
except: pass
try: pcglabels.add_node("stable-a4/stable-m3", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m3", "stable-a4/stable-m3"), label="STABILITY")
except: pass

try: pcglabels.add_node("minimum0-a2/minimum0-m1", "")
except: pass
try: pcglabels.add_node("elastic-a2/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("minimum0-a2/minimum0-m1", "elastic-a2/elastic-m1"), label="MINIMUM")
except: pass

try: pcglabels.add_node("simple/simple", "")
except: pass
try: pcglabels.add_node("order/order", "")
except: pass

try: pcglabels.add_edge(("simple/simple", "order/order"), label="RELATIONS")
except: pass

try: pcglabels.add_node("component-a6/component-m4", "")
except: pass
try: pcglabels.add_node("open-a6/open-m4", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m4", "open-a6/open-m4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a6/component-m1", "")
except: pass
try: pcglabels.add_node("elastic-a3/inelastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m1", "elastic-a3/inelastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("desmeme/desmeme", "")
except: pass
try: pcglabels.add_node("order/order", "")
except: pass

try: pcglabels.add_edge(("desmeme/desmeme", "order/order"), label="STRICTURE")
except: pass

try: pcglabels.add_node("component-a6/component-m2", "")
except: pass
try: pcglabels.add_node("elastic-a3/elastic-m1", "")
except: pass

try: pcglabels.add_edge(("component-a6/component-m2", "elastic-a3/elastic-m1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component-a2/component-m2", "")
except: pass
try: pcglabels.add_node("open-a2/open-m2", "")
except: pass

try: pcglabels.add_edge(("component-a2/component-m2", "open-a2/open-m2"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component-a1/component-m1", "")
except: pass
try: pcglabels.add_node("stable-a1/stable-m1", "")
except: pass

try: pcglabels.add_edge(("component-a1/component-m1", "stable-a1/stable-m1"), label="STABILITY")
except: pass

try: pcglabels.add_node("component-a5/component-m5", "")
except: pass
try: pcglabels.add_node("stable-a4/stable-m5", "")
except: pass

try: pcglabels.add_edge(("component-a5/component-m5", "stable-a4/stable-m5"), label="STABILITY")
except: pass

try: AghemClause.add_node("unstable-a1", "")
except: pass
try: AghemClause.add_node("component-a2", "")
except: pass

try: AghemClause.add_edge(("unstable-a1", "component-a2"), label=" ASSOCIATE")
except: pass

try: AghemClause.add_node("unstable-a1", "")
except: pass
try: AghemClause.add_node("left", "")
except: pass

try: AghemClause.add_edge(("unstable-a1", "left"), label=" ASSOCIATE_POSITION")
except: pass

try: AghemClause.add_node("elastic-a2", "")
except: pass
try: AghemClause.add_node("minimum0-a2", "")
except: pass

try: AghemClause.add_edge(("elastic-a2", "minimum0-a2"), label=" MINIMUM")
except: pass

try: AghemClause.add_node("inelastic-a1", "")
except: pass
try: AghemClause.add_node("count1-a1", "")
except: pass

try: AghemClause.add_edge(("inelastic-a1", "count1-a1"), label=" COUNT")
except: pass

try: AghemClause.add_node("arch", "")
except: pass
try: AghemClause.add_node("component-a4", "")
except: pass

try: AghemClause.add_edge(("arch", "component-a4"), label=" RIGHT_VOUSSOIR")
except: pass

try: AghemClause.add_node("open-a2", "")
except: pass
try: AghemClause.add_node("coherent-a2", "")
except: pass

try: AghemClause.add_edge(("open-a2", "coherent-a2"), label=" COHERENCE")
except: pass

try: AghemClause.add_node("order", "")
except: pass
try: AghemClause.add_node("simple", "")
except: pass

try: AghemClause.add_edge(("order", "simple"), label=" RELATIONS")
except: pass

try: AghemClause.add_node("order", "")
except: pass
try: AghemClause.add_node("syntacticConstituent", "")
except: pass

try: AghemClause.add_edge(("order", "syntacticConstituent"), label=" CONSTITUENT")
except: pass

try: AghemClause.add_node("component-a2", "")
except: pass
try: AghemClause.add_node("stable-a2", "")
except: pass

try: AghemClause.add_edge(("component-a2", "stable-a2"), label=" STABILITY")
except: pass

try: AghemClause.add_node("open-a4", "")
except: pass
try: AghemClause.add_node("coherent-a4", "")
except: pass

try: AghemClause.add_edge(("open-a4", "coherent-a4"), label=" COHERENCE")
except: pass

try: AghemClause.add_node("component-a2", "")
except: pass
try: AghemClause.add_node("open-a2", "")
except: pass

try: AghemClause.add_edge(("component-a2", "open-a2"), label=" FILLEDNESS")
except: pass

try: AghemClause.add_node("component-a6", "")
except: pass
try: AghemClause.add_node("open-a6", "")
except: pass

try: AghemClause.add_edge(("component-a6", "open-a6"), label=" FILLEDNESS")
except: pass

try: AghemClause.add_node("component-a4", "")
except: pass
try: AghemClause.add_node("inelastic-a2", "")
except: pass

try: AghemClause.add_edge(("component-a4", "inelastic-a2"), label=" ELASTICITY")
except: pass

try: AghemClause.add_node("component-a3", "")
except: pass
try: AghemClause.add_node("stable-a3", "")
except: pass

try: AghemClause.add_edge(("component-a3", "stable-a3"), label=" STABILITY")
except: pass

try: AghemClause.add_node("inelastic-a2", "")
except: pass
try: AghemClause.add_node("count1-a2", "")
except: pass

try: AghemClause.add_edge(("inelastic-a2", "count1-a2"), label=" COUNT")
except: pass

try: AghemClause.add_node("arch", "")
except: pass
try: AghemClause.add_node("component-a6", "")
except: pass

try: AghemClause.add_edge(("arch", "component-a6"), label=" RIGHT_SUPPORT")
except: pass

try: AghemClause.add_node("component-a3", "")
except: pass
try: AghemClause.add_node("elastic-a2", "")
except: pass

try: AghemClause.add_edge(("component-a3", "elastic-a2"), label=" ELASTICITY")
except: pass

try: AghemClause.add_node("elastic-a1", "")
except: pass
try: AghemClause.add_node("minimum0-a1", "")
except: pass

try: AghemClause.add_edge(("elastic-a1", "minimum0-a1"), label=" MINIMUM")
except: pass

try: AghemClause.add_node("potentiallyViolable", "")
except: pass
try: AghemClause.add_node("morphosyntacticInsertion", "")
except: pass

try: AghemClause.add_edge(("potentiallyViolable", "morphosyntacticInsertion"), label=" REPARABILITY")
except: pass

try: AghemClause.add_node("open-a3", "")
except: pass
try: AghemClause.add_node("coherent-a3", "")
except: pass

try: AghemClause.add_edge(("open-a3", "coherent-a3"), label=" COHERENCE")
except: pass

try: AghemClause.add_node("component-a1", "")
except: pass
try: AghemClause.add_node("stable-a1", "")
except: pass

try: AghemClause.add_edge(("component-a1", "stable-a1"), label=" STABILITY")
except: pass

try: AghemClause.add_node("component-a4", "")
except: pass
try: AghemClause.add_node("unstable-a1", "")
except: pass

try: AghemClause.add_edge(("component-a4", "unstable-a1"), label=" STABILITY")
except: pass

try: AghemClause.add_node("component-a5", "")
except: pass
try: AghemClause.add_node("inelastic-a3", "")
except: pass

try: AghemClause.add_edge(("component-a5", "inelastic-a3"), label=" ELASTICITY")
except: pass

try: AghemClause.add_node("arch", "")
except: pass
try: AghemClause.add_node("restkomponentenSet", "")
except: pass

try: AghemClause.add_edge(("arch", "restkomponentenSet"), label=" RESTKOMPONENTEN")
except: pass

try: AghemClause.add_node("desmeme", "")
except: pass
try: AghemClause.add_node("potentiallyViolable", "")
except: pass

try: AghemClause.add_edge(("desmeme", "potentiallyViolable"), label=" VIOLABILITY")
except: pass

try: AghemClause.add_node("elastic-a3", "")
except: pass
try: AghemClause.add_node("minimum0-a3", "")
except: pass

try: AghemClause.add_edge(("elastic-a3", "minimum0-a3"), label=" MINIMUM")
except: pass

try: AghemClause.add_node("elastic-a2", "")
except: pass
try: AghemClause.add_node("maximum100-a1", "")
except: pass

try: AghemClause.add_edge(("elastic-a2", "maximum100-a1"), label=" MAXIMUM")
except: pass

try: AghemClause.add_node("component-a6", "")
except: pass
try: AghemClause.add_node("stable-a5", "")
except: pass

try: AghemClause.add_edge(("component-a6", "stable-a5"), label=" STABILITY")
except: pass

try: AghemClause.add_node("desmeme", "")
except: pass
try: AghemClause.add_node("order", "")
except: pass

try: AghemClause.add_edge(("desmeme", "order"), label=" STRICTURE")
except: pass

try: AghemClause.add_node("component-a2", "")
except: pass
try: AghemClause.add_node("elastic-a1", "")
except: pass

try: AghemClause.add_edge(("component-a2", "elastic-a1"), label=" ELASTICITY")
except: pass

try: AghemClause.add_node("component-a3", "")
except: pass
try: AghemClause.add_node("open-a3", "")
except: pass

try: AghemClause.add_edge(("component-a3", "open-a3"), label=" FILLEDNESS")
except: pass

try: AghemClause.add_node("component-a4", "")
except: pass
try: AghemClause.add_node("open-a4", "")
except: pass

try: AghemClause.add_edge(("component-a4", "open-a4"), label=" FILLEDNESS")
except: pass

try: AghemClause.add_node("component-a1", "")
except: pass
try: AghemClause.add_node("inelastic-a1", "")
except: pass

try: AghemClause.add_edge(("component-a1", "inelastic-a1"), label=" ELASTICITY")
except: pass

try: AghemClause.add_node("potentiallyViolable", "")
except: pass
try: AghemClause.add_node("lexical", "")
except: pass

try: AghemClause.add_edge(("potentiallyViolable", "lexical"), label=" EXCEPTIONALITY")
except: pass

try: AghemClause.add_node("component-a5", "")
except: pass
try: AghemClause.add_node("stable-a4", "")
except: pass

try: AghemClause.add_edge(("component-a5", "stable-a4"), label=" STABILITY")
except: pass

try: AghemClause.add_node("inelastic-a3", "")
except: pass
try: AghemClause.add_node("count1-a3", "")
except: pass

try: AghemClause.add_edge(("inelastic-a3", "count1-a3"), label=" COUNT")
except: pass

try: AghemClause.add_node("order", "")
except: pass
try: AghemClause.add_node("count6-a1", "")
except: pass

try: AghemClause.add_edge(("order", "count6-a1"), label=" COUNT")
except: pass

try: AghemClause.add_node("open-a1", "")
except: pass
try: AghemClause.add_node("coherent-a1", "")
except: pass

try: AghemClause.add_edge(("open-a1", "coherent-a1"), label=" COHERENCE")
except: pass

try: AghemClause.add_node("component-a6", "")
except: pass
try: AghemClause.add_node("elastic-a3", "")
except: pass

try: AghemClause.add_edge(("component-a6", "elastic-a3"), label=" ELASTICITY")
except: pass

try: AghemClause.add_node("restkomponentenSet", "")
except: pass
try: AghemClause.add_node("component-a2", "")
except: pass

try: AghemClause.add_edge(("restkomponentenSet", "component-a2"), label=" RESTKOMPONENT")
except: pass

try: AghemClause.add_node("desmeme", "")
except: pass
try: AghemClause.add_node("constructionalConditioning", "")
except: pass

try: AghemClause.add_edge(("desmeme", "constructionalConditioning"), label=" CONDITIONING")
except: pass

try: AghemClause.add_node("elastic-a1", "")
except: pass
try: AghemClause.add_node("maximum1-a1", "")
except: pass

try: AghemClause.add_edge(("elastic-a1", "maximum1-a1"), label=" MAXIMUM")
except: pass

try: AghemClause.add_node("open-a5", "")
except: pass
try: AghemClause.add_node("coherent-a5", "")
except: pass

try: AghemClause.add_edge(("open-a5", "coherent-a5"), label=" COHERENCE")
except: pass

try: AghemClause.add_node("component-a1", "")
except: pass
try: AghemClause.add_node("open-a1", "")
except: pass

try: AghemClause.add_edge(("component-a1", "open-a1"), label=" FILLEDNESS")
except: pass

try: AghemClause.add_node("desmeme", "")
except: pass
try: AghemClause.add_node("arch", "")
except: pass

try: AghemClause.add_edge(("desmeme", "arch"), label=" FOUNDATION")
except: pass

try: AghemClause.add_node("arch", "")
except: pass
try: AghemClause.add_node("component-a5", "")
except: pass

try: AghemClause.add_edge(("arch", "component-a5"), label=" KEYSTONE")
except: pass

try: AghemClause.add_node("open-a6", "")
except: pass
try: AghemClause.add_node("coherent-a6", "")
except: pass

try: AghemClause.add_edge(("open-a6", "coherent-a6"), label=" COHERENCE")
except: pass

try: AghemClause.add_node("component-a5", "")
except: pass
try: AghemClause.add_node("open-a5", "")
except: pass

try: AghemClause.add_edge(("component-a5", "open-a5"), label=" FILLEDNESS")
except: pass

try: AghemClause.add_node("elastic-a3", "")
except: pass
try: AghemClause.add_node("maximum100-a2", "")
except: pass

try: AghemClause.add_edge(("elastic-a3", "maximum100-a2"), label=" MAXIMUM")
except: pass

try: AghemClause.add_node("arch", "")
except: pass
try: AghemClause.add_node("component-a3", "")
except: pass

try: AghemClause.add_edge(("arch", "component-a3"), label=" LEFT_VOUSSOIR")
except: pass

try: AghemClause.add_node("arch", "")
except: pass
try: AghemClause.add_node("component-a1", "")
except: pass

try: AghemClause.add_edge(("arch", "component-a1"), label=" LEFT_SUPPORT")
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
draw_graphs([pcgweighted, pcglabels, AghemClause, MandeClause], pcgfolder)
