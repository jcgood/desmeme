use strict;
use warnings;

use Graph;
use Moose;

# my $g1 = Graph->new(multiedged => 1);
# $g1->add_edge_by_id("Koala", "Eucalyptus", "diet");
# $g1->add_edge_by_id("Koala", "Acacia", "diet");
# $g1->add_edge_by_id("Eucalyptus", "Acacia", "at-risk");
# 
# my $g2 = Graph->new(multiedged => 1);
# $g2->add_edge_by_id("Panda", "Bamboo", "diet");
# $g2->add_edge_by_id("Panda", "Emu", "at-risk");
# $g2->add_edge_by_id("Emu", "Bamboo", "at-risk");


my $g1 = Graph->new(multiedged => 1);
$g1->set_graph_attribute("name", "ChichewaAR");
$g1->add_edge_by_id("arch", "component1", "LEFT_SUPPORT");
$g1->add_edge_by_id("component1", "inelastic1", "ELASTICITY");
$g1->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$g1->add_edge_by_id("component1", "open1", "FILLEDNESS");
$g1->add_edge_by_id("open1", "coherent1", "COHERENCE");
$g1->add_edge_by_id("component1", "stable1", "STABILITY");
$g1->add_edge_by_id("arch", "component2", "LEFT_VOUSSOIR");
$g1->add_edge_by_id("component2", "inelastic2", "ELASTICITY");
$g1->add_edge_by_id("inelastic2", "COUNT0-1", "COUNT");
$g1->add_edge_by_id("component2", "null1", "FILLEDNESS");
$g1->add_edge_by_id("component2", "stable2", "STABILITY");


my $g2 = Graph->new(multiedged => 1);
$g2->add_edge_by_id("arch", "component1", "LEFT_SUPPORT");
$g2->add_edge_by_id("component1", "elastic1", "ELASTICITY");
$g2->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$g2->add_edge_by_id("elastic1", "MAXIMUM1-1", "MAXIMUM");
$g2->add_edge_by_id("component1", "open1", "FILLEDNESS");
$g2->add_edge_by_id("open1", "coherent1", "COHERENCE");
$g2->add_edge_by_id("component1", "unstable1", "STABILITY");
$g2->add_edge_by_id("unstable1", "right", "ASSOCIATE_POSITION");
$g2->add_edge_by_id("unstable1", "component2", "ASSOCIATE");
$g2->add_edge_by_id("component2", "inelastic1", "ELASTICITY");
$g2->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$g2->add_edge_by_id("component2", "open2", "FILLEDNESS");
$g2->add_edge_by_id("open2", "coherent2", "COHERENCE");
$g2->add_edge_by_id("component2", "stable1", "STABILITY");


my $pcg = Graph->new(multiedged => 1);

# First, collect source, destination node and label
# The is for Graph1
my %m1;
my %labels;
for my $v1 ($g1->vertices){
	for my $p1 ($g1->predecessors($v1)){
		for my $label ($g1->get_multiedge_ids($p1, $v1)){
			# {"LABEL"}{"SOURCE NODE"}{"DESTINATION NODE"}
			$m1{$label}{$p1}{$v1} = 1; # There is no meaing to put 1. Just want to pickup unique key later
			$labels{$label} = 1;
		}
	}
}
# For Graph2
my %m2;
my @labels;
for my $v2 ($g2->vertices){
	for my $p2 ($g2->predecessors($v2)){
		for my $label ($g2->get_multiedge_ids($p2, $v2)){
			# {"LABEL"}{"SOURCE NODE"}{"DESTINATION NODE"}
			$m2{$label}{$p2}{$v2} = 1;
			$labels{$label} = 1;
		}
	}
}

# Second, add pairwise node.
# Node name is src1(from graph1)/src2(from graph2) or dest1(from graph1)/dest2(from graph2)
# %edges used for counting the label of neighbors
my %edges;
for my $label (keys %labels) {
	#print $label, "------\n";
	for my $src1 (keys %{$m1{$label}}){
		for my $src2 (keys %{$m2{$label}}){
			for my $dest1 (keys %{$m1{$label}{$src1}}){
				for my $dest2 (keys %{$m2{$label}{$src2}}){
					#print "src - $src1,$src2\n";
					#print "dest - $dest1,$dest2\n";
					$pcg->add_edge_by_id("$src1/$src2", "$dest1/$dest2", $label ); # JG: The algorithm has bidirectional flooding, so we enter as two-way edge
					$pcg->add_edge_by_id("$dest1/$dest2", "$src1/$src2", $label ); 
					$edges{"$src1/$src2"}{$label}++; #JG" For a given edge label figure out how many lead to/from that node
					$edges{"$dest1/$dest2"}{$label}++;
				}
			}
		}
	}
}


open (DOT, '>PCGtoDOT.py');  #Erase file


print DOT  "from pygraph.classes.digraph import digraph\n";
print DOT  "from pygraph.readwrite.markup import write\n";
print DOT  "import pydot\n\n";
print DOT  "import tdag\n\n";

print DOT  "gr = tdag.tdag(\"\")\n\n";

my $printgraph = $pcg;
my @alledges = $printgraph->edges();

my %seenEdges;
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: gr.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: gr.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		if (exists($seenEdges{"$n2/$n1"})) { print DOT  "gr.add_edge((\"$n1\", \"$n2\"), label=\" \")\n\n"; print "hellp\n";}
		else {print "$n2/$n1 ".exists($seenEdges{"$n2/$n1"})."\n"; }
		$seenEdges{"$n1/$n2"} = 1;
		
		}
	
	}
	
print DOT  "dot = gr.to_dot()\n";
print DOT  "dot.write_dot('pcg' + '.dot')";
