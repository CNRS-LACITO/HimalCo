use strict;
use warnings;

use utf8;


sub generation {
	open (FILE, ">>:utf8", "b.txt");
	my ($variable1) = $_[0];
	my ($variable2) = $_[1];
	my $radical = $variable1; 
		#$radical =~ s/,[\w|\(|\)|\;|\_|\.]+?,/,/;
	$radical =~ s/\_.//;	#supprimer _ + n'importe quel autre caractère (marque de tr en fin de racine)
	$radical =~ s/ //;	
	
	close(FILE);
}
	

open FICHIER, "<:utf8", "khaling-english.txt";



while (<FICHIER>) {
#my $donnees = <FICHIER>;
 
my ($donnees)= $_;
chomp($donnees);
my @mots = split('-',$donnees);

 #foreach my $entree (@mots) {
    generation ($mots[0], $mots[1]);
  
	#print $entree;

}
close(FICHIER);


