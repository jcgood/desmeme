use strict;
use warnings;

use Graph;
use Moose;
use Math::Round;

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
$g1->add_edge_by_id("span1", "component1", "LEFT_SUPPORT");
$g1->add_edge_by_id("component1", "inelastic1", "ELASTICITY");
$g1->add_edge_by_id("component1", "open1", "FILLEDNESS");
$g1->add_edge_by_id("component1", "stable1", "STABILITY");
$g1->add_edge_by_id("span1", "component2", "RIGHT_SUPPORT");
$g1->add_edge_by_id("component2", "inelastic2", "ELASTICITY");
$g1->add_edge_by_id("component2", "open2", "FILLEDNESS");
$g1->add_edge_by_id("component2", "unstable1", "STABILITY");


my $g2 = Graph->new(multiedged => 1);
$g2->add_edge_by_id("span2", "component3", "LEFT_SUPPORT");
$g2->add_edge_by_id("span2", "component4", "RIGHT_SUPPORT");
$g2->add_edge_by_id("component3", "elastic1", "ELASTICITY");
$g2->add_edge_by_id("component3", "filled1", "FILLEDNESS");
$g2->add_edge_by_id("component3", "unstable2", "STABILITY");
$g2->add_edge_by_id("component4", "elastic2", "ELASTICITY");
$g2->add_edge_by_id("component4", "open3", "FILLEDNESS");
$g2->add_edge_by_id("component4", "stable2", "STABILITY");


my $pcg = Graph->new(multiedged => 1);
my $pcgNoLabels = Graph->new(multiedged => 1); # No two-way arrows

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


# Second, add pairwise node but for illustration, we don't go whole way to final PCG
# Node name is src1(from graph1)/src2(from graph2) or dest1(from graph1)/dest2(from graph2)
# %edges used for counting the label of neighbors
for my $label (keys %labels) {
	#print $label, "------\n";
	for my $src1 (keys %{$m1{$label}}){
		for my $src2 (keys %{$m2{$label}}){
			for my $dest1 (keys %{$m1{$label}{$src1}}){
				for my $dest2 (keys %{$m2{$label}{$src2}}){
					#print "src - $src1,$src2\n";
					#print "dest - $dest1,$dest2\n";
					$pcgNoLabels->add_edge_by_id("$src1/$src2", "$dest1/$dest2", $label ); # JG: The algorithm has bidirectional flooding, so we enter as two-way edge
					# $pcgNoLabels->add_edge_by_id("$dest1/$dest2", "$src1/$src2", $label );# Keep the original direction only for this one.
				}
			}
		}
	}
}


open (DOT, '>PCGtoDOT.py');  #Erase file


print DOT  "from pygraph.classes.digraph import digraph\n";
print DOT  "from pygraph.readwrite.markup import write\n";
print DOT  "import pydot\n";
print DOT  "import tdag\n";
print DOT  "from tdag import draw_graphs\n\n";

print DOT  "pcg = tdag.tdag(\"pcg\")\n";
print DOT  "pcgnolabels = tdag.tdag(\"pcgnolabels\")\n";
print DOT  "g1 = tdag.tdag(\"g1\")\n";
print DOT  "g2 = tdag.tdag(\"g2\")\n\n";

my $printgraph = $pcg;
my @alledges = $printgraph->edges();
# Get outgoing arc counts
my %outgoing;
for my $edgeArray (@alledges) {
	my ($n1, $n2) = @{$edgeArray};
	$outgoing{$n1}++;
	}


for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: pcg.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: pcg.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = $numEdges * (1/$outgoing{$n1});
				
		print DOT  "try: pcg.add_edge((\"$n1\", \"$n2\"), label=\" ".nearest(.01, $weighting)."\")\nexcept: pass\n\n";
		
		}
	
	}


$printgraph = $pcgNoLabels;
@alledges = $printgraph->edges();
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: pcgnolabels.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: pcgnolabels.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = $numEdges * (1/$outgoing{$n1});
				
		print DOT  "try: pcgnolabels.add_edge((\"$n1\", \"$n2\"), label=\"$edgeLabel\")\nexcept: pass\n\n";
		
		}
	
	}



# Write out $g1 and $g2, too for display
$printgraph = $g1;
@alledges = $printgraph->edges();
my %seeng1edges;
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: g1.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: g1.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = 1/$numEdges;
				
		unless ($seeng1edges{"$n1-$n2-$edgeLabel"})
			{ print DOT  "try: g1.add_edge((\"$n1\", \"$n2\"), label=\" ".$edgeLabel."\")\nexcept: pass\n\n"; }
		
		$seeng1edges{"$n1-$n2-$edgeLabel"} = 1;
		
		}
	
	}



# Write out $g1 and $g2, too for display
$printgraph = $g2;
@alledges = $printgraph->edges();
my %seeng2edges;
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: g2.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: g2.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = 1/$numEdges;
				
		unless ($seeng2edges{"$n1-$n2-$edgeLabel"})
			{ print DOT  "try: g2.add_edge((\"$n1\", \"$n2\"), label=\" ".$edgeLabel."\")\nexcept: pass\n\n"; }
	
		$seeng2edges{"$n1-$n2-$edgeLabel"} = 1;
	
		}
	
	}

	

print DOT  "draw_graphs([pcg, pcgnolabels, g1, g2], \"./\")\n";
