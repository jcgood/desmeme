#! /opt/local/bin/perl -w

use strict;

use Storable;
	my %idtoauthorlist = %{retrieve("./bibindex")};

my $chapter = "/Users/jcgood/Dropbox/TemplatesBook/IndexTest.tex";
open (CHAP, "<", $chapter) or die "$!";

#my $indexedchapter = "/Users/jcgood/Dropbox/TemplatesBook/IndexTestIndexed.tex";
#open (INDXCHAP, ">", $indexedchapter) or die "$!";

while (my $line = <CHAP>) {

	my @bibidlist = $line =~ m/(\\\w*?cite(?:\[.*?\])?\{.*?\})/g;
	
	for my $bibidcites (@bibidlist) {
	
		my $bibids = $bibidcites;
		$bibids =~ s/^.*{//;
		$bibids =~ s/}$//;
		
		for my $bibid (split(/,/, $bibids)) {
			
			my $indexline = join("", @{$idtoauthorlist{$bibid}});
			$line =~ s/\Q$bibidcites/$bibidcites$indexline/;
				
			}
	
		}
		
	print $line;

	}