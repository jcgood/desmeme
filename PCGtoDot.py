from pygraph.classes.digraph import digraph
from pygraph.readwrite.markup import write
import pydot

import tdag

gr = tdag.tdag("")

try: gr.add_node("COUNT1-1/COUNT1-1", "")
except: pass
try: gr.add_node("inelastic1/inelastic1", "")
except: pass

try: gr.add_node("inelastic1/inelastic1", "")
except: pass
try: gr.add_node("COUNT1-1/COUNT1-1", "")
except: pass

gr.add_edge(("inelastic1/inelastic1", "COUNT1-1/COUNT1-1"), label=" ")

try: gr.add_node("inelastic1/inelastic1", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

try: gr.add_node("null1/open1", "")
except: pass
try: gr.add_node("component2/component1", "")
except: pass

try: gr.add_node("open1/open1", "")
except: pass
try: gr.add_node("coherent1/coherent1", "")
except: pass

try: gr.add_node("stable2/stable1", "")
except: pass
try: gr.add_node("component2/component2", "")
except: pass

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("open1/open1", "")
except: pass

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("arch/arch", "")
except: pass

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("inelastic1/elastic1", "")
except: pass

try: gr.add_node("inelastic2/inelastic1", "")
except: pass
try: gr.add_node("COUNT0-1/COUNT1-1", "")
except: pass

try: gr.add_node("component2/component2", "")
except: pass
try: gr.add_node("stable2/stable1", "")
except: pass

gr.add_edge(("component2/component2", "stable2/stable1"), label=" ")

try: gr.add_node("coherent1/coherent1", "")
except: pass
try: gr.add_node("open1/open1", "")
except: pass

gr.add_edge(("coherent1/coherent1", "open1/open1"), label=" ")

try: gr.add_node("inelastic2/inelastic1", "")
except: pass
try: gr.add_node("component2/component2", "")
except: pass

try: gr.add_node("open1/open2", "")
except: pass
try: gr.add_node("coherent1/coherent2", "")
except: pass

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("inelastic1/inelastic1", "")
except: pass

gr.add_edge(("component1/component2", "inelastic1/inelastic1"), label=" ")

try: gr.add_node("component2/component1", "")
except: pass
try: gr.add_node("stable2/unstable1", "")
except: pass

try: gr.add_node("component2/component2", "")
except: pass
try: gr.add_node("inelastic2/inelastic1", "")
except: pass

gr.add_edge(("component2/component2", "inelastic2/inelastic1"), label=" ")

try: gr.add_node("component1/component1", "")
except: pass
try: gr.add_node("stable1/unstable1", "")
except: pass

try: gr.add_node("COUNT0-1/COUNT1-1", "")
except: pass
try: gr.add_node("inelastic2/inelastic1", "")
except: pass

gr.add_edge(("COUNT0-1/COUNT1-1", "inelastic2/inelastic1"), label=" ")

try: gr.add_node("stable1/unstable1", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("stable1/unstable1", "component1/component1"), label=" ")

try: gr.add_node("component2/component1", "")
except: pass
try: gr.add_node("inelastic2/elastic1", "")
except: pass

try: gr.add_node("arch/arch", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("arch/arch", "component1/component1"), label=" ")

try: gr.add_node("stable1/stable1", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

try: gr.add_node("inelastic2/elastic1", "")
except: pass
try: gr.add_node("component2/component1", "")
except: pass

gr.add_edge(("inelastic2/elastic1", "component2/component1"), label=" ")

try: gr.add_node("coherent1/coherent2", "")
except: pass
try: gr.add_node("open1/open2", "")
except: pass

gr.add_edge(("coherent1/coherent2", "open1/open2"), label=" ")

try: gr.add_node("component2/component1", "")
except: pass
try: gr.add_node("null1/open1", "")
except: pass

gr.add_edge(("component2/component1", "null1/open1"), label=" ")

try: gr.add_node("open1/open1", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("open1/open1", "component1/component1"), label=" ")

try: gr.add_node("null1/open2", "")
except: pass
try: gr.add_node("component2/component2", "")
except: pass

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("stable1/stable1", "")
except: pass

gr.add_edge(("component1/component2", "stable1/stable1"), label=" ")

try: gr.add_node("stable2/unstable1", "")
except: pass
try: gr.add_node("component2/component1", "")
except: pass

gr.add_edge(("stable2/unstable1", "component2/component1"), label=" ")

try: gr.add_node("component2/component2", "")
except: pass
try: gr.add_node("null1/open2", "")
except: pass

gr.add_edge(("component2/component2", "null1/open2"), label=" ")

try: gr.add_node("component1/component2", "")
except: pass
try: gr.add_node("open1/open2", "")
except: pass

try: gr.add_node("inelastic1/elastic1", "")
except: pass
try: gr.add_node("component1/component1", "")
except: pass

gr.add_edge(("inelastic1/elastic1", "component1/component1"), label=" ")

try: gr.add_node("open1/open2", "")
except: pass
try: gr.add_node("component1/component2", "")
except: pass

gr.add_edge(("open1/open2", "component1/component2"), label=" ")

dot = gr.to_dot()
dot.write_dot('pcg' + '.dot')