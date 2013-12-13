#! /usr/bin/perl

package GraphJG::SimilarityJG::SimilarityFloodingJG;

use strict;
use warnings;

use Graph;
use Moose;
use Text::Levenshtein qw(distance);

our $VERSION = '0.02';

with 'GraphJG::SimilarityJG::MethodJG';

has 'graph' => (is => 'rw', isa => 'ArrayRef[Graph]', required => 1);

__PACKAGE__->meta->make_immutable;
no Moose;

sub calculate {
    my $self = shift;

    # Store similarity matrix $sim{vertex1}{vertex2} 
    my %sim; 
    my $itr = $self->num_of_iteration;
    my $g = $self->graph;
    my $g1 = $$g[0];
    my $g2 = $$g[1];

    # Create InitialMap
    # Similarity is calculated by 1 - (edit distnace(stringA, stringB) / length of the stringA + stringB)
    # This calcualtion can be changed
    for my $v1 ($g1->vertices){
        for my $v2 ($g2->vertices){
            #$sim{$v1}{$v2} = 1 - (distance($v1, $v2) / length("$v1$v2"));
            #print "$v1-$v2\n";
            #$sim{$v1}{$v2} = 1;
            
            my $normv1 = $v1;
            my $normv2 = $v2;
            
            
            $normv1 =~ s/(\w+?)(\d*)(-\d*)?$/$1/;
            $normv2 =~ s/(\w+?)(\d*)(-\d*)?$/$1/;
            
            # Try to handle "-a1" style suffixes, too--not tested!
            #$normv1 =~ s/(\w+?)(-\w\d*)(-\d*)?$/$1/;
            #$normv2 =~ s/(\w+?)(-\w\d*)(-\d*)?$/$1/;


            #print "Normed: $normv1, $normv2\n";
            
            if ($normv1 eq $normv2) {
            	$sim{$v1}{$v2} = 1;
            	}
            	
            else{ $sim{$v1}{$v2} = .5; } # More points if labels match, makes a difference if spreading is neural-like
            						# .5 is quasi-arbitrary, in future one could exploit ontological taxonomy
            
        }
    }

    # Create Pairwise Connectivity Graph
    my $pcg = Graph->new(multiedged => 1);

    # First, collect source, destination node and label
    # The is for Graph1
    my %m1;
    my %labels;
    for my $v1 ($g1->vertices){
        for my $p1 ($g1->predecessors($v1)){
            for my $label ($g1->get_multiedge_ids($p1, $v1)){
                # {"LABEL"}{"SOURCE NODE"}{"DESTINATION NODE"}
                $m1{$label}{$p1}{$v1} = 1; # There is no meaing to put 1. Just want to pickup unique key later
                $labels{$label} = 1;
            }
        }
    }
    # For Graph2
    my %m2;
    my @labels;
    for my $v2 ($g2->vertices){
        for my $p2 ($g2->predecessors($v2)){
            for my $label ($g2->get_multiedge_ids($p2, $v2)){
                # {"LABEL"}{"SOURCE NODE"}{"DESTINATION NODE"}
                $m2{$label}{$p2}{$v2} = 1;
                $labels{$label} = 1;
            }
        }
    }

    # Second, add pairwise node.
    # Node name is src1(from graph1)/src2(from graph2) or dest1(from graph1)/dest2(from graph2)
    # %edges used for counting the label of neighbors
    my %edges;
    my %outgoing; # JG: Adding to test different model
    for my $label (keys %labels) {
        #print $label, "------\n";
        for my $src1 (keys %{$m1{$label}}){
            for my $src2 (keys %{$m2{$label}}){
                for my $dest1 (keys %{$m1{$label}{$src1}}){
                    for my $dest2 (keys %{$m2{$label}{$src2}}){
                        #print "src - $src1,$src2\n";
                        #print "dest - $dest1,$dest2\n";
                        $pcg->add_edge_by_id("$src1/$src2", "$dest1/$dest2", $label ); # JG: The algorithm has bidirectional flooding, so we enter as two-way edge
                        $pcg->add_edge_by_id("$dest1/$dest2", "$src1/$src2", $label ); 
                        $edges{"$src1/$src2"}{$label}++; #JG" For a given edge label figure out how many lead to/from that node
                        $edges{"$dest1/$dest2"}{$label}++;
                        $outgoing{"$src1/$src2"}++; # For a different algorithm than published, with all outgoing nodes counting in weight not just those from matching labels
                        $outgoing{"$dest1/$dest2"}++;
                        #print "src1/src2: $src1/$src2\n";
                    }
                }
            }
        }
    }



    # Start iteration 
    for (my $i=0; $i<$itr; $i++){
    
        # Based on label info, create the logic to behave as the same as "Induced Propagation Graph" in the paper
        my $max=0;
        my %next_sim;
        for my $v1 ($g1->vertices){
            for my $v2 ($g2->vertices){

                my $sum=0;
                for my $n ($pcg->neighbours("$v1/$v2")){ # JG: Only resolves if the dual-label has edges
                    #my $count = 0;
                    for my $label ($pcg->get_multiedge_ids($n, "$v1/$v2")){ # JG: In case there's more than one edge connecting to nodes
                    	#print "$n $label\n";
                        #print 1/$edges{$n}{$label};
                        #print " * $n : neighbor of $v1/$v2\n";
                        #print "\n";
                        my ($n1, $n2) = split /\//, $n;
                        #$sum += $sim{$n1}{$n2} / $edges{$n}{$label}; # Original implementation, matches what is in paper (though technical report opens up possibility of different weightings)
                        $sum += $sim{$n1}{$n2} / $outgoing{"$n"}; # JG: changing algo divide by all outgoing, more "network-like"
						#print "n: $n, n1: $n1, n2: $n2, v1/v2: $v1/$v2\n";
						#print $outgoing{"$n"}.", ".$edges{$n}{$label}."\n";
						#$count++;
                    }
                    
                #print "Count: $count\n\n";
                }

                $next_sim{$v1}{$v2} = $sim{$v1}{$v2} + $sum; 
                if ($max < $next_sim{$v1}{$v2}){
                    $max = $next_sim{$v1}{$v2};
                	#print "Max: $max\n";
                }
            }
        }


        # Normalizing
        # Deviding the maximum value
        for my $v1 ($g1->vertices){
            for my $v2 ($g2->vertices){

                if (defined $next_sim{$v1}{$v2}){
                    #print "$v1/$v2 Old:".$sim{$v1}{$v2}." New: ".$next_sim{$v1}{$v2}."\n";
                    $sim{$v1}{$v2} = $next_sim{$v1}{$v2} / $max;
                }
                else {
                    print "I am undefined\n"; #JG: I'm not sure we ever get here.
                    $sim{$v1}{$v2} = $sim{$v1}{$v2} / $max;
                }
            
            }
                   
        } 

    }

    $self->_setSimilarity(\%sim);
    $self->_setPCG($pcg);

    #return \%sim;
    #return 1;
}



1;