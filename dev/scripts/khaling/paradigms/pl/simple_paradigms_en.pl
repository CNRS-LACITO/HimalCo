use strict;
use warnings;

use utf8;


	my $partie1 = "";
	my $partie2 = "";
	my $theme_A = "";
	my $theme_B = "";
	my $theme_B2 = "";
	my $theme_C = "";
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
    $partie2 =~ s/([aʌieɛuoɔɵʉ])t/$1̂j/;
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
    $radical =~ s/([aʌieɛuoɔɵʉ])([mnŋrlj])/$1̂$2/;
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
    $radical =~ s/ː([mnŋrlj])/$1/; #supprimer longueurs en syllabe fermée de sonantes
	$radical =~ s/ː̂([mnŋrlj])/̂$1/;
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
	open (FILE, ">>:utf8", "b.txt");
	my ($variable1) = $_[0];
	my ($variable2) = $_[1];
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
	if  ((substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]t")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]n")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]nt")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]ʦ")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]tt")|(substr($radical,-2,2) =~ "[aeiouɛɵʉɔʌ]s")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːs")|(substr($radical,-3,) =~ "[aeiouɛɵʉɔʌ]ːʦ"))	 { 
			$voyelle1 = "";
			$voyelle2 = "";
			$voyelle3 = "";
	}
	#print FILE $theme_A."ŋʌ"."   ".$theme_B."i"." ". $theme_C."ki"." ".$theme_D." ".$theme_E."ni ".$theme_F.$voyelle1."ti  ".$theme_H."tɛ \n";

			print FILE "\n";
			print FILE "\n";
	if ($variable1 =~ /[ptkmnŋrl].i$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vi}\n";
		print FILE "\\caption{Intransitive verb \\ipa{".$radical. "} ``".$variable2."\"  }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s &".$theme_A."ŋʌ"." &".$theme_F.$voyelle2."tʌ \\\\ \n";
		print FILE "1di &".$theme_B."i"." &".$theme_F.$voyelle1."ti   \\\\\n";
		print FILE "1de &".$theme_B."u"." &".$theme_F.$voyelle3."tu   \\\\ \n";
		print FILE "1pi &".$theme_C."ki"." &".$theme_C."tiki   \\\\ \n";
		print FILE "1pe &".$theme_C."kʌ"." &".$theme_C."tʌkʌ   \\\\ \n";
		print FILE "2s & ʔi".$theme_D." & ʔi".$theme_G2."tɛ &".$theme_B2."e  \\\\ \n";
		print FILE "2d & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti &".$theme_B."ije    \\\\\n";
		print FILE "2n & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje  \\\\ \n";
		print FILE "3s & ".$theme_D." & ".$theme_G2."tɛ   \\\\ \n";
		print FILE "3d & ".$theme_B."i"." & ".$theme_F.$voyelle1."ti   \\\\ \n";
		print FILE "3n & ".$theme_E."nu  & ".$theme_G."tɛnu \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	}
	elsif ($variable1 =~ /[aɛeiou].i$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vi}\n";
		print FILE "\\caption{Intransitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s &".$theme_2A."ŋʌ"." &".$theme_2A."ŋʌtʌ \\\\ \n";
		print FILE "1di &".$theme_2A."ji"." &".$theme_2A."̂iti   \\\\\n";
		print FILE "1de &".$theme_2A."ju"." &".$theme_2A."̂itu   \\\\ \n";
		print FILE "1pi &".$theme_2A."ki"." &".$theme_2A."ktiki   \\\\ \n";
		print FILE "1pe &".$theme_2A."kʌ"." &".$theme_2A."ktʌkʌ   \\\\ \n";
		print FILE "2s & ʔi".$theme_2A." & ʔi".$theme_2B."tɛ &".$theme_2B."je  \\\\ \n";
		print FILE "2d & ʔi".$theme_2A."ji"." & ʔi".$theme_2A."̂iti &".$theme_B."̂ije    \\\\\n";
		print FILE "2n & ʔi".$theme_2A."ni  & ʔi".$theme_2B2."tnu &".$theme_2B2."̂nje  \\\\ \n";
		print FILE "3s & ".$theme_2A." & ".$theme_2B."tɛ   \\\\ \n";
		print FILE "3d & ".$theme_2A."ji"." & ".$theme_2A."̂iti     \\\\ \n";
		print FILE "3n & ".$theme_2A."nu  & ".$theme_2B2."tnu \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	}
	
	if ($variable1 =~ /[ptkmnŋrl]t_t$/) {

		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Transitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s>3s &".$theme_O."u"." &".$theme_N."tʌ \\\\ \n";
		print FILE "1s>3d &".$theme_O."usu"." &".$theme_N."tʌsu \\\\ \n";
		print FILE "1s>3p &".$theme_O."unu"." &".$theme_N."tʌnu \\\\ \n";
		print FILE "1di>3 &".$theme_B."i"." &".$theme_F.$voyelle1."ti   \\\\\n";
		print FILE "1de>3 &".$theme_B."u"." &".$theme_F.$voyelle3."tu   \\\\ \n";
		print FILE "1pi>3 &".$theme_C."ki"." &".$theme_C."tiki   \\\\ \n";
		print FILE "1pe>3 &".$theme_C."kʌ"." &".$theme_C."tʌkʌ   \\\\ \n";
		print FILE "2s>3s & ʔi".$theme_O."ʉ  & ʔi".$theme_N."tɛ &".$theme_O."e  \\\\ \n";
		print FILE "2s>3d & ʔi".$theme_N."su  & ʔi".$theme_N."tɛsu   \\\\ \n";
		print FILE "2s>3p & ʔi".$theme_N."nu  & ʔi".$theme_N."tɛnu   \\\\ \n";
		print FILE "2d>3 & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti &".$theme_B."ije    \\\\\n";
		print FILE "2n>3 & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje  \\\\ \n";
		print FILE "3s>3s & ".$theme_O."ʉ  & ".$theme_N."tɛ  \\\\ \n";
		print FILE "3>3(d) & ".$theme_N."su"." & ".$theme_N."tɛsu  \\\\ \n";
		print FILE "3>3(p) & ".$theme_N."nu  & ".$theme_N."tɛnu \\\\ \n";
		print FILE "\\midrule\n";
		print FILE "2/3s>1s &ʔi".$theme_A."ŋʌ"." &ʔi".$theme_F.$voyelle2."tʌ &".$theme_B."ʌje \\\\ \n";
		print FILE "2/3d>1s &ʔi".$theme_A."ŋʌsu"." &ʔi".$theme_F.$voyelle2."tʌsu &".$theme_B."ʌsuje \\\\ \n";
		print FILE "2/3p>1s &ʔi".$theme_A."ŋʌnu"." &ʔi".$theme_F.$voyelle2."tʌnu &".$theme_B."ʌnuje \\\\ \n";
		print FILE "2/3>1di &ʔi".$theme_B."i"." &ʔi".$theme_F.$voyelle1."ti    \\\\\n";
		print FILE "2/3>1de &ʔi".$theme_B."u"." &ʔi".$theme_F.$voyelle3."tu  &".$theme_B."uje  \\\\ \n";
		print FILE "2/3>1pi &ʔi".$theme_C."ki"." &ʔi".$theme_C."tiki   \\\\ \n";
		print FILE "2/3>1pe &ʔi".$theme_C."kʌ"." &ʔi".$theme_C."tʌkʌ  &".$theme_C."kʌje  \\\\ \n";
		print FILE "3>2s, 1d/pe>2s & ʔi".$theme_D." & ʔi".$theme_G2."tɛ   \\\\ \n";
		print FILE "3>2d, 1d/pe>2d & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti    \\\\\n";
		print FILE "3>2p, 1d/pe>2p & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu  \\\\ \n";
		print FILE "\\midrule\n";
		print FILE "1s>2s & ".$theme_E."nɛ  & ".$theme_P."tɛni  \\\\ \n";
		print FILE "1s>2d & ".$theme_M."su  & ".$theme_P."tɛnsu   \\\\ \n";
		print FILE "1s>2p& ".$theme_M."nu  & ".$theme_P."tɛnnu   \\\\ \n";		
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	
}

	elsif ($variable1 =~ /[ptkmnŋrl]_t$/) {
	#print FILE $theme_H."u ".$theme_I."ʉ  ". $theme_J."nu ".$theme_K.$voyelle3."ta ".$theme_L."tɛ " .$theme_M."su \n";
	
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Transitive verb \\ipa{".$radical. "}  ``".$variable2."\"}\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s>3s &".$theme_H."u"." &".$theme_K.$voyelle3."tʌ \\\\ \n";
		print FILE "1s>3d &".$theme_H."usu"." &".$theme_K.$voyelle3."tʌsu \\\\ \n";
		print FILE "1s>3p &".$theme_H."unu"." &".$theme_K.$voyelle3."tʌnu \\\\ \n";
		print FILE "1di>3 &".$theme_B."i"." &".$theme_F.$voyelle1."ti   \\\\\n";
		print FILE "1de>3 &".$theme_B."u"." &".$theme_F.$voyelle3."tu   \\\\ \n";
		print FILE "1pi>3 &".$theme_C."ki"." &".$theme_C."tiki   \\\\ \n";
		print FILE "1pe>3 &".$theme_C."kʌ"." &".$theme_C."tʌkʌ   \\\\ \n";
		print FILE "2s>3s & ʔi".$theme_I."ʉ  & ʔi".$theme_L."tɛ &".$theme_I."e  \\\\ \n";
		print FILE "2s>3d & ʔi".$theme_J."su  & ʔi".$theme_L."tɛsu   \\\\ \n";
		print FILE "2s>3p & ʔi".$theme_J."nu  & ʔi".$theme_L."tɛnu   \\\\ \n";
		print FILE "2d>3 & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti &".$theme_B."ije    \\\\\n";
		print FILE "2n>3 & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje  \\\\ \n";
		print FILE "3s>3s & ".$theme_I."ʉ  & ".$theme_L."tɛ  \\\\ \n";
		print FILE "3>3(d) & ".$theme_J."su"." & ".$theme_L."tɛsu  \\\\ \n";
		print FILE "3>3(p) & ".$theme_J."nu  & ".$theme_L."tɛnu \\\\ \n";
		print FILE "\\midrule\n";
		print FILE "2/3s>1s &ʔi".$theme_A."ŋʌ"." & ʔi".$theme_F.$voyelle2."tʌ &".$theme_B."ʌje \\\\ \n";
		print FILE "2/3d>1s &ʔi".$theme_A."ŋʌsu"." & ʔi".$theme_F.$voyelle2."tʌsu &".$theme_B."ʌsuje \\\\ \n";
		print FILE "2/3p>1s &ʔi".$theme_A."ŋʌnu"." & ʔi".$theme_F.$voyelle2."tʌnu &".$theme_B."ʌnuje \\\\ \n";
		print FILE "2/3>1di & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti    \\\\\n";
		print FILE "2/3>1de & ʔi".$theme_B."u"." & ʔi".$theme_F.$voyelle3."tu  &".$theme_B."uje  \\\\ \n";
		print FILE "2/3>1pi & ʔi".$theme_C."ki"." & ʔi".$theme_C."tiki   \\\\ \n";
		print FILE "2/3>1pe & ʔi".$theme_C."kʌ"." & ʔi".$theme_C."tʌkʌ  &".$theme_C."kʌje  \\\\ \n";
		print FILE "3>2s, 1d/pe>2s & ʔi".$theme_D." & ʔi".$theme_G2."tɛ   \\\\ \n";
		print FILE "3>2d, 1d/pe>2d & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti    \\\\\n";
		print FILE "3>2p, 1d/pe>2p & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu  \\\\ \n";
		print FILE "\\midrule\n";
		print FILE "1s>2s & ".$theme_E."nɛ  & ".$theme_P."tɛni  \\\\ \n";
		print FILE "1s>2d & ".$theme_M."su  & ".$theme_P."tɛnsu   \\\\ \n";
		print FILE "1s>2p& ".$theme_M."nu  & ".$theme_P."tɛnnu   \\\\ \n";		
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
		
}

	elsif ($variable1 =~ /[aeiou]_t$/) {

	
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Transitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s &".$theme_2D."ŋʌ"." &".$theme_2E."̂ŋtʌ \\\\ \n";
		print FILE "1di &".$theme_2C."ji"." &".$theme_2C."̂iti   \\\\\n";
		print FILE "1de &".$theme_2C."ju"." &".$theme_2C."̂itu   \\\\ \n";
		print FILE "1pi &".$theme_2C."ki"." &".$theme_2C."ktiki   \\\\ \n";
		print FILE "1pe &".$theme_2C."kʌ"." &".$theme_2C."ktʌkʌ   \\\\ \n";
		print FILE "2s & ʔi".$theme_2A." & ʔi".$theme_2F."tɛ &".$theme_2F."je  \\\\ \n";
		print FILE "2d & ʔi".$theme_2C."ji"." & ʔi".$theme_2C."̂iti &".$theme_2C."̂ije    \\\\\n";
		print FILE "2n & ʔi".$theme_2C."ni  & ʔi".$theme_2G2."tnu &".$theme_2G2."̂nje  \\\\ \n";
		print FILE "3s & ".$theme_2A." & ".$theme_2F."tɛ   \\\\ \n";
		print FILE "3d & ".$theme_2A."su"." & ".$theme_2F."tsu     \\\\ \n";
		print FILE "3n & ".$theme_2A."nu  & ".$theme_2F."tnu \\\\ \n";
		print FILE "\\midrule\n";
		print FILE "2/3s>1s &ʔi".$theme_2C."ŋʌ"." &ʔi".$theme_2C."ŋʌtʌ &".$theme_2C."ŋʌje \\\\ \n";
		print FILE "2/3d>1s &ʔi".$theme_2C."ŋʌsu"." &ʔi".$theme_2C."ŋʌtʌsu &".$theme_2C."ŋʌsuje \\\\ \n";
		print FILE "2/3p>1s &ʔi".$theme_2C."ŋʌnu"." &ʔi".$theme_2C."ŋʌtʌnu &".$theme_2C."ŋʌnuje \\\\ \n";
		print FILE "2/3>1di &ʔi".$theme_2C."ji"." &ʔi".$theme_2C."̂iti    \\\\\n";
		print FILE "2/3>1de &ʔi".$theme_2C."ju"." &ʔi".$theme_2C."̂itu  &".$theme_2C."ije  \\\\ \n";
		print FILE "2/3>1pi &ʔi".$theme_2C."ki"." &ʔi".$theme_2C."ktiki   \\\\ \n";
		print FILE "2/3>1pe &ʔi".$theme_2C."kʌ"." &ʔi".$theme_2C."ktʌkʌ  &".$theme_2C."kʌje  \\\\ \n";
		print FILE "3>2s, 1d/pe>2s & ʔi".$theme_2C." & ʔi".$theme_2G."tɛ   \\\\ \n";
		print FILE "3>2d, 1d/pe>2d & ʔi".$theme_2C."ji"." & ʔi".$theme_2C."̂iti     \\\\\n";
		print FILE "3>2p, 1d/pe>2p & ʔi".$theme_2C."ni  & ʔi".$theme_2G2."tnu  \\\\ \n";
		print FILE "\\midrule\n";
		print FILE "1s>2s & ".$theme_2C."nɛ  & ".$theme_2C."̂ntɛni  \\\\ \n";
		print FILE "1s>2d & ".$theme_2C."̂nsu  & ".$theme_2C."̂ntɛnsu   \\\\ \n";
		print FILE "1s>2p& ".$theme_2C."̂nnu  & ".$theme_2C."̂ntɛnnu   \\\\ \n";		
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
}		
if ($variable1 =~ /[ptkmnŋrl]t_1$/) {

		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Transitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s>3s &".$theme_O."u"." &".$theme_N."tʌ \\\\ \n";
		print FILE "1s>3d &".$theme_O."usu"." &".$theme_N."tʌsu \\\\ \n";
		print FILE "1s>3p &".$theme_O."unu"." &".$theme_N."tʌnu \\\\ \n";
		print FILE "1di>3 &".$theme_B."i"." &".$theme_F.$voyelle1."ti   \\\\\n";
		print FILE "1de>3 &".$theme_B."u"." &".$theme_F.$voyelle3."tu   \\\\ \n";
		print FILE "1pi>3 &".$theme_C."ki"." &".$theme_C."tiki   \\\\ \n";
		print FILE "1pe>3 &".$theme_C."kʌ"." &".$theme_C."tʌkʌ   \\\\ \n";
		print FILE "2s>3s & ʔi".$theme_O."ʉ  & ʔi".$theme_N."tɛ &".$theme_O."e  \\\\ \n";
		print FILE "2s>3d & ʔi".$theme_N."su  & ʔi".$theme_N."tɛsu   \\\\ \n";
		print FILE "2s>3p & ʔi".$theme_N."nu  & ʔi".$theme_N."tɛnu   \\\\ \n";
		print FILE "2d>3 & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti &".$theme_B."ije    \\\\\n";
		print FILE "2n>3 & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje  \\\\ \n";
		print FILE "3s>3s & ".$theme_O."ʉ  & ".$theme_N."tɛ  \\\\ \n";
		print FILE "3>3(d) & ".$theme_N."su"." & ".$theme_N."tɛsu  \\\\ \n";
		print FILE "3>3(p) & ".$theme_N."nu  & ".$theme_N."tɛnu \\\\ \n";	
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	}
	elsif ($variable1 =~ /[ptkmnŋrl]_1$/) {
	
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Transitive verb \\ipa{".$radical. "}  ``".$variable2."\"}\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s>3s &".$theme_H."u"." &".$theme_K.$voyelle3."tʌ \\\\ \n";
		print FILE "1s>3d &".$theme_H."usu"." &".$theme_K.$voyelle3."tʌsu \\\\ \n";
		print FILE "1s>3p &".$theme_H."unu"." &".$theme_K.$voyelle3."tʌnu \\\\ \n";
		print FILE "1di>3 &".$theme_B."i"." &".$theme_F.$voyelle1."ti   \\\\\n";
		print FILE "1de>3 &".$theme_B."u"." &".$theme_F.$voyelle3."tu   \\\\ \n";
		print FILE "1pi>3 &".$theme_C."ki"." &".$theme_C."tiki   \\\\ \n";
		print FILE "1pe>3 &".$theme_C."kʌ"." &".$theme_C."tʌkʌ   \\\\ \n";
		print FILE "2s>3s & ʔi".$theme_I."ʉ  & ʔi".$theme_L."tɛ &".$theme_I."e  \\\\ \n";
		print FILE "2s>3d & ʔi".$theme_J."su  & ʔi".$theme_L."tɛsu   \\\\ \n";
		print FILE "2s>3p & ʔi".$theme_J."nu  & ʔi".$theme_L."tɛnu   \\\\ \n";
		print FILE "2d>3 & ʔi".$theme_B."i"." & ʔi".$theme_F.$voyelle1."ti &".$theme_B."ije    \\\\\n";
		print FILE "2n>3 & ʔi".$theme_E."ni  & ʔi".$theme_G."tɛnu &".$theme_G."nuje  \\\\ \n";
		print FILE "3s>3s & ".$theme_I."ʉ  & ".$theme_L."tɛ  \\\\ \n";
		print FILE "3>3(d) & ".$theme_J."su"." & ".$theme_L."tɛsu  \\\\ \n";
		print FILE "3>3(p) & ".$theme_J."nu  & ".$theme_L."tɛnu \\\\ \n";	
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	
	}
	
	if ($variable1 =~ /[aeiou]_1$/) {

	
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vi}\n";
		print FILE "\\caption{Transitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past & imperative \\\\ \n";
		print FILE "1s &".$theme_2D."ŋʌ"." &".$theme_2E."̂ŋtʌ \\\\ \n";
		print FILE "1di &".$theme_2C."ji"." &".$theme_2C."̂iti   \\\\\n";
		print FILE "1de &".$theme_2C."ju"." &".$theme_2C."̂itu   \\\\ \n";
		print FILE "1pi &".$theme_2C."ki"." &".$theme_2C."ktiki   \\\\ \n";
		print FILE "1pe &".$theme_2C."kʌ"." &".$theme_2C."ktʌkʌ   \\\\ \n";
		print FILE "2s & ʔi".$theme_2A." & ʔi".$theme_2F."tɛ &".$theme_2F."je  \\\\ \n";
		print FILE "2d & ʔi".$theme_2C."ji"." & ʔi".$theme_2C."̂iti &".$theme_2C."̂ije    \\\\\n";
		print FILE "2n & ʔi".$theme_2C."ni  & ʔi".$theme_2G2."tnu &".$theme_2G2."̂nje  \\\\ \n";
		print FILE "3s & ".$theme_2A." & ".$theme_2F."tɛ   \\\\ \n";
		print FILE "3d & ".$theme_2A."su"." & ".$theme_2F."tsu     \\\\ \n";
		print FILE "3n & ".$theme_2A."nu  & ".$theme_2F."tnu \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
		}
	if ($variable1 =~ /[ptkmnŋrl]t_2$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Detransitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past  \\\\ \n";
		print FILE "3s & ".$theme_O."ʉ  & ".$theme_N."tɛ  \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
		
	}
		elsif ($variable1 =~ /[ptkmnŋrl]_2$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vt}\n";
		print FILE "\\caption{Detransitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past  \\\\ \n";
		print FILE "3s & ".$theme_O."ʉ  & ".$theme_N."tɛ  \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
		}
	if ($variable1 =~ /[ptkmnŋrl]_3$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vi}\n";
		print FILE "\\caption{Intransitive verb \\ipa{".$radical. "} ``".$variable2."\"  }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past  \\\\ \n";
		print FILE "3s & ".$theme_D." & ".$theme_G2."tɛ   \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	}
	elsif ($variable1 =~ /[aɛeiou]_3$/) {
		print FILE "\\begin{table}[H]\n";
		print FILE "\\label{".$rime.".vi}\n";
		print FILE "\\caption{Intransitive verb \\ipa{".$radical. "} ``".$variable2."\" }\n";
		print FILE "\\begin{tabular}{l|l|l|l|l|l|l|l|l|l|l}  \\toprule\n";
		print FILE "&non-past & past  \\\\ \n";
		print FILE "3s & ".$theme_2A." & ".$theme_2B."tɛ   \\\\ \n";
		print FILE "\\bottomrule\n";
		print FILE "\\end{tabular}\n";
		print FILE "\\end{table}\n";
	}
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


