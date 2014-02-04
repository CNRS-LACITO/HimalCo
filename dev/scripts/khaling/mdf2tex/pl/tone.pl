use strict;
use warnings;

use utf8;


open FICHIER, "<:utf8", "c.txt";
open FICHIER2, ">>:utf8", "b.txt";

while (my $donnees = <FICHIER>) {

  $donnees =~ s/ː([ptk][ptkbdgmnŋrlsʦʣ])/̂ː$1/g;
   $donnees =~ s/ː([ptk]\W)/̂ː$1/g;
  $donnees =~ s/([aeiouɛʌɵʉ])ː/$1̄ː/g;
  #$donnees =~ s/ː/̂ː/;
  print FICHIER2 $donnees;
	#print $entree;

}