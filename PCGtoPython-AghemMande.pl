use strict;
use warnings;

use Graph;
use Moose;
use Math::Round;

#I've been adding the template-specific suffixes by hand
#And cutting and pasting the templates in, too

my $AghemClause = Graph->new(multiedged => 1);
$AghemClause->set_graph_attribute("name", "AghemClause");
$AghemClause->add_edge_by_id("desmeme", "order", "STRICTURE");
$AghemClause->add_edge_by_id("order", "syntacticConstituent", "CONSTITUENT");
$AghemClause->add_edge_by_id("order", "simple", "RELATIONS");
$AghemClause->add_edge_by_id("order", "count6-a1", "COUNT");
$AghemClause->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$AghemClause->add_edge_by_id("arch", "component-a1", "LEFT_SUPPORT");
$AghemClause->add_edge_by_id("component-a1", "inelastic-a1", "ELASTICITY");
$AghemClause->add_edge_by_id("inelastic-a1", "count1-a1", "COUNT");
$AghemClause->add_edge_by_id("component-a1", "open-a1", "FILLEDNESS");
$AghemClause->add_edge_by_id("open-a1", "coherent-a1", "COHERENCE");
$AghemClause->add_edge_by_id("component-a1", "stable-a1", "STABILITY");
$AghemClause->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$AghemClause->add_edge_by_id("restkomponentenSet", "component-a2", "RESTKOMPONENT");
$AghemClause->add_edge_by_id("component-a2", "elastic-a1", "ELASTICITY");
$AghemClause->add_edge_by_id("elastic-a1", "minimum0-a1", "MINIMUM");
$AghemClause->add_edge_by_id("elastic-a1", "maximum1-a1", "MAXIMUM");
$AghemClause->add_edge_by_id("component-a2", "open-a2", "FILLEDNESS");
$AghemClause->add_edge_by_id("open-a2", "coherent-a2", "COHERENCE");
$AghemClause->add_edge_by_id("component-a2", "stable-a2", "STABILITY");
$AghemClause->add_edge_by_id("arch", "component-a3", "LEFT_VOUSSOIR");
$AghemClause->add_edge_by_id("component-a3", "elastic-a2", "ELASTICITY");
$AghemClause->add_edge_by_id("elastic-a2", "minimum0-a2", "MINIMUM");
$AghemClause->add_edge_by_id("elastic-a2", "maximum100-a1", "MAXIMUM");
$AghemClause->add_edge_by_id("component-a3", "open-a3", "FILLEDNESS");
$AghemClause->add_edge_by_id("open-a3", "coherent-a3", "COHERENCE");
$AghemClause->add_edge_by_id("component-a3", "stable-a3", "STABILITY");
$AghemClause->add_edge_by_id("arch", "component-a4", "RIGHT_VOUSSOIR");
$AghemClause->add_edge_by_id("component-a4", "inelastic-a2", "ELASTICITY");
$AghemClause->add_edge_by_id("inelastic-a2", "count1-a2", "COUNT");
$AghemClause->add_edge_by_id("component-a4", "open-a4", "FILLEDNESS");
$AghemClause->add_edge_by_id("open-a4", "coherent-a4", "COHERENCE");
$AghemClause->add_edge_by_id("component-a4", "unstable-a1", "STABILITY");
$AghemClause->add_edge_by_id("unstable-a1", "left", "ASSOCIATE_POSITION");
$AghemClause->add_edge_by_id("unstable-a1", "component-a2", "ASSOCIATE");
$AghemClause->add_edge_by_id("arch", "component-a5", "KEYSTONE");
$AghemClause->add_edge_by_id("component-a5", "inelastic-a3", "ELASTICITY");
$AghemClause->add_edge_by_id("inelastic-a3", "count1-a3", "COUNT");
$AghemClause->add_edge_by_id("component-a5", "open-a5", "FILLEDNESS");
$AghemClause->add_edge_by_id("open-a5", "coherent-a5", "COHERENCE");
$AghemClause->add_edge_by_id("component-a5", "stable-a4", "STABILITY");
$AghemClause->add_edge_by_id("arch", "component-a6", "RIGHT_SUPPORT");
$AghemClause->add_edge_by_id("component-a6", "elastic-a3", "ELASTICITY");
$AghemClause->add_edge_by_id("elastic-a3", "minimum0-a3", "MINIMUM");
$AghemClause->add_edge_by_id("elastic-a3", "maximum100-a2", "MAXIMUM");
$AghemClause->add_edge_by_id("component-a6", "open-a6", "FILLEDNESS");
$AghemClause->add_edge_by_id("open-a6", "coherent-a6", "COHERENCE");
$AghemClause->add_edge_by_id("component-a6", "stable-a5", "STABILITY");
$AghemClause->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
$AghemClause->add_edge_by_id("desmeme", "potentiallyViolable", "VIOLABILITY");
$AghemClause->add_edge_by_id("potentiallyViolable", "morphosyntacticInsertion", "REPARABILITY");
$AghemClause->add_edge_by_id("potentiallyViolable", "lexical", "EXCEPTIONALITY");


my $MandeClause = Graph->new(multiedged => 1);
$MandeClause->set_graph_attribute("name", "MandeClause");
$MandeClause->add_edge_by_id("desmeme", "order", "STRICTURE");
$MandeClause->add_edge_by_id("order", "syntacticConstituent", "CONSTITUENT");
$MandeClause->add_edge_by_id("order", "simple", "RELATIONS");
$MandeClause->add_edge_by_id("order", "count5-m1", "COUNT");
$MandeClause->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$MandeClause->add_edge_by_id("arch", "component-m1", "LEFT_SUPPORT");
$MandeClause->add_edge_by_id("component-m1", "inelastic-m1", "ELASTICITY");
$MandeClause->add_edge_by_id("inelastic-m1", "count1-m1", "COUNT");
$MandeClause->add_edge_by_id("component-m1", "open-m1", "FILLEDNESS");
$MandeClause->add_edge_by_id("open-m1", "coherent-m1", "COHERENCE");
$MandeClause->add_edge_by_id("component-m1", "stable-m1", "STABILITY");
$MandeClause->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$MandeClause->add_edge_by_id("restkomponentenSet", "component-m2", "RESTKOMPONENT");
$MandeClause->add_edge_by_id("component-m2", "elastic-m1", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic-m1", "minimum0-m1", "MINIMUM");
$MandeClause->add_edge_by_id("elastic-m1", "maximum1-m1", "MAXIMUM");
$MandeClause->add_edge_by_id("component-m2", "open-m2", "FILLEDNESS");
$MandeClause->add_edge_by_id("open-m2", "coherent-m2", "COHERENCE");
$MandeClause->add_edge_by_id("component-m2", "stable-m2", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component-m3", "LEFT_VOUSSOIR");
$MandeClause->add_edge_by_id("component-m3", "elastic-m2", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic-m2", "minimum0-m2", "MINIMUM");
$MandeClause->add_edge_by_id("elastic-m2", "maximum1-m2", "maximum");
$MandeClause->add_edge_by_id("component-m3", "open-m3", "FILLEDNESS");
$MandeClause->add_edge_by_id("open-m3", "coherent-m3", "COHERENCE");
$MandeClause->add_edge_by_id("component-m3", "stable-m3", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component-m4", "RIGHT_VOUSSOIR");
$MandeClause->add_edge_by_id("component-m4", "elastic-m3", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic-m3", "minimum0-m3", "MINIMUM");
$MandeClause->add_edge_by_id("elastic-m3", "maximum100-m1", "maximum");
$MandeClause->add_edge_by_id("component-m4", "open-m4", "FILLEDNESS");
$MandeClause->add_edge_by_id("open-m4", "incoherent-m1", "COHERENCE");
$MandeClause->add_edge_by_id("component-m4", "stable-m4", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component-m5", "KEYSTONE");
$MandeClause->add_edge_by_id("component-m5", "inelastic-m2", "ELASTICITY");
$MandeClause->add_edge_by_id("inelastic-m2", "count1-m2", "COUNT");
$MandeClause->add_edge_by_id("component-m5", "open-m5", "FILLEDNESS");
$MandeClause->add_edge_by_id("open-m5", "coherent-m4", "COHERENCE");
$MandeClause->add_edge_by_id("component-m5", "stable-m5", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component-m4", "RIGHT_SUPPORT");
$MandeClause->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
$MandeClause->add_edge_by_id("desmeme", "notViolable", "VIOLABILITY");



my $pcg = Graph->new(multiedged => 1);
my $pcgNoLabels = Graph->new(multiedged => 1); # No two-way arrows

# First, collect source, destination node and label
# The is for Graph1
my %m1;
my %labels;
for my $v1 ($AghemClause->vertices){
	for my $p1 ($AghemClause->predecessors($v1)){
		for my $label ($AghemClause->get_multiedge_ids($p1, $v1)){
			# {"LABEL"}{"SOURCE NODE"}{"DESTINATION NODE"}
			$m1{$label}{$p1}{$v1} = 1; # There is no meaing to put 1. Just want to pickup unique key later
			$labels{$label} = 1;
		}
	}
}
# For Graph2
my %m2;
my @labels;
for my $v2 ($MandeClause->vertices){
	for my $p2 ($MandeClause->predecessors($v2)){
		for my $label ($MandeClause->get_multiedge_ids($p2, $v2)){
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


open (DOT, '>PCGtoDOT-AghemMande.py');  #Erase file


print DOT  "from pygraph.classes.digraph import digraph\n";
print DOT  "from pygraph.readwrite.markup import write\n";
print DOT  "import pydot\n";
print DOT  "import tdag\n";
print DOT  "from tdag import draw_graphs\n\n";

print DOT  "pcgweighted = tdag.tdag(\"AghemMande-weighted\")\n";
print DOT  "pcglabels = tdag.tdag(\"AghemMande-labels\")\n";
print DOT  "AghemClause = tdag.tdag(\"AghemClause\")\n";
print DOT  "MandeClause = tdag.tdag(\"MandeClause\")\n\n";

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
		print DOT  "try: pcgweighted.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: pcgweighted.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = $numEdges * (1/$outgoing{$n1});
				
		print DOT  "try: pcgweighted.add_edge((\"$n1\", \"$n2\"), label=\" ".nearest(.01, $weighting)."\")\nexcept: pass\n\n";
		
		}
	
	}


$printgraph = $pcg;
@alledges = $printgraph->edges();
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: pcglabels.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: pcglabels.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = $numEdges * (1/$outgoing{$n1});
				
		print DOT  "try: pcglabels.add_edge((\"$n1\", \"$n2\"), label=\"$edgeLabel\")\nexcept: pass\n\n";
		
		}
	
	}



# Write out $AghemClause and $MandeClause, too for display
$printgraph = $AghemClause;
@alledges = $printgraph->edges();
my %seeng1edges;
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: AghemClause.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: AghemClause.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = 1/$numEdges;
				
		unless ($seeng1edges{"$n1-$n2-$edgeLabel"})
			{ print DOT  "try: AghemClause.add_edge((\"$n1\", \"$n2\"), label=\" ".$edgeLabel."\")\nexcept: pass\n\n"; }
		
		$seeng1edges{"$n1-$n2-$edgeLabel"} = 1;
		
		}
	
	}



# Write out $AghemClause and $MandeClause, too for display
$printgraph = $MandeClause;
@alledges = $printgraph->edges();
my %seeng2edges;
for my $edgeArray (@alledges) {

	my ($n1, $n2) = @{$edgeArray};
	
	my @edgeLabels = $printgraph->get_multiedge_ids($n1,$n2);

	for my $edgeLabel (@edgeLabels) {
		print DOT  "try: MandeClause.add_node(\"$n1\", \"\")\n";
		print DOT  "except: pass\n";
		print DOT  "try: MandeClause.add_node(\"$n2\", \"\")\n";
		print DOT  "except: pass\n\n";
		
		my $numEdges = @edgeLabels;
		my $weighting = 1/$numEdges;
				
		unless ($seeng2edges{"$n1-$n2-$edgeLabel"})
			{ print DOT  "try: MandeClause.add_edge((\"$n1\", \"$n2\"), label=\" ".$edgeLabel."\")\nexcept: pass\n\n"; }
	
		$seeng2edges{"$n1-$n2-$edgeLabel"} = 1;
	
		}
	
	}

	
print DOT "# To self: I spent a long time working out why .dot files had attributes\n";
print DOT "# such as width and pos that I didn't have in my representation.\n";
print DOT "# This \"write_dot\" function is a special pydot feature that doesn't\n";
print DOT "# exist as an actual method but is, rather, generated automatically based on the extension (sort of).\n";
print DOT "# The internal representation is passed through the dot program and the output adds these extra features.\n";
print DOT "# This seems to be the same as the \"default\" ones if they aren't added.\n";
print DOT "# I looked into this to see how I should be customizing node placement.\n";
print DOT "# I guess I'd have to delve deep into dot to find out at this point.\n";
print DOT "# See comparison method in tdag for where this write_dot function is called.\n";

print DOT  "pcgfolder = \"/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/PCGs/\"\n";
print DOT  "draw_graphs([pcgweighted, pcglabels, AghemClause, MandeClause], pcgfolder)\n";
