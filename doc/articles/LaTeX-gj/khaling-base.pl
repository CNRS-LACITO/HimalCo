use strict;
use warnings;
use utf8;

sub voicing {
	my ($radical) = shift;
	$radical =~ s/([aeiuo])p$/$1b/;
	$radical =~ s/([aeiuo])t$/$1d/;
	$radical =~ s/([aeiuo])k$/$1g/;
	return $radical;
}

   sub generation {
      open (OUTPUTFILE, ">>:utf8", "output.txt");
      my ($root) = shift;
      my ($class) = shift;
      my ($meaning) = shift;
      print OUTPUTFILE voicing($root)."\n";
      close(OUTPUTFILE);
   }
	
   open INPUTFILE, "<:utf8", "input.txt";

   while (<INPUTFILE>) {
      my ($donnees)= $_;
      chomp($donnees);
      my @mots = split('_',$donnees);
      generation ($mots[0], $mots[1],$mots[2]);
   }
   close(INPUTFILE);


