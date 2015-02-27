#! /usr/bin/perl

use strict;

use FindBin;  # locate this script
use lib "$FindBin::Bin/.";
use GraphJG::SimilarityJG;


my $g1 = Graph->new(multiedged => 1);
$g1->add_edge_by_id("a", "a1", "l1");
$g1->add_edge_by_id("a", "a2", "l1");
$g1->add_edge_by_id("a1", "a2", "l2");

my $g2 = Graph->new(multiedged => 1);
$g2->add_edge_by_id("a", "b1", "l1");
$g2->add_edge_by_id("a", "b2", "l2");
$g2->add_edge_by_id("b2", "b1", "l2");

# $g2->add_edge_by_id("a", "a1", "l1");
# $g2->add_edge_by_id("a", "a2", "l1");
# $g2->add_edge_by_id("a1", "a2", "l2");





#my $s = new GraphJG::SimilarityJG(graph => [$NimboranVerb,$NimboranVerb]);
#my $method = $s->use('SimilarityFlooding');
#$method->setNumOfIteration(100);
#$method->calculate();

print "Flooding\n";
$method->showLargeSimilarities;
print "\n";