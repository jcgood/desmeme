use strict;
use FindBin;
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;
use Math::Round;


my $MandeClause = Graph->new(multiedged => 1);
$MandeClause->set_graph_attribute("name", "MandeClause");
$MandeClause->add_edge_by_id("desmeme", "order", "STRICTURE");
$MandeClause->add_edge_by_id("order", "syntacticConstituent", "CONSTITUENT");
$MandeClause->add_edge_by_id("order", "simple", "RELATIONS");
$MandeClause->add_edge_by_id("order", "COUNT5-1", "COUNT");
$MandeClause->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$MandeClause->add_edge_by_id("arch", "component1", "LEFT_SUPPORT");
$MandeClause->add_edge_by_id("component1", "inelastic1", "ELASTICITY");
$MandeClause->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$MandeClause->add_edge_by_id("component1", "open1", "FILLEDNESS");
$MandeClause->add_edge_by_id("open1", "coherent1", "COHERENCE");
$MandeClause->add_edge_by_id("component1", "stable1", "STABILITY");
$MandeClause->add_edge_by_id("arch", "restkomponentenSet", "RESTKOMPONENTEN");
$MandeClause->add_edge_by_id("restkomponentenSet", "component2", "RESTKOMPONENT");
$MandeClause->add_edge_by_id("component2", "elastic1", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$MandeClause->add_edge_by_id("elastic1", "MAXIMUM1-1", "MAXIMUM");
$MandeClause->add_edge_by_id("component2", "open2", "FILLEDNESS");
$MandeClause->add_edge_by_id("open2", "coherent2", "COHERENCE");
$MandeClause->add_edge_by_id("component2", "stable2", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component3", "LEFT_VOUSSOIR");
$MandeClause->add_edge_by_id("component3", "elastic2", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$MandeClause->add_edge_by_id("elastic2", "MAXIMUM1-2", "MAXIMUM");
$MandeClause->add_edge_by_id("component3", "open3", "FILLEDNESS");
$MandeClause->add_edge_by_id("open3", "coherent3", "COHERENCE");
$MandeClause->add_edge_by_id("component3", "stable3", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component4", "RIGHT_VOUSSOIR");
$MandeClause->add_edge_by_id("component4", "elastic3", "ELASTICITY");
$MandeClause->add_edge_by_id("elastic3", "MINIMUM0-3", "MINIMUM");
$MandeClause->add_edge_by_id("elastic3", "MAXIMUM100-1", "MAXIMUM");
$MandeClause->add_edge_by_id("component4", "open4", "FILLEDNESS");
$MandeClause->add_edge_by_id("open4", "incoherent1", "COHERENCE");
$MandeClause->add_edge_by_id("component4", "stable4", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component5", "KEYSTONE");
$MandeClause->add_edge_by_id("component5", "inelastic2", "ELASTICITY");
$MandeClause->add_edge_by_id("inelastic2", "COUNT1-2", "COUNT");
$MandeClause->add_edge_by_id("component5", "open5", "FILLEDNESS");
$MandeClause->add_edge_by_id("open5", "coherent4", "COHERENCE");
$MandeClause->add_edge_by_id("component5", "stable5", "STABILITY");
$MandeClause->add_edge_by_id("arch", "component4", "RIGHT_SUPPORT");
$MandeClause->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
$MandeClause->add_edge_by_id("desmeme", "notViolable", "VIOLABILITY");


my $ChechenPreverbalA = Graph->new(multiedged => 1);
$ChechenPreverbalA->set_graph_attribute("name", "ChechenPreverbalA");
$ChechenPreverbalA->add_edge_by_id("desmeme", "span", "FOUNDATION");
$ChechenPreverbalA->add_edge_by_id("span", "component1", "RIGHT_SUPPORT");
$ChechenPreverbalA->add_edge_by_id("component1", "open1", "FILLEDNESS");
$ChechenPreverbalA->add_edge_by_id("open1", "coherent1", "COHERENCE");
$ChechenPreverbalA->add_edge_by_id("component1", "stable1", "STABILITY");
$ChechenPreverbalA->add_edge_by_id("component1", "inelastic1", "ELASTICITY");
$ChechenPreverbalA->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
$ChechenPreverbalA->add_edge_by_id("span", "component2", "LEFT_SUPPORT");
$ChechenPreverbalA->add_edge_by_id("component2", "stable2", "STABILITY");
$ChechenPreverbalA->add_edge_by_id("component2", "partiallyFilled1", "FILLEDNESS");
$ChechenPreverbalA->add_edge_by_id("partiallyFilled1", "canonicalLineate1", "FORM");
$ChechenPreverbalA->add_edge_by_id("partiallyFilled1", "coherent2", "COHERENCE");
$ChechenPreverbalA->add_edge_by_id("partiallyFilled1", "final1", "FILLER_PLACEMENT");
$ChechenPreverbalA->add_edge_by_id("component2", "inelastic2", "ELASTICITY");
$ChechenPreverbalA->add_edge_by_id("inelastic2", "COUNT1-2", "COUNT");
$ChechenPreverbalA->add_edge_by_id("desmeme", "lexicoconstructionalConditioning", "CONDITIONING");
$ChechenPreverbalA->add_edge_by_id("lexicoconstructionalConditioning", "filledComponentSet", "FILLED_COMPONENTS");
$ChechenPreverbalA->add_edge_by_id("filledComponentSet", "component2", "FILLED_COMPONENT");
$ChechenPreverbalA->add_edge_by_id("lexicoconstructionalConditioning", "medial", "FILLER_POSITION");
$ChechenPreverbalA->add_edge_by_id("desmeme", "length", "STRICTURE");
$ChechenPreverbalA->add_edge_by_id("length", "prosodicWord", "CONSTITUENT");
$ChechenPreverbalA->add_edge_by_id("length", "COUNT2-1", "COUNT");
$ChechenPreverbalA->add_edge_by_id("desmeme", "potentiallyViolable", "VIOLABILITY");
$ChechenPreverbalA->add_edge_by_id("potentiallyViolable", "noKnownExceptions", "EXCEPTIONALITY");
$ChechenPreverbalA->add_edge_by_id("potentiallyViolable", "morphosyntacticInsertion", "REPARABILITY");


# Initialize simList
my $initialS = new GraphJG::SimilarityJG(graph => [$ChechenPreverbalA,$MandeClause]);
my $initialMethod = $initialS->use('SimilarityFlooding');
$initialMethod->setNumOfIteration(1);
$initialMethod->calculate();
my %simList = $initialMethod->getAllSimilarities;


my %sims;
for (my $count = 0; $count <=20; $count++) {

	my $s = new GraphJG::SimilarityJG(graph => [$ChechenPreverbalA,$MandeClause]);
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
	my %newSims = $method->returnAllSimilarities($ChechenPreverbalA,$MandeClause);
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
print "{\\sc chechen/mande}\t\&\t{\\sc  similarity}\\\\\n";
print "\\Hline\n";
my @orderedSims = sort { @{$sims{$b}}[-1] <=>  @{$sims{$a}}[-1] } keys(%sims);
for my $sim (@orderedSims) {
	#print "$sim \t\&\t".join("\t&\t", @{$sims{$sim}})."\t\\\\\n" if @{$sims{$sim}}[-1] > .1;
	print "$sim \t\&\t".@{$sims{$sim}}[-1]."\t\\\\\n" if @{$sims{$sim}}[-1] > .1;
	}
print "\\Hline\n";
print "\\end{tabular}\n";
