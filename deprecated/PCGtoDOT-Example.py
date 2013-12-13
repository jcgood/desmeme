from pygraph.classes.digraph import digraph
from pygraph.readwrite.markup import write
import pydot
import tdag
from tdag import draw_graphs

pcgweighted = tdag.tdag("example-pcgweighted")
pcglabels = tdag.tdag("example-pcglabels")
g1 = tdag.tdag("example-g1")
g2 = tdag.tdag("example-g2")

try: pcgweighted.add_node("stable1/unstable2", "")
except: pass
try: pcgweighted.add_node("component1/component3", "")
except: pass

try: pcgweighted.add_edge(("stable1/unstable2", "component1/component3"), label=" 1")
except: pass

try: pcgweighted.add_node("inelastic1/elastic2", "")
except: pass
try: pcgweighted.add_node("component1/component4", "")
except: pass

try: pcgweighted.add_edge(("inelastic1/elastic2", "component1/component4"), label=" 1")
except: pass

try: pcgweighted.add_node("open2/open3", "")
except: pass
try: pcgweighted.add_node("component2/component4", "")
except: pass

try: pcgweighted.add_edge(("open2/open3", "component2/component4"), label=" 1")
except: pass

try: pcgweighted.add_node("span1/span2", "")
except: pass
try: pcgweighted.add_node("component2/component4", "")
except: pass

try: pcgweighted.add_edge(("span1/span2", "component2/component4"), label=" 0.5")
except: pass

try: pcgweighted.add_node("unstable1/stable2", "")
except: pass
try: pcgweighted.add_node("component2/component4", "")
except: pass

try: pcgweighted.add_edge(("unstable1/stable2", "component2/component4"), label=" 1")
except: pass

try: pcgweighted.add_node("component1/component4", "")
except: pass
try: pcgweighted.add_node("open1/open3", "")
except: pass

try: pcgweighted.add_edge(("component1/component4", "open1/open3"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component2/component3", "")
except: pass
try: pcgweighted.add_node("inelastic2/elastic1", "")
except: pass

try: pcgweighted.add_edge(("component2/component3", "inelastic2/elastic1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("open1/filled1", "")
except: pass
try: pcgweighted.add_node("component1/component3", "")
except: pass

try: pcgweighted.add_edge(("open1/filled1", "component1/component3"), label=" 1")
except: pass

try: pcgweighted.add_node("component1/component3", "")
except: pass
try: pcgweighted.add_node("inelastic1/elastic1", "")
except: pass

try: pcgweighted.add_edge(("component1/component3", "inelastic1/elastic1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component1/component3", "")
except: pass
try: pcgweighted.add_node("open1/filled1", "")
except: pass

try: pcgweighted.add_edge(("component1/component3", "open1/filled1"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic2/elastic1", "")
except: pass
try: pcgweighted.add_node("component2/component3", "")
except: pass

try: pcgweighted.add_edge(("inelastic2/elastic1", "component2/component3"), label=" 1")
except: pass

try: pcgweighted.add_node("component2/component4", "")
except: pass
try: pcgweighted.add_node("unstable1/stable2", "")
except: pass

try: pcgweighted.add_edge(("component2/component4", "unstable1/stable2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("stable1/stable2", "")
except: pass
try: pcgweighted.add_node("component1/component4", "")
except: pass

try: pcgweighted.add_edge(("stable1/stable2", "component1/component4"), label=" 1")
except: pass

try: pcgweighted.add_node("component2/component4", "")
except: pass
try: pcgweighted.add_node("span1/span2", "")
except: pass

try: pcgweighted.add_edge(("component2/component4", "span1/span2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic2/elastic2", "")
except: pass
try: pcgweighted.add_node("component2/component4", "")
except: pass

try: pcgweighted.add_edge(("inelastic2/elastic2", "component2/component4"), label=" 1")
except: pass

try: pcgweighted.add_node("component2/component4", "")
except: pass
try: pcgweighted.add_node("open2/open3", "")
except: pass

try: pcgweighted.add_edge(("component2/component4", "open2/open3"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open1/open3", "")
except: pass
try: pcgweighted.add_node("component1/component4", "")
except: pass

try: pcgweighted.add_edge(("open1/open3", "component1/component4"), label=" 1")
except: pass

try: pcgweighted.add_node("component1/component3", "")
except: pass
try: pcgweighted.add_node("span1/span2", "")
except: pass

try: pcgweighted.add_edge(("component1/component3", "span1/span2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("component1/component4", "")
except: pass
try: pcgweighted.add_node("stable1/stable2", "")
except: pass

try: pcgweighted.add_edge(("component1/component4", "stable1/stable2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component1/component4", "")
except: pass
try: pcgweighted.add_node("inelastic1/elastic2", "")
except: pass

try: pcgweighted.add_edge(("component1/component4", "inelastic1/elastic2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component2/component3", "")
except: pass
try: pcgweighted.add_node("unstable1/unstable2", "")
except: pass

try: pcgweighted.add_edge(("component2/component3", "unstable1/unstable2"), label=" 0.33")
except: pass

try: pcgweighted.add_node("unstable1/unstable2", "")
except: pass
try: pcgweighted.add_node("component2/component3", "")
except: pass

try: pcgweighted.add_edge(("unstable1/unstable2", "component2/component3"), label=" 1")
except: pass

try: pcgweighted.add_node("span1/span2", "")
except: pass
try: pcgweighted.add_node("component1/component3", "")
except: pass

try: pcgweighted.add_edge(("span1/span2", "component1/component3"), label=" 0.5")
except: pass

try: pcgweighted.add_node("component2/component3", "")
except: pass
try: pcgweighted.add_node("open2/filled1", "")
except: pass

try: pcgweighted.add_edge(("component2/component3", "open2/filled1"), label=" 0.33")
except: pass

try: pcgweighted.add_node("component2/component4", "")
except: pass
try: pcgweighted.add_node("inelastic2/elastic2", "")
except: pass

try: pcgweighted.add_edge(("component2/component4", "inelastic2/elastic2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("inelastic1/elastic1", "")
except: pass
try: pcgweighted.add_node("component1/component3", "")
except: pass

try: pcgweighted.add_edge(("inelastic1/elastic1", "component1/component3"), label=" 1")
except: pass

try: pcgweighted.add_node("component1/component3", "")
except: pass
try: pcgweighted.add_node("stable1/unstable2", "")
except: pass

try: pcgweighted.add_edge(("component1/component3", "stable1/unstable2"), label=" 0.25")
except: pass

try: pcgweighted.add_node("open2/filled1", "")
except: pass
try: pcgweighted.add_node("component2/component3", "")
except: pass

try: pcgweighted.add_edge(("open2/filled1", "component2/component3"), label=" 1")
except: pass

try: pcglabels.add_node("stable1/unstable2", "")
except: pass
try: pcglabels.add_node("component1/component3", "")
except: pass

try: pcglabels.add_edge(("stable1/unstable2", "component1/component3"), label="STABILITY")
except: pass

try: pcglabels.add_node("inelastic1/elastic2", "")
except: pass
try: pcglabels.add_node("component1/component4", "")
except: pass

try: pcglabels.add_edge(("inelastic1/elastic2", "component1/component4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open2/open3", "")
except: pass
try: pcglabels.add_node("component2/component4", "")
except: pass

try: pcglabels.add_edge(("open2/open3", "component2/component4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("span1/span2", "")
except: pass
try: pcglabels.add_node("component2/component4", "")
except: pass

try: pcglabels.add_edge(("span1/span2", "component2/component4"), label="RIGHT_SUPPORT")
except: pass

try: pcglabels.add_node("unstable1/stable2", "")
except: pass
try: pcglabels.add_node("component2/component4", "")
except: pass

try: pcglabels.add_edge(("unstable1/stable2", "component2/component4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component1/component4", "")
except: pass
try: pcglabels.add_node("open1/open3", "")
except: pass

try: pcglabels.add_edge(("component1/component4", "open1/open3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component2/component3", "")
except: pass
try: pcglabels.add_node("inelastic2/elastic1", "")
except: pass

try: pcglabels.add_edge(("component2/component3", "inelastic2/elastic1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("open1/filled1", "")
except: pass
try: pcglabels.add_node("component1/component3", "")
except: pass

try: pcglabels.add_edge(("open1/filled1", "component1/component3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component1/component3", "")
except: pass
try: pcglabels.add_node("inelastic1/elastic1", "")
except: pass

try: pcglabels.add_edge(("component1/component3", "inelastic1/elastic1"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component1/component3", "")
except: pass
try: pcglabels.add_node("open1/filled1", "")
except: pass

try: pcglabels.add_edge(("component1/component3", "open1/filled1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("inelastic2/elastic1", "")
except: pass
try: pcglabels.add_node("component2/component3", "")
except: pass

try: pcglabels.add_edge(("inelastic2/elastic1", "component2/component3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component2/component4", "")
except: pass
try: pcglabels.add_node("unstable1/stable2", "")
except: pass

try: pcglabels.add_edge(("component2/component4", "unstable1/stable2"), label="STABILITY")
except: pass

try: pcglabels.add_node("stable1/stable2", "")
except: pass
try: pcglabels.add_node("component1/component4", "")
except: pass

try: pcglabels.add_edge(("stable1/stable2", "component1/component4"), label="STABILITY")
except: pass

try: pcglabels.add_node("component2/component4", "")
except: pass
try: pcglabels.add_node("span1/span2", "")
except: pass

try: pcglabels.add_edge(("component2/component4", "span1/span2"), label="RIGHT_SUPPORT")
except: pass

try: pcglabels.add_node("inelastic2/elastic2", "")
except: pass
try: pcglabels.add_node("component2/component4", "")
except: pass

try: pcglabels.add_edge(("inelastic2/elastic2", "component2/component4"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component2/component4", "")
except: pass
try: pcglabels.add_node("open2/open3", "")
except: pass

try: pcglabels.add_edge(("component2/component4", "open2/open3"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("open1/open3", "")
except: pass
try: pcglabels.add_node("component1/component4", "")
except: pass

try: pcglabels.add_edge(("open1/open3", "component1/component4"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component1/component3", "")
except: pass
try: pcglabels.add_node("span1/span2", "")
except: pass

try: pcglabels.add_edge(("component1/component3", "span1/span2"), label="LEFT_SUPPORT")
except: pass

try: pcglabels.add_node("component1/component4", "")
except: pass
try: pcglabels.add_node("stable1/stable2", "")
except: pass

try: pcglabels.add_edge(("component1/component4", "stable1/stable2"), label="STABILITY")
except: pass

try: pcglabels.add_node("component1/component4", "")
except: pass
try: pcglabels.add_node("inelastic1/elastic2", "")
except: pass

try: pcglabels.add_edge(("component1/component4", "inelastic1/elastic2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component2/component3", "")
except: pass
try: pcglabels.add_node("unstable1/unstable2", "")
except: pass

try: pcglabels.add_edge(("component2/component3", "unstable1/unstable2"), label="STABILITY")
except: pass

try: pcglabels.add_node("unstable1/unstable2", "")
except: pass
try: pcglabels.add_node("component2/component3", "")
except: pass

try: pcglabels.add_edge(("unstable1/unstable2", "component2/component3"), label="STABILITY")
except: pass

try: pcglabels.add_node("span1/span2", "")
except: pass
try: pcglabels.add_node("component1/component3", "")
except: pass

try: pcglabels.add_edge(("span1/span2", "component1/component3"), label="LEFT_SUPPORT")
except: pass

try: pcglabels.add_node("component2/component3", "")
except: pass
try: pcglabels.add_node("open2/filled1", "")
except: pass

try: pcglabels.add_edge(("component2/component3", "open2/filled1"), label="FILLEDNESS")
except: pass

try: pcglabels.add_node("component2/component4", "")
except: pass
try: pcglabels.add_node("inelastic2/elastic2", "")
except: pass

try: pcglabels.add_edge(("component2/component4", "inelastic2/elastic2"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("inelastic1/elastic1", "")
except: pass
try: pcglabels.add_node("component1/component3", "")
except: pass

try: pcglabels.add_edge(("inelastic1/elastic1", "component1/component3"), label="ELASTICITY")
except: pass

try: pcglabels.add_node("component1/component3", "")
except: pass
try: pcglabels.add_node("stable1/unstable2", "")
except: pass

try: pcglabels.add_edge(("component1/component3", "stable1/unstable2"), label="STABILITY")
except: pass

try: pcglabels.add_node("open2/filled1", "")
except: pass
try: pcglabels.add_node("component2/component3", "")
except: pass

try: pcglabels.add_edge(("open2/filled1", "component2/component3"), label="FILLEDNESS")
except: pass

try: g1.add_node("component2", "")
except: pass
try: g1.add_node("open2", "")
except: pass

try: g1.add_edge(("component2", "open2"), label=" FILLEDNESS")
except: pass

try: g1.add_node("span1", "")
except: pass
try: g1.add_node("component2", "")
except: pass

try: g1.add_edge(("span1", "component2"), label=" RIGHT_SUPPORT")
except: pass

try: g1.add_node("component1", "")
except: pass
try: g1.add_node("inelastic1", "")
except: pass

try: g1.add_edge(("component1", "inelastic1"), label=" ELASTICITY")
except: pass

try: g1.add_node("component1", "")
except: pass
try: g1.add_node("stable1", "")
except: pass

try: g1.add_edge(("component1", "stable1"), label=" STABILITY")
except: pass

try: g1.add_node("span1", "")
except: pass
try: g1.add_node("component1", "")
except: pass

try: g1.add_edge(("span1", "component1"), label=" LEFT_SUPPORT")
except: pass

try: g1.add_node("component2", "")
except: pass
try: g1.add_node("unstable1", "")
except: pass

try: g1.add_edge(("component2", "unstable1"), label=" STABILITY")
except: pass

try: g1.add_node("component1", "")
except: pass
try: g1.add_node("open1", "")
except: pass

try: g1.add_edge(("component1", "open1"), label=" FILLEDNESS")
except: pass

try: g1.add_node("component2", "")
except: pass
try: g1.add_node("inelastic2", "")
except: pass

try: g1.add_edge(("component2", "inelastic2"), label=" ELASTICITY")
except: pass

try: g2.add_node("component4", "")
except: pass
try: g2.add_node("open3", "")
except: pass

try: g2.add_edge(("component4", "open3"), label=" FILLEDNESS")
except: pass

try: g2.add_node("component3", "")
except: pass
try: g2.add_node("unstable2", "")
except: pass

try: g2.add_edge(("component3", "unstable2"), label=" STABILITY")
except: pass

try: g2.add_node("span2", "")
except: pass
try: g2.add_node("component4", "")
except: pass

try: g2.add_edge(("span2", "component4"), label=" RIGHT_SUPPORT")
except: pass

try: g2.add_node("component3", "")
except: pass
try: g2.add_node("filled1", "")
except: pass

try: g2.add_edge(("component3", "filled1"), label=" FILLEDNESS")
except: pass

try: g2.add_node("span2", "")
except: pass
try: g2.add_node("component3", "")
except: pass

try: g2.add_edge(("span2", "component3"), label=" LEFT_SUPPORT")
except: pass

try: g2.add_node("component4", "")
except: pass
try: g2.add_node("stable2", "")
except: pass

try: g2.add_edge(("component4", "stable2"), label=" STABILITY")
except: pass

try: g2.add_node("component3", "")
except: pass
try: g2.add_node("elastic1", "")
except: pass

try: g2.add_edge(("component3", "elastic1"), label=" ELASTICITY")
except: pass

try: g2.add_node("component4", "")
except: pass
try: g2.add_node("elastic2", "")
except: pass

try: g2.add_edge(("component4", "elastic2"), label=" ELASTICITY")
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
draw_graphs([pcgweighted, pcglabels, g1, g2], pcgfolder)
