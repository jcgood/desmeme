package ParseIndex;

sub parseindex {

use strict;
use Data::Dumper;

my $indexfile = "/Users/jcgood/Dropbox/TemplatesBook/indexterms.txt";
open (IDX, "<", $indexfile) or die "$!";

my %mainTerms;
my %crossrefTerms;
my $topTerm;
while (my $termSet = <IDX>) {

	chomp($termSet);

	if (!$termSet or $termSet eq "\t") { next; } # skip blank lines

	my $term;
	my $remainderList = 0;
	if ($termSet =~ m/(.*)(?::\s)(.*)/) {
		
		$term = $1;
		$remainderList = $2;	

		}
		
	else { $term = $termSet; }
	
	if($term !~ m/^\t/) {

		if($remainderList =~ m/see (.*)$/) {
			my $crossRef = $1;
			my $crossrefEntry = "\\tindex{$term|see {$crossRef}}";
			$crossrefTerms{$term} = $crossrefEntry;
			next;
			}

			
		if($term =~ m/(.*)\((e?s)\)$/) {
			my $singular = $1;
			$topTerm = $singular;
			}
		else { $topTerm = $term; }
			
					
		if (!$remainderList) {
		
			if($term =~ m/(.*)\((e?s)\)$/) {
				my $sortingTerm = "b".$1;
				my $singular = $1;
				my $plural = $1.$2;
				my @termList = ( [ $plural, $singular], [ $singular, $singular] );
				$mainTerms{$sortingTerm} = [ @termList ];
				}
				
			else {
				my $sortingTerm = "b".$term;
				my @termList = ( [ $term, $term] );
				$mainTerms{$sortingTerm} = [ @termList ];
				}
		
			}


		# We have a remainderList
		else {
					
			my @remainders = split(/, /, $remainderList);
			my @termList;
			my $sortingTerm;
			
			# Do the main term
			if($term =~ m/(.*)\((e?s)\)$/) {
				$sortingTerm = "b".$1;
				my $singular = $1;
				my $plural = $1.$2;
				push(@termList, ( [ $plural, $singular], [ $singular, $singular] ));
				}
			else {		
				$sortingTerm = "b".$term;
				push(@termList, ( [ $term, $term] ));
				}

			# Do the sub-terms
			foreach my $remainder (@remainders) {
	
	
				if($remainder =~ m/(.*)\((e?s)\)$/) {
					my $singular = $1;
					my $plural = $1.$2;
					push(@termList, ( [ $plural, $topTerm], [ $singular, $topTerm] ));
	
					}
					
				else {		
					push(@termList, ( [ $remainder, $topTerm] ));
					}
			
				}

			$mainTerms{$sortingTerm} = [ @termList ];
		
			}
			
		}

	
	# subheadings
	else{
		
		# strip leading tab
		$term =~ s/^\t//;

		if (!$remainderList) {
		
			if($term =~ m/(.*)\((e?s)\)$/) {
				my $sortingTerm = "a".$1;
				my $singular = $1;
				my $plural = $1.$2;

				$singular =~ m/(\w+) (\w+)/;				
				my $abbrevEntry = $singular;
				if($1) { $abbrevEntry = $1; }
				my @termList = ( [ $plural, $topTerm."!".$abbrevEntry], [ $singular, $topTerm."!".$abbrevEntry] );
				
				$mainTerms{$sortingTerm} = [ @termList ];
				
				}
				
			else {
			
				my $sortingTerm = "a".$term;
				$term =~ m/^(\w+) (\w+)$/;				
				my $abbrevEntry = $term;
				if($1) { $abbrevEntry = $1; }	
				if ($term eq "pairwise connectivity graph") { $abbrevEntry = "pairwise connectivity" } # = total hack			
				my @termList = ( [ $term, $topTerm."!".$abbrevEntry] );
				$mainTerms{$sortingTerm} = [ @termList ];				
			
				}
		
			}


		# We have a remainderList
		else {
					
			my @remainders = split(/, /, $remainderList);
			my @termList;
			my $sortingTerm;
			
			# Do the main term
			my $abbrevEntry;
			if($term =~ m/(.*)\((e?s)\)$/) {
				$sortingTerm = "a".$1;
				my $singular = $1;
				my $plural = $1.$2;
				
				$singular =~ m/(\w+) (\w+)/;				
				$abbrevEntry = $singular;
				if($1) { $abbrevEntry = $1; }
				push(@termList, ( [ $plural, $topTerm."!".$abbrevEntry], [ $singular, $topTerm."!".$abbrevEntry] ));
				}
			else {		
				$sortingTerm = "a".$term;
				$term =~ m/(\w+) (\w+)/;				
				$abbrevEntry = $term;
				if($1) { $abbrevEntry = $1; }				
				push(@termList, ( [ $term, $topTerm."!".$abbrevEntry] ));
				}

			# Do the sub-terms
			foreach my $remainder (@remainders) {
	
				if($remainder =~ m/(.*)\((e?s)\)$/) {
					my $singular = $1;
					my $plural = $1.$2;
					push(@termList, ( [ $plural, $topTerm."!".$abbrevEntry], [ $singular, $topTerm."!".$abbrevEntry] ));
	
					}
					
				else {		
					push(@termList, ( [ $remainder, $topTerm."!".$abbrevEntry] ));
					}
			
				}

			$mainTerms{$sortingTerm} = [ @termList ];
		
			}
			
		}
		
	}
	
	
# serialize the two indices--even better, make this a function and returnem
print Dumper(\%mainTerms);
print Dumper(\%crossrefTerms);

return(\%mainTerms, \%crossrefTerms);

}

1;