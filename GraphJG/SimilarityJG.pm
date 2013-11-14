#! /usr/bin/perl

# This module is adapted from the Graph::Similarity module posted to CPAN by
# Shohei Kameda. The original copyright and licensing declaration is as follows:

	#Copyright (c) 2012, Shohei Kameda C<< <shoheik@cpan.org> >>. All rights reserved.

	#This module is free software; you can redistribute it and/or
	#modify it under the same terms as Perl itself. See L<perlartistic>.

# I(=Jeff Good) am adapting his implementation of the Similarity Flooding algorithm
# to test for similarities among nodes in template graphs. I have removed his
# implementations of other similarity measures. Per my understanding of the
# Perl Artistic License, I can distribute these modifications without problem
# as long as they are freely available.

# I'm also changing the names a bit so it's clear this is customized from the original.

package GraphJG::SimilarityJG;

use warnings;
use strict;

use version; 
our $VERSION = qv('0.0.5');

use Moose;

use GraphJG::SimilarityJG::SimilarityFloodingJG;


has 'graph' => (is => 'rw', isa => 'ArrayRef[Graph]', required => 1);

__PACKAGE__->meta->make_immutable;
no Moose;

#===========================================================================
# Select which algorithm is used. And make sure the proper graph is used.
# arg1: algorithm - Please check perldoc for more details
#===========================================================================
sub use {
    my ($self, $algo) = @_; 
    my $g = $self->graph;

	my $method;
	if ($algo eq "SimilarityFlooding"){

        die "This algorithm can only applied to two graph\n" if (scalar @$g != 2); 
        die "The graph needs to be multiedged\n" unless ($$g[0]->is_multiedged && $$g[1]->is_multiedged);
        die "The graph needs to be directed graph\n" unless ($$g[0]->is_directed && $$g[1]->is_directed);
        $method = new GraphJG::SimilarityJG::SimilarityFloodingJG(graph => $g);
    }

    return $method;

}
