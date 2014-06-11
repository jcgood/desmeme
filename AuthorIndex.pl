#! /opt/local/bin/perl -w

use strict;

my $bib = "/Users/jcgood/Dropbox/TemplatesBook/Cambrined.bbl";

open (BIB, "<", $bib) or die "$!";

my %idtoauthors;

my $bibline;
my $authors;
while (my $line = <BIB>) {

	chomp($line);

	if( $line =~ m/bibitem/) {
	
		my $bibline = $line;
		if ( $line !~ m/\}$/ ) { $idtoauthors{$bibline} = 1; }

		else {
			while ( $line !~ m/\}$/ ) {
				my $nextline = <BIB>;
				chomp($nextline);
				$nextline =~ s/^\s+//;			
				$bibline = $bibline." ".$nextline;
				$line = <BIB>;
				}
			
			$bibline = $bibline." ".$line;
			}
	
		$idtoauthors{$bibline} = 1;
		}
	
	# We got 
			
				
	}
	
	
my @ids = keys(%idtoauthors);
for my $id (@ids) {
	print "$id\n";
	}