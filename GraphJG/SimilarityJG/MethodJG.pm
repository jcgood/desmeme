#! /usr/bin/perl

package GraphJG::SimilarityJG::MethodJG;

use Moose::Role;
use Data::Dumper;

requires qw/calculate/;

our $VERSION = '0.02';

has 'num_of_iteration'  => (is => 'rw', isa => 'Int', default => 100);
has 'sim' => (is => 'rw', isa => 'HashRef');
has 'pcg' => (is => 'rw');

no Moose::Role;

# Set number of the iteration. 
sub setNumOfIteration {
    my ($self, $value) = @_;
    $self->num_of_iteration($value);
}

sub showAllSimilarities {
    my $self = shift;
    my $sim = $self->sim;
    for my $i (keys %$sim) {
        for my $j (keys %{$$sim{$i}}) {
            print "$i/$j\t$$sim{$i}{$j}\n";
        }
    }
    #print Dumper $sim;
}


sub showNonZeroSimilarities {
    my $self = shift;
    my $sim = $self->sim;
    for my $i (keys %$sim) {
        for my $j (keys %{$$sim{$i}}) {
            print "$i/$j\t$$sim{$i}{$j}\n" if $$sim{$i}{$j} > 0;
        }
    }
    #print Dumper $sim;
}


# JG: Added this methos
sub getAllSimilarities {
    my $self = shift;
    my $sim = $self->sim;
    my %simList;
    for my $i (keys %$sim) {
        for my $j (keys %{$$sim{$i}}) {
             $simList{$i."/".$j} = $$sim{$i}{$j};
        }
    }
    
    return %simList;
}


# JG: Added this method
sub showLargeSimilarities {
    my $self = shift;
    my $sim = $self->sim;
    my $epsilon = .05;
    for my $i (keys %$sim) {
        for my $j (keys %{$$sim{$i}}) {
            print "$i/$j : $$sim{$i}{$j}\n" if $$sim{$i}{$j} >= $epsilon;
        }
    }
}


# JG: Added this method
sub returnAllSimilarities {
    my $self = shift;
    my $sim = $self->sim;
    my $epsilon = .05;
    my %return;
    for my $i (keys %$sim) {
        for my $j (keys %{$$sim{$i}}) {
            $return{"$i/$j"} = $$sim{$i}{$j} if $$sim{$i}{$j} >= $epsilon;
    	    }
    	}
	return %return;
	}


# JG: Added this method
sub getLargeSimilarities {
    my $self = shift;
    my $template1 = shift;
    my $template2 = shift;
    my $sim = $self->sim;
    my $epsilon = .05;
    
    open (SIMS, '>>FloodingSimilarities.txt') or die "$!"; 
    for my $i (keys %$sim) {
        for my $j (keys %{$$sim{$i}}) {
            print SIMS "$template1/$template2\t$i/$j\t$$sim{$i}{$j}\n" if $$sim{$i}{$j} >= $epsilon;
        }
    }
}


# This is used by the algoritm module 
# to set the similarity hash
sub _setSimilarity {
    my ($self, $ref) = @_; 
    $self->sim($ref);
}

# JG: This is used by the algoritm module 
# to set the PCG hash for getting back
sub _setPCG {
    my ($self, $ref) = @_; 
    $self->pcg($ref);
}


sub getSimilarity {
    my ($self, $a, $b) = @_;
    my $sim = $self->sim;
    for my $i (keys %$sim) {
        if ($i eq $a ) {
            for my $j (keys %{$$sim{$i}}) {
                if ($j eq $b) {
                    return $$sim{$i}{$j};
                }
            }
        }
        elsif ($i eq $b) {
            for my $j (keys %{$$sim{$i}}) {
                if ($j eq $a) {
                    return $$sim{$i}{$j};
                }
            }
        }
    }
    return;
}

1;
