use strict;
use warnings;

use utf8;


	my $partie1 = "";
	my $partie2 = "";
	my $theme_A = "";
	my $theme_B = "";
	my $theme_B2 = "";
	my $theme_C = "";
	my $theme_C2 = "";
	my $theme_D = "";
	my $theme_E = "";
	my $theme_F = "";
	my $theme_G = "";
	my $theme_G2 = "";
	my $theme_H = "";
	my $theme_I = "";
	my $theme_J = "";
	my $theme_K = "";
	my $theme_L = "";
	my $theme_M = "";
	my $theme_N = "";
	my $theme_O = "";
	my $theme_P = "";
	
	my $theme_2A = "";
	my $theme_2B = "";
	my $theme_2B2 = "";
	my $theme_2C = "";
	my $theme_2D = "";
	my $theme_2E = "";
	my $theme_2F = "";
	my $theme_2G = "";
	my $theme_2G2 = "";
	#1.01
	
sub regle101 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-1);
	 $partie2 = substr($radical,-1,1);
    $partie2 =~ tr/[p,t,k]/[b,d,g]/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.02
sub regle102 {
	my ($radical) = shift;
	$partie1 = substr($radical,0,-3);
	$partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1ʦ/;
	$partie2 =~ s/([aʌieɛuoɔɵʉ])n/$1ːʦ/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.03
sub regle103 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1s/;
	$partie2 =~ s/([aʌieɛuoɔɵʉ])n/$1ːs/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.04
sub regle104 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1ç/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.05
sub regle105 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])p/$1̂m/;
$partie2 =~ s/([aʌeiɛuoɔɵʉ])k/$1̂ŋ/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.06
sub regle106 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂n/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.07
sub regle107 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂j/; #garde un i car il faut qu'il apparaisse comme इ
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.08
sub regle108 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂ː/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.09
sub regle109 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/([aʌieɛuoɔɵʉ])n/$1j/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.10
sub regle110 {
	my ($radical) = shift;
	$partie1 = substr($radical,0,-3);
	$partie2 = substr($radical,-3,3);
    $partie2 =~ s/ik/ûː/;
	$partie2 =~ s/([aiʌeɛuoɔɵʉ])k/$1̂ː/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.11
sub regle111 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
    $partie2 =~ s/iŋ/ūː/;
	$partie2 =~ s/([aiʌeɛuoɔɵʉ])ŋ/$1̄ː/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.12
sub regle112 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-2);
	 $partie2 = substr($radical,-2,2);
    $partie2 =~ s/([ptkmnŋrl])t/$1/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.12
sub regle113 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-1);
	 $partie2 = substr($radical,-1,1);
    $partie2 =~ s/ak/a/;
	$radical =  $partie1.$partie2;
	return $radical;
}


#1.15
sub regle115 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-3);
	 $partie2 = substr($radical,-3,3);
	 $partie2 =~ s/iŋt/unt/;
    $partie2 =~ s/ŋt/nt/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#1.16
sub regle116 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-2);
	 $partie2 = substr($radical,-2,2);
    $partie2 =~ s/iŋ/un/;
    $partie2 =~ s/ŋ/n/;
    $partie2 =~ s/ik/ûn/;
    $partie2 =~ s/k/̂n/;
	$radical =  $partie1.$partie2;
	return $radical;
}
 
 sub regle117 {
	my ($radical) = shift;
	 $partie1 = substr($radical,0,-2);
	 $partie2 = substr($radical,-2,2);
    $partie2 =~ s/([mnŋrl])t/$1d/;
	$radical =  $partie1.$partie2;
	return $radical;
}

#2.01
sub regle201 {
	my ($radical) = shift;
    $radical =~ s/o/ɵ/;
	$radical =~ s/u/ʉ/;
	return $radical;
}

sub regle202 {
	my ($radical) = shift;
	unless (($radical  =~ "[aeiouɛɵʉɔʌː]k")|($radical =~ "[aeiouɛɵʉɔʌː]ŋ"))	{
		$radical =~ s/a/ɛ/;
	}
	return $radical;
}

#2.02
sub regle203 {
	my ($radical) = shift;
	unless (($radical =~ "[aeiouɛɵʉɔʌ]k")|($radical =~ "[aeiouɛɵʉɔʌ]ŋ"))	{
		$radical =~ s/i/ʌ/;
		$radical =~ s/u/ʌ/;
		$radical =~ s/o/oɔ/;
	}
	return $radical;
}

sub regle204{
	my ($radical) = shift;
	$radical =~ s/ik/ʌk/;
	$radical =~ s/iŋ/ʌŋ/;
	$radical =~ s/ig/ʌg/;
	$radical =~ s/ɵk/ok/;
	$radical =~ s/ɵŋ/oŋ/;
	$radical =~ s/ɵg/og/;
	$radical =~ s/ʉk/uk/;
	$radical =~ s/ʉŋ/uŋ/;
	$radical =~ s/ʉg/ug/;

	return $radical;
}

sub regle205 {
	my ($radical) = shift;
    $radical =~ s/a/ʌ/;
	return $radical;
}

sub regle301 {
	my ($radical) = shift;
    $radical =~ s/ʌ/aː/;
	$radical =~ s/a/aː/;
	$radical =~ s/o/oː/;
	$radical =~ s/ɵ/ɵː/;
	$radical =~ s/u/uː/;
	$radical =~ s/ʉ/ʉː/;
	$radical =~ s/i/iː/;
	$radical =~ s/e/eː/;
	$radical =~ s/ɛ/ɛː/;
	return $radical;
}

sub regle302 {
	my ($radical) = shift;
    $radical =~ s/([aʌieɛuoɔɵʉ])([mnŋrli])/$1̂$2/;
	return $radical;
}

sub regle303 {
	my ($radical) = shift;
    $radical =~ s/ep/eːp/;
	$radical =~ s/ɛp/ɛːp/;
	return $radical;
}

sub regle304 {
	my ($radical) = shift;
    $radical =~ s/ː([mnŋrl])/$1/; #supprimer longueurs en syllabe fermée de sonantes
	$radical =~ s/ː̂([mnŋrl])/̂$1/;
	$radical =~ s/ːː/ː/;
	$radical =~ s/ː̂ː/̂ː/;
	return $radical;
}
sub regle401 {
	my ($radical) = shift;
	$radical =~ s/([a,e,o,u])/$1ː/;
	$radical =~ s/i/uː/;
	$radical =~ s/ɛ/aː/;
	return $radical;
}



sub generation {
	open (FILE, ">>:utf8", "reflexive_paradigms_eng.txt");
	my ($variable1) = $_[0];
	my ($variable2) = $_[1];
	my ($variable3) = $_[2];
		my $radical = $variable1; 
		#$radical =~ s/,[\w|\(|\)|\;|\_|\.]+?,/,/;
	$radical =~ s/\_.//;	#supprimer _ + n'importe quel autre caractère (marque de tr en fin de racine)
	$radical =~ s/ //;	
	my $rime = $radical;
	$rime  =~ s/.*([aeiouɛ])/$1/;
	
	my $forme =$radical;
	 $forme = regle112($forme);	 
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	$forme = regle107($forme);
	$forme = regle109($forme);
	$forme = regle110($forme);
	$forme = regle111($forme);
	$forme = regle105($forme);
	 $theme_A = $forme;

	 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle102($forme);
	 $forme = regle201($forme);
	 $forme = regle205($forme);
	$theme_B = $forme;		

		 $forme =$radical;
		if ($radical =~  /t$/) { #ne subit pas la règle 205
			#$forme = regle202($forme);
			$forme = regle102($forme);
			$forme = regle201($forme);
			$theme_B2 = $forme.'ʦ';}
		 elsif ($radical =~  /n$/) {
			#$forme = regle202($forme);
			$forme = regle102($forme);
			$forme = regle201($forme);
			$theme_B2 = $forme;}
		else {
			#$forme = regle202($forme);
			$forme = regle201($forme);
			$forme = regle302($forme);
			$theme_B2 = $forme.'j'; }

	 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	 $forme = regle204($forme);
	 $forme = regle104($forme);
	 $forme = regle109($forme);
	$theme_C = $forme;		

	 $forme =$radical;
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	 $forme = regle204($forme);
	 $forme = regle109($forme);
	 $forme = regle103($forme);
	$theme_C2 = $forme;		

		 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	$forme = regle110($forme);
	 $forme = regle204($forme);
	$forme = regle107($forme);
	$forme = regle109($forme);
	$forme = regle303($forme);
	$theme_D = $forme;		
	
		 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	$forme = regle110($forme);
	$forme = regle111($forme);
	 $forme = regle204($forme);
	$forme = regle105($forme);
	$forme = regle106($forme);
	$forme = regle107($forme);
	$forme = regle109($forme);
	$forme = regle303($forme);
	$theme_E = $forme;		

		$forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle103($forme);
	 $forme = regle201($forme);
	 $forme = regle205($forme);
	$theme_F = $forme;		
	
				$forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle103($forme);
	 $forme = regle201($forme);
	$theme_G = $forme;		
	
	 $forme = regle302($forme);
	$theme_G2 = $forme;			
	
	
					$forme =$radical;
	 $forme = regle112($forme);
	#$forme = regle202($forme);
	 $forme = regle101($forme);
	 $forme = regle205($forme);
	$theme_H = $forme;		

	 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle101($forme);
	 $forme = regle201($forme);
	$forme = regle301 ($forme);
	$theme_I = $forme;		
	
	 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle201($forme);
	$forme = regle302 ($forme);
	$forme = regle301($forme);
	$forme = regle304($forme);
	$theme_J = $forme;		

	 $forme =$radical;
	 $forme = regle112($forme);
	#$forme = regle202($forme);
	$forme = regle108($forme);
	$forme = regle101($forme);
	$forme = regle205($forme);
	$theme_K = $forme;	

	 $forme =$radical;
	 $forme = regle112($forme);
	#$forme = regle202($forme);
	$forme = regle201($forme);
	$forme = regle108($forme);
	$forme = regle302 ($forme);
	$forme = regle301($forme);
	$forme = regle304($forme);	
	$theme_L = $forme;	
	
	 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	 $forme = regle204($forme);
	$forme = regle105($forme);
	$forme = regle106($forme);
	$forme = regle107($forme);
	$forme = regle109($forme);
	$forme = regle116($forme);
	$forme = regle302($forme);
	$forme = regle110($forme);
	$theme_M = $forme;	

	$forme =$radical;
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	 $forme = regle204($forme);
	$forme = regle115($forme);
	 $forme = regle117($forme);
	$theme_O = $forme;	

		 $forme =$radical;
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	 $forme = regle204($forme);
	$forme = regle115($forme);
	 $forme = regle112($forme);
	 $forme = regle117($forme);
	$forme = regle302($forme);
	$theme_N = $forme;	
	
	
	 $forme =$radical;
	 $forme = regle112($forme);
	 #$forme = regle202($forme);
	 $forme = regle203($forme);
	 $forme = regle204($forme);
	$forme = regle105($forme);
	$forme = regle106($forme);
	$forme = regle107($forme);
	$forme = regle109($forme);
	$forme = regle116($forme);
	$forme = regle110($forme);
	$theme_P = $forme;	
	
	 $forme =$radical;
	 $forme = regle202($forme);
	 $forme = regle201($forme);
	$theme_2A = $forme;	

	 $forme =$radical;
	 $forme = regle401($forme);
	$theme_2B = $forme;	
	
		$theme_2B2 = $theme_2B;
		$theme_2B2 =~ s/ː//;
		
		 $forme =$radical;
		 $forme =~ s/a/o/;
	 $forme = regle201($forme);
	$theme_2C = $forme;	
	
	$forme =$radical;
	 		 $forme =~ s/a/ʌ/;
	 $forme = regle201($forme);
	$theme_2D = $forme;	

	$forme =$radical;
	 $forme = regle201($forme);
	 $forme =~ s/a/u/;
	$theme_2E = $forme;	
	
	
			 $forme =$radical;
	  $forme =~ s/a/u/;
	 $forme = regle201($forme);
	$theme_2F = $forme;	
	
	 $forme =$radical;
	$forme =~ s/a/o/;
	 $forme = regle401($forme);
	$theme_2G = $forme;	
	
		$theme_2G2 = $theme_2G; #forme raccourcie
		$theme_2G2 =~ s/ː//;
	
	my $voyelle1 = "i";
	my $voyelle2 = "ʌ";
	my $voyelle3 = "u";
	if  ((substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]t")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]n")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]nt")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]ʦ")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]tt")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]s")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːs")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːʦ"))	{ 
			$voyelle1 = "";
			$voyelle2 = "";
			$voyelle3 = "";
	}
	#print FILE $theme_A."ŋʌ"."   ".$theme_B."i"." ". $theme_C."ki"." ".$theme_D." ".$theme_E."ni ".$theme_F.$voyelle1."ti  ".$theme_H."tɛ \n";

			print FILE "\n";
			print FILE "\n";
	
	if ($variable1 =~ /[ptkmnŋrl].r$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vr} \\centering \n";
		print FILE "\\caption{".$theme_P."sinɛ  \"".$variable2."\"  }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "\\textsc{1s} &".$theme_P."siŋʌ"." &".$theme_P."tʌsu \\\\ \n";
		print FILE "\\textsc{1di} &".$theme_G."siji"." &".$theme_G."sîjti   \\\\\n";
		print FILE "\\textsc{1de} &".$theme_G."siju"." &".$theme_G."sîjtu   \\\\ \n";
		print FILE "\\textsc{1pi} &".$theme_C2."siki"." &".$theme_C2."siktiki   \\\\ \n";
		print FILE "\\textsc{1pe} &".$theme_C2."sikʌ"." &".$theme_C2."siktʌkʌ   \\\\ \n";
		print FILE "\\textsc{2s} & ʔi".$theme_P."si & ʔi".$theme_P."tɛsi &".$theme_P."sije  \\\\ \n";
		print FILE "\\textsc{2d} & ʔi".$theme_G."siji"." & ʔi".$theme_G."sîjti &".$theme_G."sîjje    \\\\\n";
		print FILE "\\textsc{2p} & ʔi".$theme_P."sini  & ʔi".$theme_P."tɛnnu &".$theme_P."nuje  \\\\ \n";
		print FILE "\\textsc{3s} & ".$theme_P."si & ".$theme_P."tɛsi   \\\\ \n";
		print FILE "\\textsc{3d} & ".$theme_G."siji"." & ".$theme_G."sîjti   \\\\ \n";
		print FILE "\\textsc{3p} & ".$theme_P."sinu  & ".$theme_P."tɛnnu \\\\ \n";
		print  FILE "\\bottomrule\n";
		print  FILE "\\end{tabular}\n";
		print  FILE "\\end{table}\n";
	}

	elsif ($variable1 =~ /[aɛeiou]_r$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vr} \\centering \n";
		print FILE "\\caption{ ".$theme_2A."̂nsinɛ  ``".$variable2."\"  }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "\\textsc{1s} &".$theme_2A."̂nsiŋʌ"." &".$theme_2A."̂ntʌsu \\\\ \n";
		print FILE "\\textsc{1di} &".$theme_2A."ssiji"." &".$theme_2A."ssîjti   \\\\\n";
		print FILE "\\textsc{1de} &".$theme_2A."ssiju"." &".$theme_2A."ssîjtu   \\\\ \n";
		print FILE "\\textsc{1pi} &".$theme_2A."ssiki"." &".$theme_2A."ssiktiki   \\\\ \n";
		print FILE "\\textsc{1pe} &".$theme_2A."ssikʌ"." &".$theme_2A."siktʌkʌ   \\\\ \n";
		print FILE "\\textsc{2s} & ʔi".$theme_2A."̂nsi & ʔi".$theme_2A."̂ntɛsi &".$theme_2A."̂nsije  \\\\ \n";
		print FILE "\\textsc{2d} & ʔi".$theme_2A."ssiji"." & ʔi".$theme_2A."ssîjti &".$theme_2A."ssîjje    \\\\\n";
		print FILE "\\textsc{2p} & ʔi".$theme_2A."̂nsini  & ʔi".$theme_2A."̂ntɛnnu &".$theme_2A."̂nnuje  \\\\ \n";
		print FILE "\\textsc{3s} & ".$theme_2A."̂nsi & ".$theme_2A."̂ntɛsi   \\\\ \n";
		print FILE "\\textsc{3d} & ".$theme_2A."ssiji"." & ".$theme_2A."ssîjti   \\\\ \n";
		print FILE "\\textsc{3p} & ".$theme_2A."̂nsinu  & ".$theme_2A."̂ntɛnnu \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	}
close(FILE);
}
	

open FICHIER, "<:utf8", "reflexive_verbs.txt";



while (<FICHIER>) {
#my $donnees = <FICHIER>;
 
my ($donnees)= $_;
chomp($donnees);
my @mots = split('-',$donnees);

 #foreach my $entree (@mots) {	
    generation ($mots[0], $mots[2], $mots[1]);
	#print $entree;

}
close(FICHIER);


