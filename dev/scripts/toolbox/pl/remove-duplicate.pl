#!/usr/bin/perl

## Script de suppression d'entrées lexicales en doublon dans un dictionnaire au format toolbox
## CP - 30/05/2014

use strict;
use warnings;

my $usage = "perl $0 dictionary.txt > new_dictionary.txt\n";
die $usage unless @ARGV == 1;
die $usage unless -f $ARGV[0];

my @entries; #struct. de données pour les entrées lexicales (tab. de réf. de tab. anonymes)
my @tmp;

open(FILE, "<$ARGV[0]") || die $!;
while(<>){
  chomp;
  if($_ =~ /[a-z]+/){ #Si ligne contient une info lexicale -> ajout dans @tmp
    push(@tmp, $_);
  }
  else{ #Sinon (fin de l'entrée lex.) check doublon et reset @tmp
    push(@entries, [ @tmp ]) unless(contains_duplicate(\@tmp, \@entries));
    @tmp = ();
  }
}
close FILE;

## Ecriture résultat
foreach my $entry (@entries){
  print join("\n", @{$entry}), "\n\n";
}


## Vérifie si l'entrée lexicale en input existe déjà dans la structure de données
## input : ref tab entrée à tester, struct. de données contenant les entrées du dico
## output : 1 si contient doublon, 0 sinon
sub contains_duplicate{
  my $ref_new_entry = shift;
  my $ref_entries = shift;

  foreach my $ref_entry(@{ $ref_entries }){
    if(is_duplicate($ref_new_entry, $ref_entry)){
      return 1;
    }
  }
  return 0; # Toutes les entrées ont été testées -> pas doublon
}

## Teste si les deux param sont des entrées lexicales doublons
## input : ref tab de l'entrée à tester, ref tab d'une entrée déjà dans la struct. de données
## output : 1 si doublon, 0 sinon
sub is_duplicate{
  my $ref_new_entry = shift;
  my $ref_entry = shift;
  
  return 0 if(scalar(@{$ref_new_entry}) != scalar(@{$ref_new_entry})); # pas la même dimension -> pas doublon
  for(my $i=0; $i < scalar(@{$ref_new_entry}); $i++){
    return 0 if($ref_new_entry->[$i] ne $ref_entry->[$i]);
  }
  return 1; # tous les éléments des deux tabs sont égaux -> doublon
}

