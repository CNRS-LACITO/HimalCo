use strict;
use warnings;

use utf8;

sub consonne {



$_[0] =~ s/$_[1]$/$_[2]्/g;
$_[0] =~ s/$_[1] /$_[2]् /g;
$_[0] =~ s/$_[1]ʌ/$_[2]/g;
$_[0] =~ s/$_[1]([ा,ि,ी,ु,ू,े,ो])/$_[2]$1/g;
$_[0] =~ s/$_[1]/$_[2]्/g;
$_[0] =~ s/$_[1]/$_[2]्/g;
 

}


sub transcr {
my $lettre = $_[0];

$lettre =~s/ʔɛ̂i([ptkbdgmʦʣɦnŋlrsj\W])/अ्या:इ$1/g;
$lettre =~s/ʔɛ̄i([ptkbdgmʦʣɦnŋlrsj\W])/अ्याइ$1/g;
$lettre =~s/ʔɛi([ptkbdgmʦʣɦnŋlrsj\W])/अ्याइ$1/g;
$lettre =~s/ʔɛ̄ː([ptkmnŋlrsjç][ptkbdgʦʣmɦnŋlrsj\W])/अ्याऽ$1/g;
$lettre =~s/ʔɛ̂ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsj\W])/या:$1/g;
$lettre =~s/ʔɛː([ptkmnŋlrsjç][ptkbdgʦʣmɦnŋlrsj\W])/अ्याऽ$1/g;
$lettre =~s/ʔɛ̂([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsj\W])/अ्या:$1/g;
$lettre =~s/ʔɛ̄([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsj\W])/अ्या$1/g;
$lettre =~s/ʔɛ([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsj\W])/अ्या$1/g;
$lettre =~s/ʔɛː/अ्या/g;
$lettre =~s/ʔɛ̄ː/अ्या/g;
$lettre =~s/ʔɛ̂ː/अ्या:/g;
$lettre =~s/ʔɛ/अ्य/g;
$lettre =~s/ɛː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjअ\W])/याऽ$1/g;
$lettre =~s/ɛ̄ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjअ\W])/याऽ$1/g;
$lettre =~s/ɛ̂ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjअ\W])/या:$1/g;
$lettre =~s/ɛ̂i([ptkbdgmʦʣɦʔnŋlrsjअ\W])/या:इ$1/g;
$lettre =~s/ɛ̄i([ptkbdgmʦʣɦʔnŋlrsjअ\W])/याइ$1/g;
$lettre =~s/ɛi([ptkbdgmʦʣɦʔnŋlrsjअ\W])/याइ$1/g;
$lettre =~s/ɛ̂([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjअ\W])/या:$1/g;
$lettre =~s/ɛ̄([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjअ\W])/या$1/g;
$lettre =~s/ɛ([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjअ\W])/या$1/g;
$lettre =~s/ɛː/या/g;
$lettre =~s/ɛ̄ː/या/g;
$lettre =~s/ɛ̂ː/या:/g;
$lettre =~s/ɛ/य/g;

$lettre =~ s/̄i/̄इ/g;
$lettre =~ s/̂i/̂इ/g;
$lettre =~ s/([aeɛiouɵʉʌɔ])i/$1इ/g;

$lettre =~ s/ʔʌ/अ/g;
$lettre =~ s/ʔa/आ/g;
$lettre =~ s/ʔoɔ/अ्वा/g;
$lettre =~ s/ʔâː/आ:/g;
$lettre =~ s/ʔoɔ̂/अ्वा:/g;
$lettre =~ s/âː/ा:/g;
$lettre =~ s/aː/ाऽ/g;
$lettre =~ s/āː/ाऽ/g;
$lettre =~ s/aː/ाऽ/g;
$lettre =~ s/a/ा/g;
$lettre =~ s/oɔ̂/वा:/g;
$lettre =~ s/oɔ̄/वा/g;
$lettre =~ s/oɔ/वा/g;



$lettre =~ s/ʔīː/इऽ/g;
$lettre =~ s/ʔiː/इऽ/g;
$lettre =~ s/ʔîː/इ:/g;
$lettre =~ s/ʔi/इ/g;
$lettre =~ s/īː/िऽ/g;
$lettre =~ s/iː/िऽ/g;
$lettre =~ s/îː/ि:/g;
$lettre =~ s/i/ि/g;

$lettre =~s/ʔʉ/अ्यu/g;
$lettre =~s/ʉ/यu/g;

$lettre =~s/ʔɵ/अ्यo/g;
$lettre =~s/ɵ/यo/g;



$lettre =~ s/ʔūː/ऊ/g;
$lettre =~ s/ʔuː/ऊ/g;
$lettre =~ s/ʔûː/ऊ:/g;
$lettre =~ s/ʔu/उ/g;
$lettre =~ s/ūː/ुऽ/g;
$lettre =~ s/uː/ुऽ/g;
$lettre =~ s/ûː/ु:/g;
$lettre =~ s/u/ु/g;

$lettre =~ s/ʔēː/एऽ/g;
$lettre =~ s/ʔêː/ए:/g;
$lettre =~ s/ʔe/ए/g;
$lettre =~ s/ēː/ेऽ/g;
$lettre =~ s/eː/ेऽ/g;
$lettre =~ s/êː/े:/g;
$lettre =~ s/e/े/g;

$lettre =~ s/ʔoː/ओऽ/g;
$lettre =~ s/ʔōː/ओऽ/g;
$lettre =~ s/ʔôː/ओ:/g;
$lettre =~ s/ʔo/ओ/g;
$lettre =~ s/ōː/ोऽ/g;
$lettre =~ s/oː/ोऽ/g;
$lettre =~ s/ôː/ो:/g;
$lettre =~ s/o/ो/g;

$lettre =~ s/̂/:/g;
$lettre =~ s/̄//g;
#$lettre =~ s/k$/क्/g;
#$lettre =~ s/k /क् /g;
#$lettre =~ s/ka/क/g;
#$lettre =~ s/k([ि,ी,ु,ू,े,ो])/क$1/g;
#$lettre =~ s/k/क्/g;

&consonne($lettre,"kh","ख");
&consonne($lettre,"k","क");
&consonne($lettre,"gh","घ");
&consonne($lettre,"g","ग");
&consonne($lettre,"ŋ","ङ");

&consonne($lettre,"ʦh","छ");
&consonne($lettre,"ʦ","च");
&consonne($lettre,"ʣh","झ");
&consonne($lettre,"ʣ","ज");
&consonne($lettre,"ɲ","ञ");

&consonne($lettre,"ʈh","ठ");
&consonne($lettre,"ʈ","ट");
&consonne($lettre,"ɖh","झ");
&consonne($lettre,"ɖ","ड");
&consonne($lettre,"ɳ","ण");

&consonne($lettre,"th","थ");
&consonne($lettre,"t","त");
&consonne($lettre,"dh","ध");
&consonne($lettre,"d","द");
&consonne($lettre,"n","न");
 
&consonne($lettre,"ph","फ");
&consonne($lettre,"p","प");
&consonne($lettre,"bh","भ");
&consonne($lettre,"b","ब");
&consonne($lettre,"m","म");
&consonne($lettre,"ç","ह्इ");

&consonne($lettre,"r","र");
&consonne($lettre,"l","ल");
&consonne($lettre,"s","स");
&consonne($lettre,"w","व");
&consonne($lettre,"j","य");
&consonne($lettre,"ɦ","ह");

$lettre =~ s/ह्इ्/ह्इ/g;
$lettre =~ s/प्त/प्‍त/g;
$lettre =~ s/र्य/र्‍य/g;
$lettre =~ s/र्व/र्‍व/g;
$lettre =~ s/त्न/त्‍न/g;
$lettre =~ s/म्न/म्‍न/g;
$lettre =~ s/प्न/प्‍न/g;
$lettre =~ s/न्न/न्‍न/g;
$lettre =~ s/क्न/क्‍न/g;
$lettre =~ s/स्न/स्‍न/g;
$lettre =~ s/च्न/च्‌‍न/g;
$lettre =~ s/च्च/च्‌‍च/g;
$lettre =~ s/अ्वा/\\skt\{अ्\}वा/g;
$lettre =~ s/अ्य/\\skt\{अ्\}य/g;
$lettre =~ s/्ये/\\skt\{्\}ये/g;
$lettre =~ s/्‍ये/\\skt\{्\}ये/g;
$lettre =~ s/ुक्त/\\skt\{ुक्\}त/g;
$lettre =~ s/ुक्क/\\skt\{ुक्\}क/g;
$lettre =~ s/ुङ्/\\skt\{ुङ्\}/g;
$lettre =~ s/क्त/\\skt\{क्\}त/g;
$lettre =~ s/क्क/\\skt\{क्\}क/g;
$lettre =~ s/ङ्/\\skt\{ङ्\}/g;

$lettre =~ tr/[A-Z]/[a-z]/;

return $lettre;

}

sub voyelles {
		my ($radical) = shift;
		$radical =~ tr/uʉi/ʌʌʌ/;
		$radical =~ s/o/oɔ/;
		$radical =~ s/ɵ/oɔ/;
		return $radical;
}
	
sub infinitif1 {
	my ($radical) = shift;
	$radical =~s/(k|p|t|r|l|n|m|ŋ)(t|d)/$1/; #simplifie consonne finale
	my $variable = $radical;
	if ($radical =~ m/p$/) { #finales en -p
		$variable =~ s/p$/̂m/;
		$variable = voyelles($variable);
	}	

	if ($radical =~ m/t$/) { #finales en -t
		$variable =~ s/t$/̂n/;
		$variable = voyelles($variable);
	}	
	
	if ($radical =~ m/k$/) { #finales en -k
		$variable =~ s/k$/̂ː/;
		$variable =~ tr/iɵʉ/uou/;
	}

	if ($radical =~ m/ŋ$/) { #finales en -ŋ
		$variable =~ s/ŋ$/ː/;
		$variable =~ tr/iɵʉ/uou/;
	}

	if ($radical =~ m/n$/) { #finales en -n
		$variable = voyelles($variable);
		$variable =~ s/n$/i/;
	}	

	if ($radical =~ m/(m|r|l)$/) { #finales en -r l m
		$variable = voyelles($variable);
	}
	
	$variable =~ tr/A/ɵ/;
	
	return $variable;	
}



sub infinitif2 {
	my ($radical) = shift;
	$radical =~ s/\-si//;
	$radical =~s/(k|p|t|r|l|n|m|ŋ)(t|d)/$1/; #simplifie consonne finale
	my $variable = $radical;
	
	if ($radical =~ m/(m|p|r|l|t|n)$/) {
		$variable = infinitif1($variable);
	}

	if ($radical =~ m/k$/) {		
		$variable =~ tr/iɵʉ/uou/;
		$variable =~ s/k$/̂n/;
	}
	
	if ($radical =~ m/ŋ$/) {		
		$variable =~ tr/iɵʉ/ʌou/;
		$variable =~ s/ŋ$/n/;
	}

	if ($radical =~ m/(a|ɛ|i|o|u|ɵ|ʉ|A)$/) {
		$variable =~ tr/ou/ɵʉ/;
		$variable = $variable."̂n";
	}
	
	return $variable."si";	
}

sub infinitif3 {
	my ($radical) = shift;
	my $variable = $radical;
	my $adverbe = $radical;
	$variable =~ s/\(.*\)//;
	$variable =~ s/ //;	
	$adverbe =~ s/.*\((.*)\).*/$1/;
	return $adverbe." ".infinitif($variable);
	#if ($variable =~ m/\-si$/) { #verbes reflechis
	#	$variable = infinitif2($variable); 
	#} 
}


sub infinitif {
	my ($radical) = shift;
	my $variable = $radical;
	if ($radical =~ m/\(.*\)/) { #verbes à adverbes
		$variable = infinitif3($variable); 
	}
	elsif ($radical =~ m/\-si$/) { #verbes reflechis
		$variable = infinitif2($variable); 
	} 
	else 	{$variable = infinitif1($variable); }
	return $variable;	
}


open FICHIER, "<:utf8", "Dictionary.txt";
open FICHIER2, ">:utf8", "dico-khaling";
my $counter = 0;
my $rime = "";
while (<FICHIER>) {
my ($donnees)= $_;
chomp($donnees);

	if ($donnees =~ m/^\\lx/) {
			
			$donnees =~ s/\\lx//;
			$donnees =~ s/ //;
			$rime = 	$donnees;
			$rime  =~ s/.*([aeiouɵʉɛ])/$1/;
			$rime  =~ tr/ɵʉ/ou/;
			print FICHIER2 "\\section*{\\nep{".transcr(infinitif($donnees)).transcr("nɛ")."}}\n";
			print FICHIER2 "\\ipa{\\textbf{".(infinitif($donnees))."nɛ}}\n";
			print FICHIER2 " (\\ipa{".$donnees."}) 	";
	}

	if ($donnees =~ m/^\\se/) {
			
			$donnees =~ s/\\se//;
			$donnees =~ s/ //;
			print FICHIER2 "\\subsection*{\\nep{".transcr(infinitif($donnees))."nɛ}}\n";
			print FICHIER2 "\\ipa{\\textbf{".(infinitif($donnees))."nɛ}}\n";
			print FICHIER2 " (\\ipa{".$donnees."})";
	}
	
	if ($donnees =~ m/^\\ps/) { #rajouter le nepali pour part of speech akarmak etc
			$donnees =~ s/\\ps//;
			$donnees =~ s/\(.*\)//;
			$donnees =~ s/ //;
			print FICHIER2 " \\ipa{".$donnees."}";
			if ($donnees =~ "vt") { print FICHIER2 " (Table \\ref{".$rime.".vt})";	}
			if ($donnees =~ "vi") { print FICHIER2 " (Table \\ref{".$rime.".vi})";	}
	}
	
	if ($donnees =~ m/^\\ge/) {
			$donnees =~ s/\\ge//;
			$donnees =~ s/ //;
			print FICHIER2 " \\engloss{``".$donnees."''}";
	}

	if ($donnees =~ m/^\\ue/) {
			$donnees =~ s/\\ue//;
			$donnees =~ s/ //;
			print FICHIER2 " \\engloss{usage:".$donnees."}";
	}
	
	if ($donnees =~ m/^\\gn/) {
			$donnees =~ s/\\gn//;
			$donnees =~ s/ //;
			print FICHIER2 "\\nep{".$donnees."}\n";
			print FICHIER2 "\n";
	}

	if ($donnees =~ m/^\\xv/) {
			$donnees =~ s/\\xv//;
			$donnees =~ s/ //;
			print FICHIER2 " \n\n \\nep{".transcr($donnees)."}";
			print FICHIER2 " \\ipa{".$donnees."}";
			$counter++;
	}
	
	if ($donnees =~ m/^\\xe/) {
			$donnees =~ s/\\xe//;
			$donnees =~ s/ //;
			print FICHIER2 "  \\engloss{".$donnees."} \n";
			print FICHIER2 "\n";
	}
	
	if ($donnees =~ m/^\\xn/) {
			$donnees =~ s/\\xn//;
			$donnees =~ s/ //;
			print FICHIER2 "  \\nep{".$donnees."}";
	}
	
	if ($donnees =~ m/^\\1s/) {
			$donnees =~ s/\\1s//;
			$donnees =~ s/ //;
			print FICHIER2 " 1sg: \\ipa{".$donnees."}   ".transcr($donnees);
	}

	if ($donnees =~ m/^\\1d/) {
			$donnees =~ s/\\1d//;
			$donnees =~ s/ //;
			print FICHIER2 " 1du: \\ipa{".$donnees."}   ".transcr($donnees);
	}

	if ($donnees =~ m/^\\1e/) {
			$donnees =~ s/\\1e//;
			$donnees =~ s/ //;
			print FICHIER2 " 1sg: \\ipa{".$donnees."}   ".transcr($donnees);
	}


	if ($donnees =~ m/^\\3s/) {
			$donnees =~ s/\\3s//;
			$donnees =~ s/ //;
			print FICHIER2 " 3sg: \\ipa{".$donnees."}   ".transcr($donnees);
	}

	if ($donnees =~ m/^\\4s/) {
			$donnees =~ s/\\4s//;
			$donnees =~ s/ //;
			print FICHIER2 " 3sg: \\ipa{".$donnees."}   ".transcr($donnees);
	}
	
}
close(FICHIER);
close(FICHIER2);

