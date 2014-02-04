use strict;
use warnings;

use utf8;


open FICHIER, "<:utf8", "d.txt";
open FICHIER2, ">:utf8", "texte3.txt";

 
sub consonne {



$_[0] =~ s/$_[1]$/$_[2]्/g;
$_[0] =~ s/$_[1] /$_[2]् /g;
$_[0] =~ s/$_[1]ʌ/$_[2]/g;
$_[0] =~ s/$_[1]([ा,ि,ी,ु,ू,े,ो,ै,ौ])/$_[2]$1/g;
$_[0] =~ s/$_[1]/$_[2]्/g;
$_[0] =~ s/$_[1]/$_[2]्/g;
 

}
 #my(@lines) = <FICHIER>:
  
#foreach $lettre (@lines) {

while (<FICHIER>) 
{
#print "b";
my $lettre = $_;
if ($lettre =~ m/LABEL/) {}
else  {
  $lettre =~ s/ː([ptk][ptkbdgmnŋrlsʦʣ])/̂ː$1/g;
  $lettre =~ s/ː([ptk]\W)/̂ː$1/g;
  $lettre =~ s/([aeiouɛʌɵʉ])ː/$1̄ː/g;

$lettre =~s/ʔɛ̂i([ptkbdgmʦʣɦnŋlrsjw\W])/अ्या:इ$1/g;
$lettre =~s/ʔɛ̄i([ptkbdgmʦʣɦnŋlrsjw\W])/अ्याइ$1/g;
$lettre =~s/ʔɛi([ptkbdgmʦʣɦnŋlrsjw\W])/अ्याइ$1/g;
$lettre =~s/ʔɛ̄ː([ptkmnŋlrsjç][ptkbdgʦʣmɦnŋlrsjw\W])/अ्याऽ$1/g;
$lettre =~s/ʔɛ̂ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/या:$1/g;
$lettre =~s/ʔɛː([ptkmnŋlrsjç][ptkbdgʦʣmɦnŋlrsjw\W])/अ्याऽ$1/g;
$lettre =~s/ʔɛ̂([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/अ्या:$1/g;
$lettre =~s/ʔɛ̄([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/अ्या$1/g;
$lettre =~s/ʔɛ([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjw\W])/अ्या$1/g;
$lettre =~s/ʔɛː/अ्या/g;
$lettre =~s/ʔɛ̄ː/अ्या/g;
$lettre =~s/ʔɛ̂ː/अ्या:/g;
$lettre =~s/ʔɛ/अ्य/g;
$lettre =~s/ɛu/याउ/g;
$lettre =~s/ɛ‍̄u/याउ/g;
$lettre =~s/ɛː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjwअ\W])/याऽ$1/g;
$lettre =~s/ɛ̄ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjwअ\W])/याऽ$1/g;
$lettre =~s/ɛ̂ː([ptkmnŋlrsjç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या:$1/g;
$lettre =~s/ɛ̂i([ptkbdgmʦʣɦʔnŋlrsjwअ\W])/या:इ$1/g;
$lettre =~s/ɛ̄i([ptkbdgmʦʣɦʔnŋlrsjwअ\W])/याइ$1/g;
$lettre =~s/ɛi([ptkbdgmʦʣɦʔnŋlrsjwअ\W])/याइ$1/g;
$lettre =~s/ɛ̂([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या:$1/g;
$lettre =~s/ɛ̄([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या$1/g;
$lettre =~s/ɛ([ptkmnŋlrsijç][ptkbdgmʦʣɦnŋlrsjwअ\W])/या$1/g;
$lettre =~s/ɛː/या/g;
$lettre =~s/ɛ̄ː/या/g;
$lettre =~s/ɛ̂ː/या:/g;
$lettre =~s/ɛ/य/g;

$lettre =~s/ʔʌi/ऐ/g;
$lettre =~s/ʔʌ̄i/ऐ/g;
$lettre =~s/ʔʌ̂i/ऐ:/g;
$lettre =~s/ʔʌu/औ/g;
$lettre =~s/ʔʌ̄u/औ/g;
$lettre =~s/ʔʌ̂u/औ:/g;
$lettre =~s/ʌi/ै/g;
$lettre =~s/ʌ̄i/ै/g;
$lettre =~s/ʌ̂i/ै:/g;
$lettre =~s/ʌu/ौ/g;
$lettre =~s/ʌ̄u/ौ/g;
$lettre =~s/ʌ‍̂u/ौ:/g;
$lettre =~s/ēu/ेउ/g;
$lettre =~s/eu/ेउ/g;

$lettre =~ s/̄i/̄इ/g;
$lettre =~ s/̂i/̂इ/g;
$lettre =~ s/([aeɛiouɵʉʌɔ])i/$1इ/g;

$lettre =~ s/ʔʌ/अ/g;
$lettre =~ s/ʔa/आ/g;
$lettre =~ s/ʔoɔ/अ्वा/g;
$lettre =~ s/ʔâː/आ:/g;
$lettre =~ s/ʔoɔ̂/अ्वा:/g;
$lettre =~ s/âː/ा:/g;
$lettre =~ s/āː/ाऽ/g;
$lettre =~ s/aː/ाऽ/g;
$lettre =~ s/a/ा/g;
$lettre =~ s/oɔ̂/वा:/g;
$lettre =~ s/oɔ̄/वा/g;
$lettre =~ s/oɔ/वा/g;



$lettre =~ s/ʔīː/इऽ/g;
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
$lettre =~ s/ʔu‍̂ː/ऊ:/g;
$lettre =~ s/ʔu/उ/g;
$lettre =~ s/ūː/ुऽ/g;
$lettre =~ s/uː/ुऽ/g;
$lettre =~ s/ûː/ु:/g;
$lettre =~ s/u/ु/g;

$lettre =~ s/ʔēː/एऽ/g;
$lettre =~ s/ʔe‍̂ː/ए:/g;
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
}
$lettre =~ tr/[A-Z]/[a-z]/;
#lettre =~ tr/\[h\]/\[H\]/;
print FICHIER2 $lettre;



}
close(FICHIER);




close(FICHIER2);