#! C:\perl\bin\perl.exe


# Transforme un fichier initialement au format XML ITE en un fichier Toolbox

$var1 = $ARGV[0];

$temp=$var1;
$temp=~s/\.xml//g;


$text_in=$var1;
$text_out=$temp."_ok";


  open (IN, "$text_in")|| die "Probleme à l'ouverture du fichier d'entrée";

  open (OUT, ">$text_out")|| die "Probleme à l'ouverture du fichier de sortie";
 
$s=0;
$w=0;
$m=0;



while ($line=<IN>) {


	 # detection de la phrase et recuperation de l'identifiant
	if ($s==0 and $line=~m/<S(.*)>/){
			$s=1;
			$temp=$1;
			
			if ($temp=~m/id="(.*)"/){
			$rf=$1;
			print OUT "\\rf $rf\n";
			}
			
	}
	if ($s==1 and $line=~m/<W(.*)>/){
			$w=1;
			
	}
	if ($s==1 and $w==1 and $line=~m/<M(.*)>/){
			$m=1;
			
	}
	 # detection de la balise audio et recuperation des infos de synchronisation au niveau de la phrase
	if ($s==1 and $line=~m/<AUDIO(.*)\/>/){
			$temp=$1;

			if ($temp=~m/start="(.*?)"/){
			$start=$1;
			print OUT "\\sync_d $start\n";

			}
			
			if ($temp=~m/end="(.*?)"/){
			$end=$1;
			print OUT "\\sync_f $end\n";

			}		
	}
	
	# recuperation des transcriptions au niveau de la phrase puis du mot puis du morpheme
	if ($line=~m/<FORM(.*)>(.*)<\/FORM>/){
		if ($s==1 and $w==0 and $m==0){
			$s_form=$2;
			
		}
		if ($s==1 and $w==1 and $m==0){
			if (length($w_form)==0) {$w_form=$2;}
			else {$w_form=$w_form." ".$2;}
		}
		if ($s==1 and $w==1 and $m==1){
			if (length($m_form)==0) {$m_form=$2;}
			else {$m_form=$m_form." ".$2;}
		}

	}
	
	# recuperation des traductions/gloses au niveau de la phrase puis du mot puis du morpheme
	if ($line=~m/<TRANSL(.*)>(.*)<\/TRANSL>/){
		if ($s==1 and $w==0 and $m==0){
			$s_transl=$2;
		
		}
		if ($s==1 and $w==1 and $m==0){
			if (length($w_transl)==0) {$w_transl=$2;}
			else {$w_transl=$w_transl." ".$2;}
		}
		if ($s==1 and $w==1 and $m==1){
			if (length($m_transl)==0) {$m_transl=$2;}
			else {$m_transl=$m_transl." ".$2;}
		}

	}
	
	# reinitialisation des variables de detection
	if ($s==1 and $w==1 and $m==1 and $line=~m/<\/M.*/){
			$m=0;
			

		}
	if ($s==1 and $w==1 and $m==0 and $line=~m/<\/W.*/){
			$w=0;
			

		}
	if ($s==1 and $w==0 and $m==0 and $line=~m/<\/S.*/){
			$s=0;
			if (length($s_form)>0){print OUT "\\tx $s_form\n";}
			if (length($s_transl)>0){print OUT "\\ft $s_transl\n";}
			if (length($m_form)>0){print OUT "\\mb $m_form\n";}
			if (length($m_transl)>0){print OUT "\\ge $m_transl\n";}
			if (length($w_form)>0){print OUT "\\wb $w_form\n";}
			if (length($w_transl)>0){print OUT "\\wge $w_transl\n";}
			print OUT "\n";

			 $s_form="";
			 $w_form="";
			 $m_form="";
			 $s_transl="";
			 $w_transl="";
			 $m_transl="";
		}
	
	
}

	close(IN);
	close(OUT);
