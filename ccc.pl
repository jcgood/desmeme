#! /usr/bin/perl

use Graph;
use Graph::Similarity;



    my $g1 = Graph->new;
    $g1->add_vertices("A","B","C");
    $g1->add_edges(['A', 'B'], ['B','C']);

    my $g2 = Graph->new;
    $g2->add_vertices("a","b","c","d","e");
    $g2->add_edges(['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e']);

    my $s = new Graph::Similarity(graph => [$g1, $g2]);

    my $method = $s->use('CoupledNodeEdgeScoring');
    $method->calculate();
    $method->showAllSimilarities;

    #===============================================
    # Or by Similarity Flooding 
    my $g1 = Graph->new(multiedged => 1);
    $g1->add_vertices("I","coffee","apple","swim");
    $g1->add_edge_by_id("I", "coffee", "drink");
    $g1->add_edge_by_id("I", "swim", "can't");
    $g1->add_edge_by_id("I", "apple", "eat");

    my $g2 = Graph->new(multiedged => 1);
    $g2->add_vertices("she","cake","apple juice","swim");
    $g2->add_edge_by_id("she", "apple juice", "drink");
    $g2->add_edge_by_id("she", "swim", "can");
    $g2->add_edge_by_id("she", "cake", "eat");
    
    my $s = new Graph::Similarity(graph => [$g1,$g2]);
    my $method = $s->use('SimilarityFlooding');
    $method->calculate();
    $method->showAllSimilarities;