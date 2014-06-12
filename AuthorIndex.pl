#! /opt/local/bin/perl -w

use strict;

my $bib = "/Users/jcgood/Dropbox/TemplatesBook/Cambrined.bbl";

open (BIB, "<", $bib) or die "$!";

my %idtoauthors;

while (my $line = <BIB>) {

	chomp($line);
	if( $line =~ m/bibitem/) {
	
		my $bibline = $line;
		if ( $line =~ m/\}$/ ) { }

		else {
			my $nextline = <BIB>;
			chomp($nextline);
			$nextline =~ s/^\s+//;
			until ( $nextline =~ m/\}$/ ) {
				$bibline = $bibline." ".$nextline;
				$nextline = <BIB>;
				chomp($nextline);
				$nextline =~ s/^\s+//;
				}
			
			$bibline = $bibline." ".$nextline;
			}
			
		$bibline =~ m/\]\{(.*?)\}$/;
		my $bibid = $1;
			
		# We know what's next is the author names
		my $authorline = <BIB>;
		chomp($authorline);
		if($authorline =~ m/(.*)\.\s+\d\d\d\d/) {
		
			my $author = $1;
			if($author =~ m/(\s|~)\w$/) {
				$author .= ".";
				}
		
			$idtoauthors{$bibid} = $author

			}

		else {
			my $nextauthline = <BIB>;
			chomp($nextauthline);
			$nextauthline =~ s/^\s+//;
			until ( $nextauthline =~ m/(.*)\.\s+\d\d\d\d\.$/ ) {
				$authorline = $authorline." ".$nextauthline;
				$nextauthline = <BIB>;
				chomp($nextauthline);
				$nextauthline =~ s/^\s+//;
				}
			
			$nextauthline =~ m/(.*)\.\s+\d\d\d\d\.$/;
			$authorline = $authorline." ".$1;
			$idtoauthors{$bibid} = $authorline;
			}

		
		}	
			
				
	}

# Seem to have the ids and the authors
# Now I need to parse the authors to get last name first in all cases to make the index...dragons
	
my @ids = keys(%idtoauthors);
for my $id (@ids) {
	print "$id ".$idtoauthors{$id}."\n";
	}