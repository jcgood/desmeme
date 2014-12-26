#! /opt/local/bin/perl -w

use strict;
use Storable;
use List::MoreUtils qw(uniq);
use ParseIndex;

system("/opt/local/bin/perl -w /Users/jcgood/gitrepos/desmeme/MakeBibIndex.pl");


my %idtoauthorlist = %{retrieve("./bibindex")};

my @chapters = ("1-Defining","2-DescriptionLanguage","3-CaseStudies","4-Comparison","5-MovingForward", "Appendices", "TemplateOntology", "TemplateProps");

# Get language list


open (LANGS, "<", "/Users/jcgood/Dropbox/TemplatesBook/languagelist.txt") or die "$!";
my @langs;
while (my $lang = <LANGS>) {
	
	chomp($lang);
	push(@langs, $lang);

	}


@langs = uniq(@langs);

# Our system will adopt the subset principle
# To do: Help systematize entries, maybe separate file and/or parsing structure?

my ($subjects,$crossrefs) = ParseIndex::parseindex();

my %subjects = %$subjects;
my %crossrefs = %$crossrefs;



#Read in by paragraph not line for terms that cross line breaks
$/ = "\n\n";

my %seenLangs;
my %seenterms;
foreach my $chapter (@chapters) {

	my $chapterpath = "/Users/jcgood/Dropbox/TemplatesBook/$chapter.tex";
	open (CHAP, "<", $chapterpath) or die "$!";

	my $indexedchapter = "/Users/jcgood/Dropbox/TemplatesBook/$chapter"."Indexed.tex";
	open (INDXCHAP, ">", $indexedchapter) or die "$!";

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

		# Messy conditions to avoid index markers in bad places
		unless ($line =~ m/\\.*?section/ or $line =~ m/\\chapter/) {
			my $matched = 0;
			foreach my $lang (@langs) {
				# A line break may "count" as a space, need to make a copy, otherwise we destroy the original with looping
				my $langcopy = $lang;
				$langcopy =~ s/ /\( \|\\n\)/g;
				my $matches = $line =~ s/(?<!(\\.ref\{))(?<!(\\ref\{))(?<!(\\label\{))\b$langcopy\b/$lang\\lindex\{$lang\}/g;
				# Do this to check for typoes--if a lang never matches, why is it there?
				if ($matches) { $seenLangs{$lang} = 1; }
				}
			}


		# Lots of special logic needed for embedded terms
		unless ($line =~ m/\\.*?section/ or $line =~ m/\\chapter/) {
			TERM: foreach my $subj (sort(keys(%subjects))) {
				# We are at a top-level index term, for now, we'll just go one deep, otherwise dragons
				my @termset = @{$subjects{$subj}}; # order matters
				
				foreach my $termpair (@termset) {
					my ($textterm, $indexterm) = @$termpair;
					#print "xxx: $textterm, $indexterm\n";
					# A line break may "count" as a space, need to make a copy, otherwise we destroy the original with looping
					my $texttermcopy = $textterm;
					$texttermcopy =~ s/ /\( \|\\n\)/g;
					my $matches = $line =~ s/(?<!(?:\\.ref\{))(?<!(?:\\ref\{))(?<!(?:\\label\{))(?<!(?:\s\())(?<!(?:\\tindex\{))(?<!(?:\\cite\{))(?<!(?::))(?<!(?:chainin\())(?<!(?:COPY ))(?<!(?:\\s{))\b($texttermcopy)\b(?!\\tindex)/$1\\tindex\{$indexterm\}/gi;
					# Do this to check for typoes--if a term never matches, why is it there? # To do fix me for nested data structure
					if ($matches) { $seenterms{$textterm} = 1; next TERM;}
					# If we have matched a term in a termset, we skip the rest of the set, we may lose some terms, but are assuming paragraph-level topics for laziness
					}
				}
			}

		print INDXCHAP $line;
		}

	}


# Do some error tests for elements indicated as being indexed but not found
foreach my $lang (@langs) {
	unless(exists($seenLangs{$lang})) { print "Language $lang did not match any line.\n"; }
	}
	
# to do: update for new data structure
foreach my $subj (keys(%subjects)) {
	# We are at a top-level index term, for now, we'll just go one deep, otherwise dragons
	my @termset = @{$subjects{$subj}}; # order matters
				
	foreach my $termpair (@termset) {
		my ($textterm, $indexterm) = @$termpair; 
		unless(exists($seenterms{$textterm})) { print "Term $textterm did not match any line.\n"; }
	
		}
	}
	
	
# Add the "see also" for the terms at the end of the last chapter

open (C5, ">>", "/Users/jcgood/Dropbox/TemplatesBook/5-MovingForwardIndexed.tex") or die "$!";
print C5 "\n\n";
for my $crossref (keys(%crossrefs)) {
	print C5 $crossrefs{$crossref}."\n";
	}