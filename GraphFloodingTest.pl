use strict;
use FindBin;
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;


my $g1 = Graph->new(multiedged => 1);
$g1->add_edge_by_id("Koala", "Eucalyptus", "diet");
$g1->add_edge_by_id("Koala", "Acacia", "diet");
$g1->add_edge_by_id("Eucalyptus", "Acacia", "at-risk");

my $g2 = Graph->new(multiedged => 1);
$g2->add_edge_by_id("Panda", "Bamboo", "diet");
$g2->add_edge_by_id("Panda", "Emu", "at-risk");
$g2->add_edge_by_id("Emu", "Bamboo", "at-risk");

# Initialize simList
my $initialS = new GraphJG::SimilarityJG(graph => [$g1,$g2]);
my $initialMethod = $initialS->use('SimilarityFlooding');
$initialMethod->setNumOfIteration(1);
$initialMethod->calculate();
my %simList = $initialMethod->getAllSimilarities;


for (my $count = 1; $count <=15; $count++) {

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

	$method->showAllSimilarities($g1,$g2);
	print "\n";
	
	if ($eucDist != 0 and $eucDist < .05) {
	
		#$method->showAllSimilarities($g1,$g2);
		
		last;
	
		}
	
	%simList = %newSimList;
	
	}