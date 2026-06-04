use strict;
use FindBin;
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;


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


# Initialize simList
my $initialS = new GraphJG::SimilarityJG(graph => [$g1,$g2]);
my $initialMethod = $initialS->use('SimilarityFlooding');
$initialMethod->setNumOfIteration(1);
$initialMethod->calculate();
my %simList = $initialMethod->getAllSimilarities;


for (my $count = 0; $count <=20; $count++) {

	my $s = new GraphJG::SimilarityJG(graph => [$g1,$g2]);
	my $method = $s->use('SimilarityFlooding');
	$method->setNumOfIteration($count);
	$method->calculate();

	my %newSimList = $method->getAllSimilarities;

	my @dists;
	for my $v (keys(%simList)) {
		
		# This is messy: We run through the paired graph to see if this paired node is in any subgraph.
		# "Free-floating" nodes get ignored for the purposes of calculating the Euclidean distance.
		my $pcg = $method->pcg;
		my @pairedvs = $pcg->vertices();
		for my $pairedv (@pairedvs) {
			if($v eq $pairedv) {
				my $oldSim = $simList{$v};
				my $newSim = $newSimList{$v};
				my $diff = $oldSim - $newSim;
				push(@dists,$diff);
				last;			
				}
			}
		}	
	
	my $eucSum;
	for my $dist (@dists) {
	
		#print "d: ".$dist*$dist."\n";
		$eucSum += $dist*$dist;
	
		}
	
	my $eucDist = sqrt($eucSum);
	print "Count: $count\n";	
	print "$eucDist\n";

	#$method->showNonZeroSimilarities($g1,$g2);
	$method->showLargeSimilarities($g1,$g2);
	print "\n";
	
	if ($eucDist != 0 and $eucDist < .05) {
	
		#$method->showAllSimilarities($g1,$g2);
		
		last;
	
		}
	
	%simList = %newSimList;
	
	}