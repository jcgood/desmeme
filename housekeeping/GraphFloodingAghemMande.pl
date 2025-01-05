use strict;
use FindBin;
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;
use Math::Round;


my $AghemClause = Graph->new(multiedged => 1);
$AghemClause->set_graph_attribute("name", "AghemClause");
$AghemClause->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
$AghemClause->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$AghemClause->add_edge_by_id("arch", "component1", "RIGHT_SUPPORT");
$AghemClause->add_edge_by_id("component1", "elastic1", "ELASTICITY");
$AghemClause->add_edge_by_id("elastic1", "MAXIMUM100-1", "MAXIMUM");
$AghemClause->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$AghemClause->add_edge_by_id("component1", "open1", "FILLEDNESS");
$AghemClause->add_edge_by_id("open1", "coherent1", "COHERENCE");
$AghemClause->add_edge_by_id("component1", "stable1", "STABILITY");
$AghemClause->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$AghemClause->add_edge_by_id("restkomponentenSet", "component2", "RESTKOMPONENTE");
$AghemClause->add_edge_by_id("component2", "stable2", "STABILITY");
$AghemClause->add_edge_by_id("component2", "elastic2", "ELASTICITY");
$AghemClause->add_edge_by_id("elastic2", "MAXIMUM1-1", "MAXIMUM");
$AghemClause->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$AghemClause->add_edge_by_id("component2", "open2", "FILLEDNESS");
$AghemClause->add_edge_by_id("open2", "coherent2", "COHERENCE");
$AghemClause->add_edge_by_id("arch", "component3", "LEFT_VOUSSOIR");
$AghemClause->add_edge_by_id("component3", "open3", "FILLEDNESS");
$AghemClause->add_edge_by_id("open3", "coherent3", "COHERENCE");
$AghemClause->add_edge_by_id("component3", "elastic3", "ELASTICITY");
$AghemClause->add_edge_by_id("elastic3", "MINIMUM0-3", "MINIMUM");
$AghemClause->add_edge_by_id("elastic3", "MAXIMUM100-2", "MAXIMUM");
$AghemClause->add_edge_by_id("component3", "stable3", "STABILITY");
$AghemClause->add_edge_by_id("arch", "component4", "LEFT_SUPPORT");
$AghemClause->add_edge_by_id("component4", "stable4", "STABILITY");
$AghemClause->add_edge_by_id("component4", "inelastic1", "ELASTICITY");
$AghemClause->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$AghemClause->add_edge_by_id("component4", "open4", "FILLEDNESS");
$AghemClause->add_edge_by_id("open4", "coherent4", "COHERENCE");
$AghemClause->add_edge_by_id("arch", "component5", "KEYSTONE");
$AghemClause->add_edge_by_id("component5", "inelastic2", "ELASTICITY");
$AghemClause->add_edge_by_id("inelastic2", "COUNT1-2", "COUNT");
$AghemClause->add_edge_by_id("component5", "stable5", "STABILITY");
$AghemClause->add_edge_by_id("component5", "open5", "FILLEDNESS");
$AghemClause->add_edge_by_id("open5", "coherent5", "COHERENCE");
$AghemClause->add_edge_by_id("arch", "component6", "RIGHT_VOUSSOIR");
$AghemClause->add_edge_by_id("component6", "inelastic3", "ELASTICITY");
$AghemClause->add_edge_by_id("inelastic3", "COUNT1-3", "COUNT");
$AghemClause->add_edge_by_id("component6", "unstable1", "STABILITY");
$AghemClause->add_edge_by_id("unstable1", "left", "ASSOCIATE_POSITION");
$AghemClause->add_edge_by_id("unstable1", "component2", "ASSOCIATE");
$AghemClause->add_edge_by_id("component6", "open6", "FILLEDNESS");
$AghemClause->add_edge_by_id("open6", "coherent6", "COHERENCE");
$AghemClause->add_edge_by_id("desmeme", "order", "STRICTURE");
$AghemClause->add_edge_by_id("order", "simple", "RELATIONS");
$AghemClause->add_edge_by_id("order", "COUNT6-1", "COUNT");
$AghemClause->add_edge_by_id("order", "syntacticConstituent", "CONSTITUENT");
$AghemClause->add_edge_by_id("desmeme", "potentiallyViolable", "VIOLABILITY");
$AghemClause->add_edge_by_id("potentiallyViolable", "lexical", "EXCEPTIONALITY");
$AghemClause->add_edge_by_id("potentiallyViolable", "morphosyntacticInsertion", "REPARABILITY");


my $MandeClause = Graph->new(multiedged => 1);
$MandeClause->set_graph_attribute("name", "MandeClause");
$MandeClause->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$MandeClause->add_edge_by_id("arch", "component1", "LEFT_SUPPORT");
$MandeClause->add_edge_by_id("component1", "inelastic1", "ELASTICITY");
$MandeClause->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$MandeClause->add_edge_by_id("component1", "stable1", "STABILITY");
$MandeClause->add_edge_by_id("component1", "open1", "FILLEDNESS");
$MandeClause->add_edge_by_id("open1", "coherent1", "COHERENCE");
$MandeClause->add_edge_by_id("arch", "component2", "RIGHT_VOUSSOIR");
$MandeClause->add_edge_by_id("component2", "open2", "FILLEDNESS");
$MandeClause->add_edge_by_id("open2", "incoherent1", "COHERENCE");
$MandeClause->add_edge_by_id("component2", "stable2", "STABILITY");
$MandeClause->add_edge_by_id("component2", "elastic1", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic1", "MAXIMUM100-1", "MAXIMUM");
$MandeClause->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$MandeClause->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$MandeClause->add_edge_by_id("restkomponentenSet", "component3", "RESTKOMPONENTE");
$MandeClause->add_edge_by_id("component3", "stable3", "STABILITY");
$MandeClause->add_edge_by_id("component3", "elastic2", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$MandeClause->add_edge_by_id("elastic2", "MAXIMUM1-1", "MAXIMUM");
$MandeClause->add_edge_by_id("component3", "open3", "FILLEDNESS");
$MandeClause->add_edge_by_id("open3", "coherent2", "COHERENCE");
$MandeClause->add_edge_by_id("arch", "component4", "KEYSTONE");
$MandeClause->add_edge_by_id("component4", "inelastic2", "ELASTICITY");
$MandeClause->add_edge_by_id("inelastic2", "COUNT1-2", "COUNT");
$MandeClause->add_edge_by_id("component4", "stable4", "STABILITY");
$MandeClause->add_edge_by_id("component4", "open4", "FILLEDNESS");
$MandeClause->add_edge_by_id("open4", "coherent3", "COHERENCE");
$MandeClause->add_edge_by_id("arch", "component2", "RIGHT_SUPPORT");
$MandeClause->add_edge_by_id("arch", "component5", "LEFT_VOUSSOIR");
$MandeClause->add_edge_by_id("component5", "open5", "FILLEDNESS");
$MandeClause->add_edge_by_id("open5", "coherent4", "COHERENCE");
$MandeClause->add_edge_by_id("component5", "elastic3", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic3", "MINIMUM0-3", "MINIMUM");
$MandeClause->add_edge_by_id("elastic3", "MAXIMUM1-2", "MAXIMUM");
$MandeClause->add_edge_by_id("component5", "stable5", "STABILITY");
$MandeClause->add_edge_by_id("desmeme", "order", "STRICTURE");
$MandeClause->add_edge_by_id("order", "COUNT5-1", "COUNT");
$MandeClause->add_edge_by_id("order", "simple", "RELATIONS");
$MandeClause->add_edge_by_id("order", "syntacticConstituent", "CONSTITUENT");
$MandeClause->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
$MandeClause->add_edge_by_id("desmeme", "notViolable", "VIOLABILITY");


# Initialize simList
my $initialS = new GraphJG::SimilarityJG(graph => [$AghemClause,$MandeClause]);
my $initialMethod = $initialS->use('SimilarityFlooding');
$initialMethod->setNumOfIteration(1);
$initialMethod->calculate();
my %simList = $initialMethod->getAllSimilarities;


my %sims;
for (my $count = 0; $count <=20; $count++) {

	my $s = new GraphJG::SimilarityJG(graph => [$AghemClause,$MandeClause]);
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

	#$method->showNonZeroSimilarities($AghemClause,$MandeClause);
	my %newSims = $method->returnAllSimilarities($AghemClause,$MandeClause);
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

# All iterations print
# print "\\begin{tabular}{>{\\em}lrrrrrrrrrrrrrrrrrrrr}\n";
# print "\\Hline\n";
# print "{\\sc node\$\\downarrow\$\\\phantom{ent1/com}iter\$\\rightarrow\$}\t\&\t{\\sc  0}\&\t{\\sc  1}\&\t{\\sc  2}\&\t{\\sc  3}\&\t{\\sc  4} \\\\\n";
# print "\\Hline\n";
# for my $sim (sort(keys(%sims))) {
# 	print "$sim \t\&\t".join("\t&\t", @{$sims{$sim}})."\t\\\\\n" if @{$sims{$sim}}[-1] > .1;
# 	}
# print "\\Hline\n";
# print "\\end{tabular}\n";

# Last iteration prints
# We collected the whole list, but we'll only report the last iteration for now, hence the [-1]
print "\\begin{tabular}{>{\\em}lrrrrrrrrrrrrrrrrrrrr}\n";
print "\\Hline\n";
print "{\\sc aghem/mande}\t\&\t{\\sc  similarity}\\\\\n";
print "\\Hline\n";
my @orderedSims = sort { @{$sims{$b}}[-1] <=>  @{$sims{$a}}[-1] } keys(%sims);
for my $sim (@orderedSims) {
	print "$sim \t\&\t".@{$sims{$sim}}[-1]."\t\\\\\n" if @{$sims{$sim}}[-1] > .1;
	}
print "\\Hline\n";
print "\\end{tabular}\n";
