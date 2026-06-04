use strict;
use FindBin;
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;
use Math::Round;


my $ChacoboNonInterruptibleByNP_719 = Graph->new(multiedged => 1);
$ChacoboNonInterruptibleByNP_719->set_graph_attribute("name", "ChacoboNonInterruptibleByNP_719");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("arch", "component1", "KEYSTONE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component1", "inelastic1", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component1", "stable1", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component1", "filled1", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("filled1", "embeddedDesmeme", "FORM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("restkomponentenSet", "component2", "RESTKOMPONENTE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component2", "elastic1", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic1", "MAXIMUM1-1", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component2", "stable2", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component2", "filled2", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("filled2", "canonicalLineate1", "FORM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("restkomponentenSet", "component3", "RESTKOMPONENTE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component3", "elastic2", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic2", "MAXIMUM1-2", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component3", "stable3", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component3", "open1", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("open1", "coherent1", "COHERENCE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("restkomponentenSet", "component4", "RESTKOMPONENTE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component4", "elastic3", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic3", "MINIMUM0-3", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic3", "MAXIMUM2-1", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component4", "open2", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("open2", "incoherent1", "COHERENCE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component4", "stable4", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("restkomponentenSet", "component5", "RESTKOMPONENTE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component5", "elastic4", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic4", "MINIMUM0-4", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic4", "MAXIMUM1-3", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component5", "filled3", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("filled3", "canonicalLineate2", "FORM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component5", "stable5", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("restkomponentenSet", "component6", "RESTKOMPONENTE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component6", "filled4", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("filled4", "canonicalLineate3", "FORM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component6", "elastic5", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic5", "MAXIMUM1-4", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic5", "MINIMUM0-5", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component6", "stable6", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("arch", "component1", "LEFT_SUPPORT");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("arch", "component7", "LEFT_VOUSSOIR");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component7", "null1", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component7", "stable7", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component7", "inelastic2", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("inelastic2", "COUNT0-1", "COUNT");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("arch", "component8", "RIGHT_SUPPORT");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component8", "elastic6", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic6", "MINIMUM0-6", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic6", "MAXIMUM1-5", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component8", "open3", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("open3", "coherent2", "COHERENCE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component8", "stable8", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("arch", "component9", "RIGHT_VOUSSOIR");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component9", "open4", "FILLEDNESS");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("open4", "coherent3", "COHERENCE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component9", "elastic7", "ELASTICITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic7", "MINIMUM0-7", "MINIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("elastic7", "MAXIMUM3-1", "MAXIMUM");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("component9", "stable9", "STABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("desmeme", "edge", "STRICTURE");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("edge", "COUNT2-1", "COUNT");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("edge", "morphologicalConstituent", "CONSTITUENT");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("desmeme", "notViolable", "VIOLABILITY");
$ChacoboNonInterruptibleByNP_719->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");

my $ChichewaVerbMOR = Graph->new(multiedged => 1);
$ChichewaVerbMOR->set_graph_attribute("name", "ChichewaVerbMOR");
$ChichewaVerbMOR->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
$ChichewaVerbMOR->add_edge_by_id("desmeme", "order", "STRICTURE");
$ChichewaVerbMOR->add_edge_by_id("order", "COUNT7-1", "COUNT");
$ChichewaVerbMOR->add_edge_by_id("order", "morphosyntacticConstituent", "CONSTITUENT");
$ChichewaVerbMOR->add_edge_by_id("order", "simple", "RELATIONS");
$ChichewaVerbMOR->add_edge_by_id("desmeme", "notViolable", "VIOLABILITY");
$ChichewaVerbMOR->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$ChichewaVerbMOR->add_edge_by_id("arch", "component1", "LEFT_VOUSSOIR");
$ChichewaVerbMOR->add_edge_by_id("component1", "elastic1", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$ChichewaVerbMOR->add_edge_by_id("elastic1", "MAXIMUM1-1", "MAXIMUM");
$ChichewaVerbMOR->add_edge_by_id("component1", "open1", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("open1", "coherent1", "COHERENCE");
$ChichewaVerbMOR->add_edge_by_id("component1", "stable1", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("arch", "component2", "RIGHT_VOUSSOIR");
$ChichewaVerbMOR->add_edge_by_id("component2", "null1", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("component2", "stable2", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("component2", "inelastic1", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("inelastic1", "COUNT0-1", "COUNT");
$ChichewaVerbMOR->add_edge_by_id("arch", "component3", "RIGHT_SUPPORT");
$ChichewaVerbMOR->add_edge_by_id("component3", "inelastic2", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("inelastic2", "COUNT1-1", "COUNT");
$ChichewaVerbMOR->add_edge_by_id("component3", "open2", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("open2", "coherent2", "COHERENCE");
$ChichewaVerbMOR->add_edge_by_id("component3", "stable3", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("arch", "component4", "LEFT_SUPPORT");
$ChichewaVerbMOR->add_edge_by_id("component4", "elastic2", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("elastic2", "MAXIMUM1-2", "MAXIMUM");
$ChichewaVerbMOR->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$ChichewaVerbMOR->add_edge_by_id("component4", "filled1", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("filled1", "canonicalLineate1", "FORM");
$ChichewaVerbMOR->add_edge_by_id("component4", "stable4", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("arch", "component3", "KEYSTONE");
$ChichewaVerbMOR->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$ChichewaVerbMOR->add_edge_by_id("restkomponentenSet", "component5", "RESTKOMPONENTE");
$ChichewaVerbMOR->add_edge_by_id("component5", "stable5", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("component5", "elastic3", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("elastic3", "MINIMUM0-3", "MINIMUM");
$ChichewaVerbMOR->add_edge_by_id("elastic3", "MAXIMUM1-3", "MAXIMUM");
$ChichewaVerbMOR->add_edge_by_id("component5", "open3", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("open3", "coherent3", "COHERENCE");
$ChichewaVerbMOR->add_edge_by_id("restkomponentenSet", "component6", "RESTKOMPONENTE");
$ChichewaVerbMOR->add_edge_by_id("component6", "open4", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("open4", "coherent4", "COHERENCE");
$ChichewaVerbMOR->add_edge_by_id("component6", "inelastic3", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("inelastic3", "COUNT1-2", "COUNT");
$ChichewaVerbMOR->add_edge_by_id("component6", "stable6", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("restkomponentenSet", "component7", "RESTKOMPONENTE");
$ChichewaVerbMOR->add_edge_by_id("component7", "elastic4", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("elastic4", "MAXIMUM1-4", "MAXIMUM");
$ChichewaVerbMOR->add_edge_by_id("elastic4", "MINIMUM0-4", "MINIMUM");
$ChichewaVerbMOR->add_edge_by_id("component7", "filled2", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("filled2", "canonicalLineate2", "FORM");
$ChichewaVerbMOR->add_edge_by_id("component7", "stable7", "STABILITY");
$ChichewaVerbMOR->add_edge_by_id("restkomponentenSet", "component8", "RESTKOMPONENTE");
$ChichewaVerbMOR->add_edge_by_id("component8", "elastic5", "ELASTICITY");
$ChichewaVerbMOR->add_edge_by_id("elastic5", "MINIMUM0-5", "MINIMUM");
$ChichewaVerbMOR->add_edge_by_id("elastic5", "MAXIMUM1-5", "MAXIMUM");
$ChichewaVerbMOR->add_edge_by_id("component8", "open5", "FILLEDNESS");
$ChichewaVerbMOR->add_edge_by_id("open5", "coherent5", "COHERENCE");
$ChichewaVerbMOR->add_edge_by_id("component8", "stable8", "STABILITY");



# Initialize simList
my $initialS = new GraphJG::SimilarityJG(graph => [$ChacoboNonInterruptibleByNP_719,$ChichewaVerbMOR]);
my $initialMethod = $initialS->use('SimilarityFlooding');
$initialMethod->setNumOfIteration(1);
$initialMethod->calculate();
my %simList = $initialMethod->getAllSimilarities;


my %sims;
for (my $count = 0; $count <=20; $count++) {

	my $s = new GraphJG::SimilarityJG(graph => [$ChacoboNonInterruptibleByNP_719,$ChichewaVerbMOR]);
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
	#print "Count: $count\n";	
	#print "$eucDist\n";

	#$method->showNonZeroSimilarities($ChechenPreverbalA,$MandeClause);
	my %newSims = $method->returnAllSimilarities($ChacoboNonInterruptibleByNP_719,$ChichewaVerbMOR);
	for my $node (keys(%newSims)) {
	
		if (exists($sims{$node})) {
			my @oldSimList = @{$sims{$node}};
			push(@oldSimList, nearest(.01, $newSims{$node}));
			$sims{$node} = \@oldSimList;
						
			}
	
		else{
			my @newSimList = (nearest(.01, $newSims{$node}));
			$sims{$node} = \@newSimList;
			
			}
	
		}
	
	if ($eucDist != 0 and $eucDist < .05) {
		last;	
		}
	
	%simList = %newSimList;
	
	}

# We collected the whole list, but we'll only report the last iteration for now, hence the [-1]
print "\\begin{tabular}{>{\\em}lrrrrrrrrrrrrrrrrrrrr}\n";
print "\\Hline\n";
#print "{\\sc node\$\\downarrow\$\\\phantom{ent1/com}iter\$\\rightarrow\$}\t\&\t{\\sc  0}\&\t{\\sc  1}\&\t{\\sc  2}\&\t{\\sc  3}\&\t{\\sc  4} \\\\\n";
print "{\\sc chacobo/chichwewa}\t\&\t{\\sc  similarity}\\\\\n";
print "\\Hline\n";
my @orderedSims = sort { @{$sims{$b}}[-1] <=>  @{$sims{$a}}[-1] } keys(%sims);
for my $sim (@orderedSims) {
	#print "$sim \t\&\t".join("\t&\t", @{$sims{$sim}})."\t\\\\\n" if @{$sims{$sim}}[-1] > .1;
	print "$sim \t\&\t".@{$sims{$sim}}[-1]."\t\\\\\n" if @{$sims{$sim}}[-1] > .1;
	}
print "\\Hline\n";
print "\\end{tabular}\n";
