#! /usr/bin/perl

use Graph;
use Graph::Similarity;

my $g1 = Graph->new; # Use Graph module
$g1->add_vertices("MINIMUM0-1", "MINIMUM0-3", "MINIMUM0-2", "simple", "desmeme", "MAXIMUM100-1", "MAXIMUM100-2", "elastic3", "elastic2", "elastic1", "coherent6", "lexical", "component5", "component4", "coherent5", "coherent4", "component1", "coherent2", "component3", "component2", "coherent3", "COUNT1-1", "COUNT1-3", "COUNT1-2", "coherent1", "constructionalConditioning", "unstable1", "inelastic1", "inelastic2", "inelastic3", "syntacticConstituent", "potentiallyViolable", "MAXIMUM1-1", "arch", "stable4", "stable5", "open6", "stable1", "stable2", "stable3", "morphosyntacticInsertion", "COUNT6-1", "restkomponentenSet", "component6", "open5", "open4", "left", "open1", "order", "open3", "open2");
$g1->add_edges(["desmeme'", "constructionalConditioning"], ["desmeme'", "arch"], ["desmeme'", "potentiallyViolable"], ["desmeme'", "order"], ["elastic3'", "MINIMUM0-3"], ["elastic3'", "MAXIMUM100-2"], ["elastic2'", "MINIMUM0-2"], ["elastic2'", "MAXIMUM1-1"], ["elastic1'", "MINIMUM0-1"], ["elastic1'", "MAXIMUM100-1"], ["component5'", "stable4"], ["component5'", "elastic3"], ["component5'", "open5"], ["component4'", "stable3"], ["component4'", "inelastic2"], ["component4'", "open4"], ["component1'", "stable1"], ["component1'", "elastic1"], ["component1'", "open1"], ["component3'", "stable2"], ["component3'", "elastic2"], ["component3'", "open2"], ["component2'", "unstable1"], ["component2'", "inelastic1"], ["component2'", "open3"], ["unstable1'", "left"], ["unstable1'", "component3"], ["inelastic1'", "COUNT1-1"], ["inelastic2'", "COUNT1-2"], ["inelastic3'", "COUNT1-3"], ["potentiallyViolable'", "morphosyntacticInsertion"], ["potentiallyViolable'", "lexical"], ["arch'", "component1"], ["arch'", "component2"], ["arch'", "restkomponentenSet"], ["arch'", "component4"], ["arch'", "component5"], ["arch'", "component6"], ["open6'", "coherent6"], ["restkomponentenSet'", "component3"], ["component6'", "stable5"], ["component6'", "inelastic3"], ["component6'", "open6"], ["open5'", "coherent5"], ["open4'", "coherent4"], ["open1'", "coherent1"], ["order'", "simple"], ["order'", "COUNT6-1"], ["order'", "syntacticConstituent"], ["open3'", "coherent3"], ["open2'", "coherent2"]);

my $g2 = Graph->new;
$g2->add_vertices("MINIMUM0-1", "MINIMUM0-2", "semantic", "simple", "desmeme", "elastic2", "elastic1", "filled2", "filled1", "morphologicalConstituent", "null1", "component4", "component1", "component3", "component2", "COUNT1-1", "filledComponentSet", "lexicoconstructionalConditioning", "multiple", "coherent1", "COUNT0-1", "COUNT2-1", "inelastic1", "inelastic2", "potentiallyViolable", "MAXIMUM1-2", "MAXIMUM1-1", "arch", "stable4", "stable1", "stable2", "stable3", "morphosyntacticInsertion", "canonicalLineate1", "canonicalLineate2", "open1", "order");
$g2->add_edges(["desmeme'", "lexicoconstructionalConditioning"], ["desmeme'", "arch"], ["desmeme'", "potentiallyViolable"], ["desmeme'", "order"], ["elastic2'", "MINIMUM0-2"], ["elastic2'", "MAXIMUM1-2"], ["elastic1'", "MINIMUM0-1"], ["elastic1'", "MAXIMUM1-1"], ["filled2'", "canonicalLineate2"], ["filled1'", "canonicalLineate1"], ["component4'", "stable4"], ["component4'", "inelastic2"], ["component4'", "open1"], ["component1'", "stable1"], ["component1'", "elastic1"], ["component1'", "filled1"], ["component3'", "stable3"], ["component3'", "inelastic1"], ["component3'", "null1"], ["component2'", "stable2"], ["component2'", "elastic2"], ["component2'", "filled2"], ["filledComponentSet'", "component1"], ["filledComponentSet'", "component2"], ["lexicoconstructionalConditioning'", "filledComponentSet"], ["lexicoconstructionalConditioning'", "multiple"], ["inelastic1'", "COUNT0-1"], ["inelastic2'", "COUNT1-1"], ["potentiallyViolable'", "semantic"], ["potentiallyViolable'", "morphosyntacticInsertion"], ["arch'", "component3"], ["arch'", "component2"], ["arch'", "component4"], ["arch'", "component1"], ["arch'", "component4"], ["open1'", "coherent1"], ["order'", "simple"], ["order'", "COUNT2-1"], ["order'", "morphologicalConstituent"]);

my $s = new Graph::Similarity(graph => [$g1, $g2]);
my $method = $s->use('CoupledNodeEdgeScoring');

$method->calculate();

print "Coupled Node:\n";
$method->showAllSimilarities;

#===============================================
# Or by Similarity Flooding 
# my $g1 = Graph->new(multiedged => 1);
# $g1->add_vertices("I","coffee","apple","swim");
# $g1->add_edge_by_id("I", "coffee", "drink");
# $g1->add_edge_by_id("I", "swim", "can't");
# $g1->add_edge_by_id("I", "apple", "eat");
# 
# my $g2 = Graph->new(multiedged => 1);
# $g2->add_vertices("she","cake","apple juice","swim");
# $g2->add_edge_by_id("she", "apple juice", "drink");
# $g2->add_edge_by_id("she", "swim", "can");
# $g2->add_edge_by_id("she", "cake", "eat");
# 

print "xxx\n";

 my $s = new Graph::Similarity(graph => [$g1,$g2]);
 my $method = $s->use('SimilarityFlooding');
 $method->calculate();
 $method->showAllSimilarities;