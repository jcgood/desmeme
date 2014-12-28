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
		
			# hack for special case
			elsif($authorline =~ m/R Core Team/) { $author = "R~Core~Team"; }

			$idtoauthors{$bibid} = $author;

			}


		else {
			my $nextauthline = <BIB>;
			chomp($nextauthline);
			$nextauthline =~ s/^\s+//;
			until ( $nextauthline =~ m/.*\.\s+\d\d\d\d/ or $nextauthline =~ m/^\d\d\d\d.*?\./) {
				$authorline = $authorline." ".$nextauthline;
				$nextauthline = <BIB>;
				chomp($nextauthline);
				$nextauthline =~ s/^\s+//;
				#special condition of year on one line
				if ($nextauthline =~ m/^\d\d\d\d.*?\./) {
					$authorline =~ s/\.$//;
					$idtoauthors{$bibid} = $authorline;
					}
				}
			
			$nextauthline =~ m/(.*)\.\s+\d\d\d\d/;
			$authorline = $authorline." ".$1 if defined($1);
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
	my $firstauthor;
	
	# Weird hack for weird author and because the $1 variable remains defined with
	# previous first author despite loop (seems like a bug in this case)
	if($authorstring eq "R~Core~Team") { $firstauthor = "R~Core~Team"; }
	
	else{
		$authorstring =~ m/^(.*?,\s.*?)(,|\\\&|$)/;	
		$firstauthor = $1;
		}
	$firstauthor =~ s/\(ed(s?)\.\)//;
	$firstauthor =~ s/\s+$//;
	$firstauthor =~ s/^\s+//;
	
	#Random fixes for problem entries
	$firstauthor =~ s/\{\\SortNoop\{Hacken\}\}//;
		
	#print "zzzz: $firstauthor\n";
	push(@authorlist,"\\aindex{$firstauthor}");
	
	# remove first author to get other authors which are formatted differently
	$authorstring =~ s/^(.*?,\s.*?)(,|\\\&|$)\s?//;
	
	#print "xxx: $authorstring yyy\n";
	
	# Get other authors	
	while ($authorstring =~ /(.*?)(?:,|\\\&|$)/g) {
	 	
	 	my $nextauthor = $1;
		$nextauthor =~ s/\(ed(s?)\.\)//;
		$nextauthor =~ s/\s+$//;
		$nextauthor =~ s/^\s+//;
	 	
	 	# Special conditions for second authors with only one initial
	 	$nextauthor =~ s/^([A-Z]\.)~/$1 /;
	 	
	 	$nextauthor =~ m/^(.*)\s(.*)$/;
	 	if ($nextauthor) {  
	 		my $first = $1;
	 		my $last = $2;
	 		
	 		if(!$last) { print "xxx: $first\n$nextauthor $id\n"; }
	 		if(!$first) { print "yyy: $last\n$nextauthor $id\n"; }
	 		
	 		
	 		# Hack for weird author of R Core Team
	 		if($first =~ m/Team/) { $last = ""; }

	 		my $reversename = "\\aindex{$last, $first}";

	 		# Continued for weird author of R Core Team
	 		if($first =~ m/Team/) { $reversename = "\\aindex{R~Core~Team}"; $first = ""; }

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