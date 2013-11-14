#! /usr/bin/perl

use FindBin;  # locate this script
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;


my $g1 = Graph->new(multiedged => 1);
# $g1->add_edge_by_id("desmeme", "order", "STRICTURE");
# $g1->add_edge_by_id("desmeme", "arch", "FOUNDATION");
# $g1->add_edge_by_id("desmeme", "constructionalConditioning", "CONDITIONING");
# $g1->add_edge_by_id("desmeme", "notViolable", "VIOLABILITY");
# $g1->add_edge_by_id("component3", "inelastic3", "ELASTICITY");
# $g1->add_edge_by_id("component1", "stable1", "STABILITY");
# $g1->add_edge_by_id("component1", "open1", "FILLEDNESS");
# $g1->add_edge_by_id("component3", "inelastic3", "ELASTICITY");
# $g1->add_edge_by_id("component3", "open2", "FILLEDNESS");
# $g1->add_edge_by_id("component3", "stable3", "STABILITY");
# $g1->add_edge_by_id("component2", "null1", "FILLEDNESS");
# $g1->add_edge_by_id("component2", "stable2", "STABILITY");
# $g1->add_edge_by_id("component2", "inelastic2", "ELASTICITY");
# $g1->add_edge_by_id("inelastic1", "COUNT1-1", "COUNT");
# $g1->add_edge_by_id("inelastic2", "COUNT0-1", "COUNT");
# $g1->add_edge_by_id("inelastic3", "COUNT1-2", "COUNT");
# $g1->add_edge_by_id("arch", "component1", "RIGHT_VOUSSOIR");
# $g1->add_edge_by_id("arch", "component1", "RIGHT_VOUSSOIR");
# $g1->add_edge_by_id("arch", "component2", "LEFT_VOUSSOIR");
# $g1->add_edge_by_id("arch", "component3", "LEFT_SUPPORT");
# $g1->add_edge_by_id("arch", "component3", "LEFT_SUPPORT");
# $g1->add_edge_by_id("open1", "coherent1", "COHERENCE");
# $g1->add_edge_by_id("order", "prosodicWord", "CONSTITUENT");
# $g1->add_edge_by_id("order", "simple", "RELATIONS");
# $g1->add_edge_by_id("order", "COUNT2-1", "COUNT");
# $g1->add_edge_by_id("open2", "coherent2", "COHERENCE");

$g1->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$g1->add_edge_by_id("desmeme", "potentiallyViolable", "VIOLABILITY");
$g1->add_edge_by_id("desmeme", "prosodicConditioning", "CONDITIONING");
$g1->add_edge_by_id("desmeme", "order", "STRICTURE");
$g1->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$g1->add_edge_by_id("elastic2", "MAXIMUM1-2", "MAXIMUM");
$g1->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$g1->add_edge_by_id("elastic1", "MAXIMUM1-1", "MAXIMUM");
$g1->add_edge_by_id("component4", "open3", "FILLEDNESS");
$g1->add_edge_by_id("component4", "inelastic2", "ELASTICITY");
$g1->add_edge_by_id("component4", "stable2", "STABILITY");
$g1->add_edge_by_id("component1", "unstable1", "STABILITY");
$g1->add_edge_by_id("component1", "elastic2", "ELASTICITY");
$g1->add_edge_by_id("component1", "open2", "FILLEDNESS");
$g1->add_edge_by_id("component3", "inelastic1", "ELASTICITY");
$g1->add_edge_by_id("component3", "stable1", "STABILITY");
$g1->add_edge_by_id("component3", "null1", "FILLEDNESS");
$g1->add_edge_by_id("component2", "elastic1", "ELASTICITY");
$g1->add_edge_by_id("component2", "open1", "FILLEDNESS");
$g1->add_edge_by_id("component2", "unstable2", "STABILITY");
$g1->add_edge_by_id("unstable1", "component2", "ASSOCIATE");
$g1->add_edge_by_id("unstable1", "right", "ASSOCIATE_POSITION");
$g1->add_edge_by_id("inelastic1", "COUNT0-1", "COUNT");
$g1->add_edge_by_id("inelastic2", "COUNT1-1", "COUNT");
$g1->add_edge_by_id("unstable2", "left", "ASSOCIATE_POSITION");
$g1->add_edge_by_id("unstable2", "component1", "ASSOCIATE");



$g1->add_edge_by_id("a", "a1", "l1");
$g1->add_edge_by_id("a", "a2", "l1");
$g1->add_edge_by_id("a1", "a2", "l2");



 my $g2 = Graph->new(multiedged => 1);
$g2->add_edge_by_id("desmeme", "arch", "FOUNDATION");
$g2->add_edge_by_id("desmeme", "potentiallyViolable", "VIOLABILITY");
$g2->add_edge_by_id("desmeme", "prosodicConditioning", "CONDITIONING");
$g2->add_edge_by_id("desmeme", "order", "STRICTURE");
$g2->add_edge_by_id("elastic2", "MINIMUM0-2", "MINIMUM");
$g2->add_edge_by_id("elastic2", "MAXIMUM1-2", "MAXIMUM");
$g2->add_edge_by_id("elastic1", "MINIMUM0-1", "MINIMUM");
$g2->add_edge_by_id("elastic1", "MAXIMUM1-1", "MAXIMUM");
$g2->add_edge_by_id("component4", "open3", "FILLEDNESS");
$g2->add_edge_by_id("component4", "inelastic2", "ELASTICITY");
$g2->add_edge_by_id("component4", "stable2", "STABILITY");
$g2->add_edge_by_id("component1", "unstable1", "STABILITY");
$g2->add_edge_by_id("component1", "elastic2", "ELASTICITY");
$g2->add_edge_by_id("component1", "open2", "FILLEDNESS");
$g2->add_edge_by_id("component3", "inelastic1", "ELASTICITY");
$g2->add_edge_by_id("component3", "stable1", "STABILITY");
$g2->add_edge_by_id("component3", "null1", "FILLEDNESS");
$g2->add_edge_by_id("component2", "elastic1", "ELASTICITY");
$g2->add_edge_by_id("component2", "open1", "FILLEDNESS");
$g2->add_edge_by_id("component2", "unstable2", "STABILITY");
$g2->add_edge_by_id("unstable1", "component2", "ASSOCIATE");
$g2->add_edge_by_id("unstable1", "right", "ASSOCIATE_POSITION");
$g2->add_edge_by_id("inelastic1", "COUNT0-1", "COUNT");
$g2->add_edge_by_id("inelastic2", "COUNT1-1", "COUNT");
$g2->add_edge_by_id("unstable2", "left", "ASSOCIATE_POSITION");
$g2->add_edge_by_id("unstable2", "component1", "ASSOCIATE");
$g2->add_edge_by_id("potentiallyViolable", "noKnownExceptions", "EXCEPTIONALITY");
$g2->add_edge_by_id("potentiallyViolable", "phonologicalRepair", "REPARABILITY");
$g2->add_edge_by_id("arch", "component1", "RIGHT_VOUSSOIR");
$g2->add_edge_by_id("arch", "component3", "LEFT_VOUSSOIR");
$g2->add_edge_by_id("arch", "component4", "LEFT_SUPPORT");
$g2->add_edge_by_id("arch", "component2", "RIGHT_SUPPORT");
$g2->add_edge_by_id("arch", "component4", "LEFT_SUPPORT");
$g2->add_edge_by_id("open1", "coherent1", "COHERENCE");
$g2->add_edge_by_id("order", "simple", "RELATIONS");
$g2->add_edge_by_id("order", "COUNT3-1", "COUNT");
$g2->add_edge_by_id("order", "segment", "CONSTITUENT");
$g2->add_edge_by_id("open3", "coherent3", "COHERENCE");
$g2->add_edge_by_id("open2", "coherent2", "COHERENCE");

#$g2->add_edge_by_id("a", "b1", "l1");
#$g2->add_edge_by_id("a", "b2", "l2");
#$g2->add_edge_by_id("b2", "b1", "l2");

# $g2->add_edge_by_id("a", "a1", "l1");
# $g2->add_edge_by_id("a", "a2", "l1");
# $g2->add_edge_by_id("a1", "a2", "l2");


my $s = new GraphJG::SimilarityJG(graph => [$g1,$g2]);
my $method = $s->use('SimilarityFlooding');

$method->setNumOfIteration(100);

$method->calculate();

print "Flooding\n";
$method->showLargeSimilarities;
print "\n";