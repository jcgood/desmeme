from pygraph.classes.digraph import digraph
from pygraph.readwrite.markup import write
import pydot

import tdag

gr = tdag.tdag("")

try: gr.add_node("stable3/stable4", "")
except: pass
try: gr.add_node("component3/component5", "")
except: pass

gr.add_edge(("stable3/stable4", "component3/component5"), label="STABILITY")

try: gr.add_node("component1/component5", "")
except: pass
try: gr.add_node("inelastic1/elastic4", "")
except: pass

gr.add_edge(("component1/component5", "inelastic1/elastic4"), label="ELASTICITY")

try: gr.add_node("component3/component1", "")
except: pass
try: gr.add_node("filled1/open1", "")
except: pass

gr.add_edge(("component3/component1", "filled1/open1"), label="FILLEDNESS")

try: gr.add_node("component2/component3", "")
except: pass
try: gr.add_node("null1/open3", "")
except: pass

gr.add_edge(("component2/component3", "null1/open3"), label="FILLEDNESS")

try: gr.add_node("MINIMUM0-1/MINIMUM0-3", "")
except: pass
try: gr.add_node("elastic1/elastic3", "")
except: pass

gr.add_edge(("MINIMUM0-1/MINIMUM0-3", "elastic1/elastic3"), label="MINIMUM")

try: gr.add_node("component1/component4", "")
except: pass
try: gr.add_node("open1/open4", "")
except: pass

gr.add_edge(("component1/component4", "open1/open4"), label="FILLEDNESS")

try: gr.add_node("component3/component1", "")
except: pass
try: gr.add_node("elastic1/elastic1", "")
except: pass

gr.add_edge(("component3/component1", "elastic1/elastic1"), label="ELASTICITY")

try: gr.add_node("null1/open2", "")
except: pass
try: gr.add_node("component2/component2", "")
except: pass

gr.add_edge(("null1/open2", "component2/component2"), label="FILLEDNESS")

try: gr.add_node("component3/component4", "")
except: pass
try: gr.add_node("elastic1/elastic3", "")
except: pass

gr.add_edge(("component3/component4", "elastic1/elastic3"), label="ELASTICITY")

try: gr.add_node("component2/component3", "")
except: pass
try: gr.add_node("inelastic2/elastic2", "")
except: pass

gr.add_edge(("component2/component3", "inelastic2/elastic2"), label="ELASTICITY")

try: gr.add_node("COUNT0-1/COUNT1-1", "")
except: pass
try: gr.add_node("inelastic2/inelastic1", "")
except: pass

gr.add_edge(("COUNT0-1/COUNT1-1", "inelastic2/inelastic1"), label="COUNT")

try: gr.add_node("desmeme/desmeme", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

gr.add_edge(("desmeme/desmeme", "arch/arch"), label="FOUNDATION")

try: gr.add_node("elastic2/elastic3", "")
except: pass
try: gr.add_node("component4/component4", "")
except: pass

gr.add_edge(("elastic2/elastic3", "component4/component4"), label="ELASTICITY")

try: gr.add_node("open1/open2", "")
except: pass
try: gr.add_node("coherent1/coherent2", "")
except: pass

gr.add_edge(("open1/open2", "coherent1/coherent2"), label="COHERENCE")

try: gr.add_node("stable2/stable3", "")
except: pass
try: gr.add_node("component2/component4", "")
except: pass

gr.add_edge(("stable2/stable3", "component2/component4"), label="STABILITY")

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("component3/component5", "")
except: pass

gr.add_edge(("arch/arch", "component3/component5"), label="RIGHT_VOUSSOIR")

try: gr.add_node("filled1/open2", "")
except: pass
try: gr.add_node("component3/component2", "")
except: pass

gr.add_edge(("filled1/open2", "component3/component2"), label="FILLEDNESS")

try: gr.add_node("COUNT2-1/COUNT5-1", "")
except: pass
try: gr.add_node("order/order", "")
except: pass

gr.add_edge(("COUNT2-1/COUNT5-1", "order/order"), label="COUNT")

try: gr.add_node("component3/component2", "")
except: pass
try: gr.add_node("elastic1/inelastic1", "")
except: pass

gr.add_edge(("component3/component2", "elastic1/inelastic1"), label="ELASTICITY")

try: gr.add_node("stable2/unstable1", "")
except: pass
try: gr.add_node("component2/component1", "")
except: pass

gr.add_edge(("stable2/unstable1", "component2/component1"), label="STABILITY")

try: gr.add_node("filled2/open3", "")
except: pass
try: gr.add_node("component4/component3", "")
except: pass

gr.add_edge(("filled2/open3", "component4/component3"), label="FILLEDNESS")

try: gr.add_node("stable4/stable3", "")
except: pass
try: gr.add_node("component4/component4", "")
except: pass

gr.add_edge(("stable4/stable3", "component4/component4"), label="STABILITY")

try: gr.add_node("filled1/open3", "")
except: pass
try: gr.add_node("component3/component3", "")
except: pass

gr.add_edge(("filled1/open3", "component3/component3"), label="FILLEDNESS")

try: gr.add_node("MAXIMUM1-2/MAXIMUM100-1", "")
except: pass
try: gr.add_node("elastic2/elastic4", "")
except: pass

gr.add_edge(("MAXIMUM1-2/MAXIMUM100-1", "elastic2/elastic4"), label="MAXIMUM")

try: gr.add_node("component4/component3", "")
except: pass
try: gr.add_node("stable4/stable2", "")
except: pass

gr.add_edge(("component4/component3", "stable4/stable2"), label="STABILITY")

try: gr.add_node("elastic2/inelastic1", "")
except: pass
try: gr.add_node("component4/component2", "")
except: pass

gr.add_edge(("elastic2/inelastic1", "component4/component2"), label="ELASTICITY")

try: gr.add_node("inelastic1/elastic2", "")
except: pass
try: gr.add_node("component1/component3", "")
except: pass

gr.add_edge(("inelastic1/elastic2", "component1/component3"), label="ELASTICITY")

try: gr.add_node("morphologicalConstituent/syntacticConstituent", "")
except: pass
try: gr.add_node("order/order", "")
except: pass

gr.add_edge(("morphologicalConstituent/syntacticConstituent", "order/order"), label="CONSTITUENT")

try: gr.add_node("elastic2/elastic3", "")
except: pass
try: gr.add_node("MINIMUM0-2/MINIMUM0-3", "")
except: pass

gr.add_edge(("elastic2/elastic3", "MINIMUM0-2/MINIMUM0-3"), label="MINIMUM")

try: gr.add_node("filled1/open4", "")
except: pass
try: gr.add_node("component3/component4", "")
except: pass

gr.add_edge(("filled1/open4", "component3/component4"), label="FILLEDNESS")

try: gr.add_node("component4/component5", "")
except: pass
try: gr.add_node("filled2/open5", "")
except: pass

gr.add_edge(("component4/component5", "filled2/open5"), label="FILLEDNESS")

try: gr.add_node("stable2/stable4", "")
except: pass
try: gr.add_node("component2/component5", "")
except: pass

gr.add_edge(("stable2/stable4", "component2/component5"), label="STABILITY")

try: gr.add_node("lexicoconstructionalConditioning/constructionalConditioning", "")
except: pass
try: gr.add_node("desmeme/desmeme", "")
except: pass

gr.add_edge(("lexicoconstructionalConditioning/constructionalConditioning", "desmeme/desmeme"), label="CONDITIONING")

try: gr.add_node("elastic2/elastic1", "")
except: pass
try: gr.add_node("component4/component1", "")
except: pass

gr.add_edge(("elastic2/elastic1", "component4/component1"), label="ELASTICITY")

try: gr.add_node("component1/component3", "")
except: pass
try: gr.add_node("stable1/stable2", "")
except: pass

gr.add_edge(("component1/component3", "stable1/stable2"), label="STABILITY")

try: gr.add_node("component4/component2", "")
except: pass
try: gr.add_node("filled2/open2", "")
except: pass

gr.add_edge(("component4/component2", "filled2/open2"), label="FILLEDNESS")

try: gr.add_node("order/inelastic1", "")
except: pass
try: gr.add_node("COUNT2-1/COUNT1-1", "")
except: pass

gr.add_edge(("order/inelastic1", "COUNT2-1/COUNT1-1"), label="COUNT")

try: gr.add_node("stable4/unstable1", "")
except: pass
try: gr.add_node("component4/component1", "")
except: pass

gr.add_edge(("stable4/unstable1", "component4/component1"), label="STABILITY")

try: gr.add_node("elastic1/elastic2", "")
except: pass
try: gr.add_node("component3/component3", "")
except: pass

gr.add_edge(("elastic1/elastic2", "component3/component3"), label="ELASTICITY")

try: gr.add_node("stable1/stable4", "")
except: pass
try: gr.add_node("component1/component5", "")
except: pass

gr.add_edge(("stable1/stable4", "component1/component5"), label="STABILITY")

try: gr.add_node("MINIMUM0-2/MINIMUM0-1", "")
except: pass
try: gr.add_node("elastic2/elastic1", "")
except: pass

gr.add_edge(("MINIMUM0-2/MINIMUM0-1", "elastic2/elastic1"), label="MINIMUM")

try: gr.add_node("inelastic1/order", "")
except: pass
try: gr.add_node("COUNT1-1/COUNT5-1", "")
except: pass

gr.add_edge(("inelastic1/order", "COUNT1-1/COUNT5-1"), label="COUNT")

try: gr.add_node("open1/open1", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("open1/open1", "component1/component1"), label="FILLEDNESS")

try: gr.add_node("MINIMUM0-1/MINIMUM0-1", "")
except: pass
try: gr.add_node("elastic1/elastic1", "")
except: pass

gr.add_edge(("MINIMUM0-1/MINIMUM0-1", "elastic1/elastic1"), label="MINIMUM")

try: gr.add_node("component3/component5", "")
except: pass
try: gr.add_node("filled1/open5", "")
except: pass

gr.add_edge(("component3/component5", "filled1/open5"), label="FILLEDNESS")

try: gr.add_node("elastic2/elastic4", "")
except: pass
try: gr.add_node("MINIMUM0-2/MINIMUM0-4", "")
except: pass

gr.add_edge(("elastic2/elastic4", "MINIMUM0-2/MINIMUM0-4"), label="MINIMUM")

try: gr.add_node("inelastic1/inelastic1", "")
except: pass
try: gr.add_node("COUNT1-1/COUNT1-1", "")
except: pass

gr.add_edge(("inelastic1/inelastic1", "COUNT1-1/COUNT1-1"), label="COUNT")

try: gr.add_node("component2/component4", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

gr.add_edge(("component2/component4", "arch/arch"), label="LEFT_VOUSSOIR")

try: gr.add_node("stable2/stable1", "")
except: pass
try: gr.add_node("component2/component2", "")
except: pass

gr.add_edge(("stable2/stable1", "component2/component2"), label="STABILITY")

try: gr.add_node("stable1/stable2", "")
except: pass
try: gr.add_node("component1/component3", "")
except: pass

gr.add_edge(("stable1/stable2", "component1/component3"), label="STABILITY")

try: gr.add_node("stable3/stable2", "")
except: pass
try: gr.add_node("component3/component3", "")
except: pass

gr.add_edge(("stable3/stable2", "component3/component3"), label="STABILITY")

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("component4/component5", "")
except: pass

gr.add_edge(("arch/arch", "component4/component5"), label="RIGHT_SUPPORT")

try: gr.add_node("elastic1/elastic3", "")
except: pass
try: gr.add_node("component3/component4", "")
except: pass

gr.add_edge(("elastic1/elastic3", "component3/component4"), label="ELASTICITY")

try: gr.add_node("open1/open3", "")
except: pass
try: gr.add_node("coherent1/coherent3", "")
except: pass

gr.add_edge(("open1/open3", "coherent1/coherent3"), label="COHERENCE")

try: gr.add_node("component4/component1", "")
except: pass
try: gr.add_node("filled2/open1", "")
except: pass

gr.add_edge(("component4/component1", "filled2/open1"), label="FILLEDNESS")

try: gr.add_node("elastic2/elastic2", "")
except: pass
try: gr.add_node("MINIMUM0-2/MINIMUM0-2", "")
except: pass

gr.add_edge(("elastic2/elastic2", "MINIMUM0-2/MINIMUM0-2"), label="MINIMUM")

try: gr.add_node("stable4/stable4", "")
except: pass
try: gr.add_node("component4/component5", "")
except: pass

gr.add_edge(("stable4/stable4", "component4/component5"), label="STABILITY")

try: gr.add_node("elastic1/elastic3", "")
except: pass
try: gr.add_node("MAXIMUM1-1/MAXIMUM1-3", "")
except: pass

gr.add_edge(("elastic1/elastic3", "MAXIMUM1-1/MAXIMUM1-3"), label="MAXIMUM")

try: gr.add_node("open1/open1", "")
except: pass
try: gr.add_node("coherent1/coherent1", "")
except: pass

gr.add_edge(("open1/open1", "coherent1/coherent1"), label="COHERENCE")

try: gr.add_node("stable3/stable1", "")
except: pass
try: gr.add_node("component3/component2", "")
except: pass

gr.add_edge(("stable3/stable1", "component3/component2"), label="STABILITY")

try: gr.add_node("component3/component3", "")
except: pass
try: gr.add_node("elastic1/elastic2", "")
except: pass

gr.add_edge(("component3/component3", "elastic1/elastic2"), label="ELASTICITY")

try: gr.add_node("component4/component4", "")
except: pass
try: gr.add_node("filled2/open4", "")
except: pass

gr.add_edge(("component4/component4", "filled2/open4"), label="FILLEDNESS")

try: gr.add_node("MINIMUM0-1/MINIMUM0-4", "")
except: pass
try: gr.add_node("elastic1/elastic4", "")
except: pass

gr.add_edge(("MINIMUM0-1/MINIMUM0-4", "elastic1/elastic4"), label="MINIMUM")

try: gr.add_node("coherent1/coherent2", "")
except: pass
try: gr.add_node("open1/open2", "")
except: pass

gr.add_edge(("coherent1/coherent2", "open1/open2"), label="COHERENCE")

try: gr.add_node("elastic1/elastic2", "")
except: pass
try: gr.add_node("MAXIMUM1-1/MAXIMUM1-2", "")
except: pass

gr.add_edge(("elastic1/elastic2", "MAXIMUM1-1/MAXIMUM1-2"), label="MAXIMUM")

try: gr.add_node("stable1/stable1", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

gr.add_edge(("stable1/stable1", "component1/component2"), label="STABILITY")

try: gr.add_node("inelastic2/elastic1", "")
except: pass
try: gr.add_node("component2/component1", "")
except: pass

gr.add_edge(("inelastic2/elastic1", "component2/component1"), label="ELASTICITY")

try: gr.add_node("elastic2/elastic1", "")
except: pass
try: gr.add_node("MAXIMUM1-2/MAXIMUM1-1", "")
except: pass

gr.add_edge(("elastic2/elastic1", "MAXIMUM1-2/MAXIMUM1-1"), label="MAXIMUM")

try: gr.add_node("component4/component3", "")
except: pass
try: gr.add_node("elastic2/elastic2", "")
except: pass

gr.add_edge(("component4/component3", "elastic2/elastic2"), label="ELASTICITY")

try: gr.add_node("coherent1/coherent3", "")
except: pass
try: gr.add_node("open1/open3", "")
except: pass

gr.add_edge(("coherent1/coherent3", "open1/open3"), label="COHERENCE")

try: gr.add_node("component1/component4", "")
except: pass
try: gr.add_node("stable1/stable3", "")
except: pass

gr.add_edge(("component1/component4", "stable1/stable3"), label="STABILITY")

try: gr.add_node("component2/component2", "")
except: pass
try: gr.add_node("null1/open2", "")
except: pass

gr.add_edge(("component2/component2", "null1/open2"), label="FILLEDNESS")

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("open1/open2", "")
except: pass

gr.add_edge(("component1/component2", "open1/open2"), label="FILLEDNESS")

try: gr.add_node("stable3/stable3", "")
except: pass
try: gr.add_node("component3/component4", "")
except: pass

gr.add_edge(("stable3/stable3", "component3/component4"), label="STABILITY")

try: gr.add_node("MAXIMUM1-2/MAXIMUM1-2", "")
except: pass
try: gr.add_node("elastic2/elastic2", "")
except: pass

gr.add_edge(("MAXIMUM1-2/MAXIMUM1-2", "elastic2/elastic2"), label="MAXIMUM")

try: gr.add_node("null1/open1", "")
except: pass
try: gr.add_node("component2/component1", "")
except: pass

gr.add_edge(("null1/open1", "component2/component1"), label="FILLEDNESS")

try: gr.add_node("MINIMUM0-2/MINIMUM0-3", "")
except: pass
try: gr.add_node("elastic2/elastic3", "")
except: pass

gr.add_edge(("MINIMUM0-2/MINIMUM0-3", "elastic2/elastic3"), label="MINIMUM")

try: gr.add_node("component4/component2", "")
except: pass
try: gr.add_node("stable4/stable1", "")
except: pass

gr.add_edge(("component4/component2", "stable4/stable1"), label="STABILITY")

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("arch/arch", "component1/component1"), label="LEFT_SUPPORT")

try: gr.add_node("elastic2/elastic4", "")
except: pass
try: gr.add_node("component4/component5", "")
except: pass

gr.add_edge(("elastic2/elastic4", "component4/component5"), label="ELASTICITY")

try: gr.add_node("component1/component5", "")
except: pass
try: gr.add_node("open1/open5", "")
except: pass

gr.add_edge(("component1/component5", "open1/open5"), label="FILLEDNESS")

try: gr.add_node("component3/component5", "")
except: pass
try: gr.add_node("stable3/stable4", "")
except: pass

gr.add_edge(("component3/component5", "stable3/stable4"), label="STABILITY")

try: gr.add_node("stable2/stable2", "")
except: pass
try: gr.add_node("component2/component3", "")
except: pass

gr.add_edge(("stable2/stable2", "component2/component3"), label="STABILITY")

try: gr.add_node("component2/component4", "")
except: pass
try: gr.add_node("stable2/stable3", "")
except: pass

gr.add_edge(("component2/component4", "stable2/stable3"), label="STABILITY")

try: gr.add_node("elastic2/elastic3", "")
except: pass
try: gr.add_node("MAXIMUM1-2/MAXIMUM1-3", "")
except: pass

gr.add_edge(("elastic2/elastic3", "MAXIMUM1-2/MAXIMUM1-3"), label="MAXIMUM")

try: gr.add_node("inelastic2/elastic3", "")
except: pass
try: gr.add_node("component2/component4", "")
except: pass

gr.add_edge(("inelastic2/elastic3", "component2/component4"), label="ELASTICITY")

try: gr.add_node("order/order", "")
except: pass
try: gr.add_node("simple/simple", "")
except: pass

gr.add_edge(("order/order", "simple/simple"), label="RELATIONS")

try: gr.add_node("component1/component3", "")
except: pass
try: gr.add_node("open1/open3", "")
except: pass

gr.add_edge(("component1/component3", "open1/open3"), label="FILLEDNESS")

try: gr.add_node("inelastic1/elastic3", "")
except: pass
try: gr.add_node("component1/component4", "")
except: pass

gr.add_edge(("inelastic1/elastic3", "component1/component4"), label="ELASTICITY")

try: gr.add_node("null1/open5", "")
except: pass
try: gr.add_node("component2/component5", "")
except: pass

gr.add_edge(("null1/open5", "component2/component5"), label="FILLEDNESS")

try: gr.add_node("inelastic2/elastic4", "")
except: pass
try: gr.add_node("component2/component5", "")
except: pass

gr.add_edge(("inelastic2/elastic4", "component2/component5"), label="ELASTICITY")

try: gr.add_node("component3/component5", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

gr.add_edge(("component3/component5", "arch/arch"), label="RIGHT_VOUSSOIR")

try: gr.add_node("order/order", "")
except: pass
try: gr.add_node("desmeme/desmeme", "")
except: pass

gr.add_edge(("order/order", "desmeme/desmeme"), label="STRICTURE")

try: gr.add_node("elastic1/elastic1", "")
except: pass
try: gr.add_node("MAXIMUM1-1/MAXIMUM1-1", "")
except: pass

gr.add_edge(("elastic1/elastic1", "MAXIMUM1-1/MAXIMUM1-1"), label="MAXIMUM")

try: gr.add_node("inelastic1/elastic4", "")
except: pass
try: gr.add_node("component1/component5", "")
except: pass

gr.add_edge(("inelastic1/elastic4", "component1/component5"), label="ELASTICITY")

try: gr.add_node("elastic1/inelastic1", "")
except: pass
try: gr.add_node("component3/component2", "")
except: pass

gr.add_edge(("elastic1/inelastic1", "component3/component2"), label="ELASTICITY")

try: gr.add_node("COUNT1-1/COUNT1-1", "")
except: pass
try: gr.add_node("inelastic1/inelastic1", "")
except: pass

gr.add_edge(("COUNT1-1/COUNT1-1", "inelastic1/inelastic1"), label="COUNT")

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

gr.add_edge(("component1/component2", "arch/arch"), label="KEYSTONE")

try: gr.add_node("component4/component4", "")
except: pass
try: gr.add_node("elastic2/elastic3", "")
except: pass

gr.add_edge(("component4/component4", "elastic2/elastic3"), label="ELASTICITY")

try: gr.add_node("elastic2/elastic1", "")
except: pass
try: gr.add_node("MINIMUM0-2/MINIMUM0-1", "")
except: pass

gr.add_edge(("elastic2/elastic1", "MINIMUM0-2/MINIMUM0-1"), label="MINIMUM")

try: gr.add_node("coherent1/coherent4", "")
except: pass
try: gr.add_node("open1/open4", "")
except: pass

gr.add_edge(("coherent1/coherent4", "open1/open4"), label="COHERENCE")

try: gr.add_node("null1/open3", "")
except: pass
try: gr.add_node("component2/component3", "")
except: pass

gr.add_edge(("null1/open3", "component2/component3"), label="FILLEDNESS")

try: gr.add_node("elastic2/elastic2", "")
except: pass
try: gr.add_node("MAXIMUM1-2/MAXIMUM1-2", "")
except: pass

gr.add_edge(("elastic2/elastic2", "MAXIMUM1-2/MAXIMUM1-2"), label="MAXIMUM")

try: gr.add_node("open1/open3", "")
except: pass
try: gr.add_node("component1/component3", "")
except: pass

gr.add_edge(("open1/open3", "component1/component3"), label="FILLEDNESS")

try: gr.add_node("MAXIMUM1-2/MAXIMUM1-1", "")
except: pass
try: gr.add_node("elastic2/elastic1", "")
except: pass

gr.add_edge(("MAXIMUM1-2/MAXIMUM1-1", "elastic2/elastic1"), label="MAXIMUM")

try: gr.add_node("component2/component1", "")
except: pass
try: gr.add_node("stable2/unstable1", "")
except: pass

gr.add_edge(("component2/component1", "stable2/unstable1"), label="STABILITY")

try: gr.add_node("elastic1/elastic1", "")
except: pass
try: gr.add_node("MINIMUM0-1/MINIMUM0-1", "")
except: pass

gr.add_edge(("elastic1/elastic1", "MINIMUM0-1/MINIMUM0-1"), label="MINIMUM")

try: gr.add_node("elastic1/elastic2", "")
except: pass
try: gr.add_node("MINIMUM0-1/MINIMUM0-2", "")
except: pass

gr.add_edge(("elastic1/elastic2", "MINIMUM0-1/MINIMUM0-2"), label="MINIMUM")

try: gr.add_node("desmeme/desmeme", "")
except: pass
try: gr.add_node("potentiallyViolable/notViolable", "")
except: pass

gr.add_edge(("desmeme/desmeme", "potentiallyViolable/notViolable"), label="VIOLABILITY")

try: gr.add_node("COUNT1-1/COUNT5-1", "")
except: pass
try: gr.add_node("inelastic1/order", "")
except: pass

gr.add_edge(("COUNT1-1/COUNT5-1", "inelastic1/order"), label="COUNT")

try: gr.add_node("component4/component3", "")
except: pass
try: gr.add_node("filled2/open3", "")
except: pass

gr.add_edge(("component4/component3", "filled2/open3"), label="FILLEDNESS")

try: gr.add_node("filled2/open2", "")
except: pass
try: gr.add_node("component4/component2", "")
except: pass

gr.add_edge(("filled2/open2", "component4/component2"), label="FILLEDNESS")

try: gr.add_node("component3/component4", "")
except: pass
try: gr.add_node("filled1/open4", "")
except: pass

gr.add_edge(("component3/component4", "filled1/open4"), label="FILLEDNESS")

try: gr.add_node("open1/open4", "")
except: pass
try: gr.add_node("component1/component4", "")
except: pass

gr.add_edge(("open1/open4", "component1/component4"), label="FILLEDNESS")

try: gr.add_node("order/order", "")
except: pass
try: gr.add_node("morphologicalConstituent/syntacticConstituent", "")
except: pass

gr.add_edge(("order/order", "morphologicalConstituent/syntacticConstituent"), label="CONSTITUENT")

try: gr.add_node("filled2/open4", "")
except: pass
try: gr.add_node("component4/component4", "")
except: pass

gr.add_edge(("filled2/open4", "component4/component4"), label="FILLEDNESS")

try: gr.add_node("component4/component1", "")
except: pass
try: gr.add_node("stable4/unstable1", "")
except: pass

gr.add_edge(("component4/component1", "stable4/unstable1"), label="STABILITY")

try: gr.add_node("coherent1/coherent5", "")
except: pass
try: gr.add_node("open1/open5", "")
except: pass

gr.add_edge(("coherent1/coherent5", "open1/open5"), label="COHERENCE")

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("stable1/unstable1", "")
except: pass

gr.add_edge(("component1/component1", "stable1/unstable1"), label="STABILITY")

try: gr.add_node("filled1/open1", "")
except: pass
try: gr.add_node("component3/component1", "")
except: pass

gr.add_edge(("filled1/open1", "component3/component1"), label="FILLEDNESS")

try: gr.add_node("MAXIMUM1-1/MAXIMUM100-1", "")
except: pass
try: gr.add_node("elastic1/elastic4", "")
except: pass

gr.add_edge(("MAXIMUM1-1/MAXIMUM100-1", "elastic1/elastic4"), label="MAXIMUM")

try: gr.add_node("component2/component1", "")
except: pass
try: gr.add_node("inelastic2/elastic1", "")
except: pass

gr.add_edge(("component2/component1", "inelastic2/elastic1"), label="ELASTICITY")

try: gr.add_node("filled2/open5", "")
except: pass
try: gr.add_node("component4/component5", "")
except: pass

gr.add_edge(("filled2/open5", "component4/component5"), label="FILLEDNESS")

try: gr.add_node("filled1/open5", "")
except: pass
try: gr.add_node("component3/component5", "")
except: pass

gr.add_edge(("filled1/open5", "component3/component5"), label="FILLEDNESS")

try: gr.add_node("elastic2/elastic4", "")
except: pass
try: gr.add_node("MAXIMUM1-2/MAXIMUM100-1", "")
except: pass

gr.add_edge(("elastic2/elastic4", "MAXIMUM1-2/MAXIMUM100-1"), label="MAXIMUM")

try: gr.add_node("MINIMUM0-2/MINIMUM0-4", "")
except: pass
try: gr.add_node("elastic2/elastic4", "")
except: pass

gr.add_edge(("MINIMUM0-2/MINIMUM0-4", "elastic2/elastic4"), label="MINIMUM")

try: gr.add_node("stable3/unstable1", "")
except: pass
try: gr.add_node("component3/component1", "")
except: pass

gr.add_edge(("stable3/unstable1", "component3/component1"), label="STABILITY")

try: gr.add_node("stable4/stable2", "")
except: pass
try: gr.add_node("component4/component3", "")
except: pass

gr.add_edge(("stable4/stable2", "component4/component3"), label="STABILITY")

try: gr.add_node("null1/open4", "")
except: pass
try: gr.add_node("component2/component4", "")
except: pass

gr.add_edge(("null1/open4", "component2/component4"), label="FILLEDNESS")

try: gr.add_node("component2/component2", "")
except: pass
try: gr.add_node("inelastic2/inelastic1", "")
except: pass

gr.add_edge(("component2/component2", "inelastic2/inelastic1"), label="ELASTICITY")

try: gr.add_node("inelastic1/elastic1", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("inelastic1/elastic1", "component1/component1"), label="ELASTICITY")

try: gr.add_node("desmeme/desmeme", "")
except: pass
try: gr.add_node("lexicoconstructionalConditioning/constructionalConditioning", "")
except: pass

gr.add_edge(("desmeme/desmeme", "lexicoconstructionalConditioning/constructionalConditioning"), label="CONDITIONING")

try: gr.add_node("open1/open5", "")
except: pass
try: gr.add_node("component1/component5", "")
except: pass

gr.add_edge(("open1/open5", "component1/component5"), label="FILLEDNESS")

try: gr.add_node("component3/component5", "")
except: pass
try: gr.add_node("elastic1/elastic4", "")
except: pass

gr.add_edge(("component3/component5", "elastic1/elastic4"), label="ELASTICITY")

try: gr.add_node("inelastic1/inelastic1", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

gr.add_edge(("inelastic1/inelastic1", "component1/component2"), label="ELASTICITY")

try: gr.add_node("inelastic2/order", "")
except: pass
try: gr.add_node("COUNT0-1/COUNT5-1", "")
except: pass

gr.add_edge(("inelastic2/order", "COUNT0-1/COUNT5-1"), label="COUNT")

try: gr.add_node("MAXIMUM1-1/MAXIMUM1-2", "")
except: pass
try: gr.add_node("elastic1/elastic2", "")
except: pass

gr.add_edge(("MAXIMUM1-1/MAXIMUM1-2", "elastic1/elastic2"), label="MAXIMUM")

try: gr.add_node("order/order", "")
except: pass
try: gr.add_node("COUNT2-1/COUNT5-1", "")
except: pass

gr.add_edge(("order/order", "COUNT2-1/COUNT5-1"), label="COUNT")

try: gr.add_node("inelastic2/elastic2", "")
except: pass
try: gr.add_node("component2/component3", "")
except: pass

gr.add_edge(("inelastic2/elastic2", "component2/component3"), label="ELASTICITY")

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("component2/component4", "")
except: pass

gr.add_edge(("arch/arch", "component2/component4"), label="LEFT_VOUSSOIR")

try: gr.add_node("elastic1/elastic1", "")
except: pass
try: gr.add_node("component3/component1", "")
except: pass

gr.add_edge(("elastic1/elastic1", "component3/component1"), label="ELASTICITY")

try: gr.add_node("inelastic2/inelastic1", "")
except: pass
try: gr.add_node("COUNT0-1/COUNT1-1", "")
except: pass

gr.add_edge(("inelastic2/inelastic1", "COUNT0-1/COUNT1-1"), label="COUNT")

try: gr.add_node("elastic1/elastic3", "")
except: pass
try: gr.add_node("MINIMUM0-1/MINIMUM0-3", "")
except: pass

gr.add_edge(("elastic1/elastic3", "MINIMUM0-1/MINIMUM0-3"), label="MINIMUM")

try: gr.add_node("open1/open5", "")
except: pass
try: gr.add_node("coherent1/coherent5", "")
except: pass

gr.add_edge(("open1/open5", "coherent1/coherent5"), label="COHERENCE")

try: gr.add_node("elastic1/elastic4", "")
except: pass
try: gr.add_node("MINIMUM0-1/MINIMUM0-4", "")
except: pass

gr.add_edge(("elastic1/elastic4", "MINIMUM0-1/MINIMUM0-4"), label="MINIMUM")

try: gr.add_node("elastic1/elastic4", "")
except: pass
try: gr.add_node("MAXIMUM1-1/MAXIMUM100-1", "")
except: pass

gr.add_edge(("elastic1/elastic4", "MAXIMUM1-1/MAXIMUM100-1"), label="MAXIMUM")

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

gr.add_edge(("component1/component1", "arch/arch"), label="LEFT_SUPPORT")

try: gr.add_node("component1/component5", "")
except: pass
try: gr.add_node("stable1/stable4", "")
except: pass

gr.add_edge(("component1/component5", "stable1/stable4"), label="STABILITY")

try: gr.add_node("component3/component3", "")
except: pass
try: gr.add_node("filled1/open3", "")
except: pass

gr.add_edge(("component3/component3", "filled1/open3"), label="FILLEDNESS")

try: gr.add_node("component2/component5", "")
except: pass
try: gr.add_node("null1/open5", "")
except: pass

gr.add_edge(("component2/component5", "null1/open5"), label="FILLEDNESS")

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("stable1/stable1", "")
except: pass

gr.add_edge(("component1/component2", "stable1/stable1"), label="STABILITY")

try: gr.add_node("stable1/stable3", "")
except: pass
try: gr.add_node("component1/component4", "")
except: pass

gr.add_edge(("stable1/stable3", "component1/component4"), label="STABILITY")

try: gr.add_node("component4/component2", "")
except: pass
try: gr.add_node("elastic2/inelastic1", "")
except: pass

gr.add_edge(("component4/component2", "elastic2/inelastic1"), label="ELASTICITY")

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("open1/open1", "")
except: pass

gr.add_edge(("component1/component1", "open1/open1"), label="FILLEDNESS")

try: gr.add_node("component3/component3", "")
except: pass
try: gr.add_node("stable3/stable2", "")
except: pass

gr.add_edge(("component3/component3", "stable3/stable2"), label="STABILITY")

try: gr.add_node("elastic2/elastic2", "")
except: pass
try: gr.add_node("component4/component3", "")
except: pass

gr.add_edge(("elastic2/elastic2", "component4/component3"), label="ELASTICITY")

try: gr.add_node("component4/component1", "")
except: pass
try: gr.add_node("elastic2/elastic1", "")
except: pass

gr.add_edge(("component4/component1", "elastic2/elastic1"), label="ELASTICITY")

try: gr.add_node("component2/component1", "")
except: pass
try: gr.add_node("null1/open1", "")
except: pass

gr.add_edge(("component2/component1", "null1/open1"), label="FILLEDNESS")

try: gr.add_node("component2/component5", "")
except: pass
try: gr.add_node("stable2/stable4", "")
except: pass

gr.add_edge(("component2/component5", "stable2/stable4"), label="STABILITY")

try: gr.add_node("component3/component2", "")
except: pass
try: gr.add_node("stable3/stable1", "")
except: pass

gr.add_edge(("component3/component2", "stable3/stable1"), label="STABILITY")

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("inelastic1/inelastic1", "")
except: pass

gr.add_edge(("component1/component2", "inelastic1/inelastic1"), label="ELASTICITY")

try: gr.add_node("MINIMUM0-1/MINIMUM0-2", "")
except: pass
try: gr.add_node("elastic1/elastic2", "")
except: pass

gr.add_edge(("MINIMUM0-1/MINIMUM0-2", "elastic1/elastic2"), label="MINIMUM")

try: gr.add_node("MINIMUM0-2/MINIMUM0-2", "")
except: pass
try: gr.add_node("elastic2/elastic2", "")
except: pass

gr.add_edge(("MINIMUM0-2/MINIMUM0-2", "elastic2/elastic2"), label="MINIMUM")

try: gr.add_node("open1/open4", "")
except: pass
try: gr.add_node("coherent1/coherent4", "")
except: pass

gr.add_edge(("open1/open4", "coherent1/coherent4"), label="COHERENCE")

try: gr.add_node("COUNT2-1/COUNT1-1", "")
except: pass
try: gr.add_node("order/inelastic1", "")
except: pass

gr.add_edge(("COUNT2-1/COUNT1-1", "order/inelastic1"), label="COUNT")

try: gr.add_node("MAXIMUM1-2/MAXIMUM1-3", "")
except: pass
try: gr.add_node("elastic2/elastic3", "")
except: pass

gr.add_edge(("MAXIMUM1-2/MAXIMUM1-3", "elastic2/elastic3"), label="MAXIMUM")

try: gr.add_node("component4/component4", "")
except: pass
try: gr.add_node("stable4/stable3", "")
except: pass

gr.add_edge(("component4/component4", "stable4/stable3"), label="STABILITY")

try: gr.add_node("stable4/stable1", "")
except: pass
try: gr.add_node("component4/component2", "")
except: pass

gr.add_edge(("stable4/stable1", "component4/component2"), label="STABILITY")

try: gr.add_node("component3/component4", "")
except: pass
try: gr.add_node("stable3/stable3", "")
except: pass

gr.add_edge(("component3/component4", "stable3/stable3"), label="STABILITY")

try: gr.add_node("COUNT0-1/COUNT5-1", "")
except: pass
try: gr.add_node("inelastic2/order", "")
except: pass

gr.add_edge(("COUNT0-1/COUNT5-1", "inelastic2/order"), label="COUNT")

try: gr.add_node("component2/component4", "")
except: pass
try: gr.add_node("null1/open4", "")
except: pass

gr.add_edge(("component2/component4", "null1/open4"), label="FILLEDNESS")

try: gr.add_node("stable1/unstable1", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("stable1/unstable1", "component1/component1"), label="STABILITY")

try: gr.add_node("component2/component3", "")
except: pass
try: gr.add_node("stable2/stable2", "")
except: pass

gr.add_edge(("component2/component3", "stable2/stable2"), label="STABILITY")

try: gr.add_node("component2/component5", "")
except: pass
try: gr.add_node("inelastic2/elastic4", "")
except: pass

gr.add_edge(("component2/component5", "inelastic2/elastic4"), label="ELASTICITY")

try: gr.add_node("component4/component5", "")
except: pass
try: gr.add_node("elastic2/elastic4", "")
except: pass

gr.add_edge(("component4/component5", "elastic2/elastic4"), label="ELASTICITY")

try: gr.add_node("component2/component4", "")
except: pass
try: gr.add_node("inelastic2/elastic3", "")
except: pass

gr.add_edge(("component2/component4", "inelastic2/elastic3"), label="ELASTICITY")

try: gr.add_node("elastic1/elastic4", "")
except: pass
try: gr.add_node("component3/component5", "")
except: pass

gr.add_edge(("elastic1/elastic4", "component3/component5"), label="ELASTICITY")

try: gr.add_node("open1/open2", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

gr.add_edge(("open1/open2", "component1/component2"), label="FILLEDNESS")

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

gr.add_edge(("arch/arch", "component1/component2"), label="KEYSTONE")

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("desmeme/desmeme", "")
except: pass

gr.add_edge(("arch/arch", "desmeme/desmeme"), label="FOUNDATION")

try: gr.add_node("coherent1/coherent1", "")
except: pass
try: gr.add_node("open1/open1", "")
except: pass

gr.add_edge(("coherent1/coherent1", "open1/open1"), label="COHERENCE")

try: gr.add_node("component1/component4", "")
except: pass
try: gr.add_node("inelastic1/elastic3", "")
except: pass

gr.add_edge(("component1/component4", "inelastic1/elastic3"), label="ELASTICITY")

try: gr.add_node("component4/component5", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

gr.add_edge(("component4/component5", "arch/arch"), label="RIGHT_SUPPORT")

try: gr.add_node("potentiallyViolable/notViolable", "")
except: pass
try: gr.add_node("desmeme/desmeme", "")
except: pass

gr.add_edge(("potentiallyViolable/notViolable", "desmeme/desmeme"), label="VIOLABILITY")

try: gr.add_node("component3/component2", "")
except: pass
try: gr.add_node("filled1/open2", "")
except: pass

gr.add_edge(("component3/component2", "filled1/open2"), label="FILLEDNESS")

try: gr.add_node("component4/component5", "")
except: pass
try: gr.add_node("stable4/stable4", "")
except: pass

gr.add_edge(("component4/component5", "stable4/stable4"), label="STABILITY")

try: gr.add_node("inelastic2/inelastic1", "")
except: pass
try: gr.add_node("component2/component2", "")
except: pass

gr.add_edge(("inelastic2/inelastic1", "component2/component2"), label="ELASTICITY")

try: gr.add_node("simple/simple", "")
except: pass
try: gr.add_node("order/order", "")
except: pass

gr.add_edge(("simple/simple", "order/order"), label="RELATIONS")

try: gr.add_node("filled2/open1", "")
except: pass
try: gr.add_node("component4/component1", "")
except: pass

gr.add_edge(("filled2/open1", "component4/component1"), label="FILLEDNESS")

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("inelastic1/elastic1", "")
except: pass

gr.add_edge(("component1/component1", "inelastic1/elastic1"), label="ELASTICITY")

try: gr.add_node("desmeme/desmeme", "")
except: pass
try: gr.add_node("order/order", "")
except: pass

gr.add_edge(("desmeme/desmeme", "order/order"), label="STRICTURE")

try: gr.add_node("component1/component3", "")
except: pass
try: gr.add_node("inelastic1/elastic2", "")
except: pass

gr.add_edge(("component1/component3", "inelastic1/elastic2"), label="ELASTICITY")

try: gr.add_node("MAXIMUM1-1/MAXIMUM1-3", "")
except: pass
try: gr.add_node("elastic1/elastic3", "")
except: pass

gr.add_edge(("MAXIMUM1-1/MAXIMUM1-3", "elastic1/elastic3"), label="MAXIMUM")

try: gr.add_node("component2/component2", "")
except: pass
try: gr.add_node("stable2/stable1", "")
except: pass

gr.add_edge(("component2/component2", "stable2/stable1"), label="STABILITY")

try: gr.add_node("component3/component1", "")
except: pass
try: gr.add_node("stable3/unstable1", "")
except: pass

gr.add_edge(("component3/component1", "stable3/unstable1"), label="STABILITY")

try: gr.add_node("MAXIMUM1-1/MAXIMUM1-1", "")
except: pass
try: gr.add_node("elastic1/elastic1", "")
except: pass

gr.add_edge(("MAXIMUM1-1/MAXIMUM1-1", "elastic1/elastic1"), label="MAXIMUM")

dot = gr.to_dot()
dot.write_dot('pcg' + '.dot')