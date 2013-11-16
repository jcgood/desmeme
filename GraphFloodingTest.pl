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
		
		my $oldSim = $simList{$v};
		my $newSim = $newSimList{$v};
		my $diff = $oldSim - $newSim;
		push(@dists,$diff);
		#print "diff: $diff\n";
	
		}	
	
	my $eucSum;
	for my $dist (@dists) {
	
		#print "d: ".$dist*$dist."\n";
		$eucSum += $dist*$dist;
	
		}
	
	my $eucDist = sqrt($eucSum);
	print "$eucDist\n";
	
	if ($eucDist != 0 and $eucDist < .05) {
	
		$method->getLargeSimilarities($g1,$g2);
		print "hello\n";
		
		last;
	
		}
	
	%simList = %newSimList;
	
	}