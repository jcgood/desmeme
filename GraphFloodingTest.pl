#! /usr/bin/perl
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

my $s = new GraphJG::SimilarityJG(graph => [$g1,$g2]);
my $method = $s->use('SimilarityFlooding');
$method->setNumOfIteration(10);
$method->calculate();

print "Flooding\n";
$method->showAllSimilarities;
print "\n";