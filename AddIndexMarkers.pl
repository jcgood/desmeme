#! /opt/local/bin/perl -w

use strict;
use Storable;
use List::MoreUtils qw(uniq);

system("/opt/local/bin/perl -w /Users/jcgood/gitrepos/desmeme/MakeBibIndex.pl");

#Read in by paragraph not line for terms that cross line breaks
$/ = "\n\n";

my %idtoauthorlist = %{retrieve("./bibindex")};

my @chapters = ("1-Defining","2-DescriptionLanguage","3-CaseStudies","4-Comparison","5-MovingForward");

my @langs = (

	"Ahtna",
	"Athabaskan",
	"Bantu",
	"Chechen",
	"Chichewa",
	"English",
	"German",
	"Ingush",
	"Japanese",
	"Nimboran",
	"Penutian",
	"Semitic",
	"Sierra Miwok",
	"sign languages",
	"Tiene",
	"Turkish",

	);

@langs = uniq(@langs);

# Our system will adopt the subset principle
# To do: Help systematize entries, maybe separate file and/or parsing structure?
my %subjects = (

	amorphophonologicaltemplate => [
	
		[ "morphophonological templates" => "template!morphophonological" ],
		[ "morphophonological template" => "template!morphophonological" ],
	
		],

	amorphosyntactictemplate => [
	
		[ "morphosyntactic templates" => "template!morphosyntactic" ],
		[ "morphosyntactic template" => "template!morphosyntactic" ],
	
		],

	aphonologicaltemplate => [
	
		[ "phonological templates" => "template!phonological" ],
		[ "phonological template" => "template!phonological" ],
		
		],

	asyntactictemplate => [
	
		[ "syntactic templates" => "template!syntactic" ],
		[ "syntactic template" => "template!syntactic" ],
		
		],

	btemplate => [

		[ templates => "template" ],
		[ template => "template" ],
		
		],
		

	atemplatic => [
		[ templatic => "templatic"]
		],

	aphonology => [
		[ phonology => "phonology"]
		],

	amorphology => [
		[ morphology => "morphology"]
		],

	asyntax => [
		[ syntax => "syntax"]
		],

	awordorder => [
		[ "word order" => "word order"]
		],

	atypology => [
		[ "typology" => "typology"]
		],

	atypological => [
		[ "typological" => "typological"]
		],

	agenerative => [
		[ "generative" => "generative"]
		],

	aformallinguistics => [
		[ "formal linguistics" => "formal linguistics"]
		],

	afunctional => [
		[ "functional" => "functional"]
		],


	);


# clausal template
# morphological template


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
					my $matches = $line =~ s/(?<!(?:\\.ref\{))(?<!(?:\\ref\{))(?<!(?:\\label\{))(?<!(?:\s\())(?<!(?:\\tindex\{))\b($texttermcopy)\b(?!\\tindex)/$1\\tindex\{$indexterm\}/gi;
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