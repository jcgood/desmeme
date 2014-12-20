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
			
		# We know what's next is usually author names, they seem to max out at three lines(?)
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
			until ( $nextauthline =~ m/.*\.\s+\d\d\d\d/ ) {
				$authorline = $authorline." ".$nextauthline;
				$nextauthline = <BIB>;
				chomp($nextauthline);
				$nextauthline =~ s/^\s+//;
				#special condition of year on one line
				if ($nextauthline =~ m/^\d\d\d\d\./) {
					$authorline =~ s/\.$//;
					$idtoauthors{$bibid} = $authorline;
					}
				}
			
			$nextauthline =~ m/(.*)\.\s+\d\d\d\d/;
			$authorline = $authorline." ".$1;
			$idtoauthors{$bibid} = $authorline unless exists($idtoauthors{$bibid});
			}
		
		}	
			
	}


# Seem to have the ids and the authors
# Now I need to parse the authors to get last name first in all cases to make the index...dragons
	
my @ids = keys(%idtoauthors);
my %idtoauthorlist;
for my $id (@ids) {

	my @authorlist;

	my $authorstring = $idtoauthors{$id};
	
	# Get first author
	$authorstring =~ m/^(.*?,\s.*?)(,|\\\&|$)/;	
	my $firstauthor = $1;
	$firstauthor =~ s/\(ed(s?)\.\)//;
	$firstauthor =~ s/\s+$//;
	$firstauthor =~ s/^\s+//;
	push(@authorlist,"\\aindex{$firstauthor}");
	
	# remove first author to get other authors which are formatted differently
	$authorstring =~ s/^(.*?,\s.*?)(,|\\\&|$)\s?//;
	
	# Get other authors	
	while ($authorstring =~ /(.*?)(?:,|\\\&|$)/g) {
	 	
	 	my $nextauthor = $1;
		$nextauthor =~ s/\(ed(s?)\.\)//;
		$nextauthor =~ s/\s+$//;
		$nextauthor =~ s/^\s+//;
	 	
	 	# Special conditions for second authors with only one inition
	 	$nextauthor =~ s/^([A-Z]\.)~/$1 /;
	 	
	 	$nextauthor =~ m/^(.*)\s(.*)$/;
	 	if ($nextauthor) {  
	 		my $first = $1;
	 		my $last = $2;
	 		
	 		if(!$last) { print "xxx: $first\n$nextauthor\n"; }
	 		if(!$first) { print "yyy: $last\n$nextauthor\n"; }
	 		
	 		
	 		my $reversename = "\\aindex{$last, $first}";
	 		push(@authorlist,$reversename);
	 		}
	 		
		}
	
	
	$idtoauthorlist{$id} = \@authorlist;
	
	}


# my @bibitems = keys(%idtoauthorlist);
# for my $bibitem (@bibitems) {
# 
# 	my @authorlist = @{$idtoauthorlist{$bibitem}};
# 	print "$bibitem ".join("", @authorlist)."\n";
# 
# 	}

use Storable;
	store \%idtoauthorlist, "./bibindex";
#  $hashref = retrieve('file');