# xxxx A FAIRE : ajouter les formes rédupliquées dans les formes alternatives des verbes

# Déclaration des modules utilisés
use Encode;		# pour décoder UTF-8
use utf8; 			# codage UTF-8 pour traiter des caractères Unicode. Autre option à explorer : use encoding 'utf-8-strict'; 
# "UTF-8 treats the first 128 codepoints, 0..127, the same as ASCII. They take only one byte per character. 
# All other characters are encoded as two or more (up to six) bytes using a complex scheme. 
# Fortunately, Perl handles this for us, so we don't have to worry about this."
use strict; 			# déclaration des variables
use warnings; 	

### use Lingua::ZH::CCDICT; # pour la conversion des caractères en pinyin. A installer.

### use List::Member; # équivalent d'une fonction ismember(x, Y) dont j'ai pris l'habitude dans MatLab; au final, n'est pas utilisée ds ce script

# Définition du chemin vers les fichiers d'entrée et de sortie
my $path_file_in = 'C:\Documents and Settings\alexis\Mes documents\My Dropbox\donneesNAISH\lexique_na_en_transfert_vers_Toolbox.txt';
my $path_file_out = 'C:\Documents and Settings\alexis\Mes documents\My Dropbox\donneesNAISH\naish\Dictionary.txt';

# Ouverture des fichiers texte employés en entrée et sortie. Si ça ne marche pas le script s'arrête.
# Structure du fichier pris en entrée : texte Unicode, délimité par des tabulations.
open my $in, '<', $path_file_in or die "Impossible de lire le fichier $path_file_in";
open my $out, '>', $path_file_out or die "Impossible d'écrire dans le fichier $path_file_out";

# Déclaration et initialisation de variables servant à la lecture et l'écriture de lignes des fichiers texte
my $ln_in = '';			# ligne lue d'Excel
my $ln_out = '';			# ligne préparée pour la sortie dans fichier texte
my $alternatives = '';	# chaîne (pouvant correspondre à plusieurs lignes) contenant les formes alternatives pour l'interlinéarisation
my @LIGNE = ();  	# ligne découpée en cellules
my $vides = ''; 			# lignes vides
my $cell = '';				# une cellule : correspond à une case dans le tableau Excel

# On définit les caractères tonals
my @tones = ("˩|˧|˥|˩˧|˧˥"); 

# On initialise une variable pour le ton : on en aura besoin à différents endroits du script.
my $ton = '';

# En-tête du fichier : toujours le même. 
print $out "\\_sh v3.0  100  MDF 4.0\n";
print $out "\\_DateStampHasFourDigitYear\n\n";

# On stocke les préfixes à ajouter pour Toolbox dans une liste.
# Préfixes à ajouter : 
# première colonne : \lx, lexème : le mot en na de Yongning. 
# deuxième colonne : trad. française, qu'on annonce comme anglaise pr des questions d'utilisation ultérieure. 
# Puis : chinois (gn), pinyin (py), exemples (xv), trad. des exemples en français (xe), classificateur (cl), sens du cl (cle), 
# anglais (gang), numéro d'enregistrement (enrt), sémantique, notes phonologiques, notes sémantiques, vérifs, 
# champ sémantique; données de F5, comm. F5, ex. F5, vérifs F5; idem pour M23; et une colonne pour M18 et une pour M21
my @pre =('lx', 'u', 'ge', 'gn', 'py', 'xv', 'xe', 'cl', 'cle', 'gang', 'enrt', 'nt_phon', 'nt_sem', 'nt_verifs', 'sem', 'lx_F5', 'nt_F5', 'xv_F5', 'nt_verifs_F5', 'lx_M23', 'nt_M23', 'xv_M23', 'nt_verifs_M23', 'lx_M18', 'lx_M21', 'a');
# On crée une sous-liste contenant les champs qu'il est utile d'indiquer même s'ils sont vides : exemples et leurs traductions, qui seront ainsi
# aisés à remplir par la suite.
my @pre_obl=('lx', 'u', 'ge', 'gn', 'py', 'xv', 'xe', 'cl', 'cle', 'gang', 'enrt', 'nt_phon', 'nt_sem', 'nt_verifs', 'sem');

# Préparation d'une boucle pour lire toutes les lignes. On initialise un compteur de lignes.
my $nb_ln = 0;

# On lit une première ligne : façon de laisser de côté la première ligne, simple en-tête
<$in>;

while (<$in>) {
	$ln_in = $_ ;
	# on incrémente le compteur de lignes
	$nb_ln++;
	# on commence par transformer la ligne de texte en une liste, en récupérant la division par tabulations
	@LIGNE = split(/\t/, $ln_in);

	# On initialise une variable-compteur i qui servira pour parcourir les colonnes d'une même ligne.
	my $i = 0;
	
	# On récupère la forme de citation : 
	my $citform = $LIGNE[$i];
	# Ca plante dans les traitements sur les chaînes de caractères si on ne force pas un codage Unicode. 
	$citform = decode('utf8', $citform);
	
	# Idée de départ : supprimer tous les espaces : principe : tout ce qui figure dans le dictionnaire doit être une entrée lexicale intégrée, 
	# pas une construction. Mais ce principe est trop rigide: ʂv˧ɖv˧ tʰv˧, former de "penser"+"sortir", a des sens lexicalisés : 
	# "comprendre", "avoir la nostalgie"... et il est utile de présenter le trisyllabe dans une entrée de dictionnaire, même si sa structure interne
	# (construction résultative) demeure claire.
	# # # if ($citform =~ m/\s/) { # S'il y a des espaces :
		# # # $citform =~ s/\s+//g;  # on les supprime
		# # # print "Espaces en trop dans la ligne $nb_ln\n";
	# # # }
	
	# Une condition : qu'il y ait une forme pour le mot. Il faut au moins une forme chez l'un des locuteurs. Il ne faut pas non plus que le contenu
	# de la forme de citation soit une simple astérisque, qui signale que le mot a été demandé mais que le locuteur n'a pas trouvé de mot correspondant autre qu'emprunt ou périphrase.
	if (($citform ne "" && $citform ne '*') || $LIGNE[15] ne "" || $LIGNE[19] ne "" || $LIGNE[23] ne "" ||  $LIGNE[24] ne "") {

		# On traite autant de colonnes qu'il en a été déclarées dans la définition de la liste @pre.
		my $a_traiter = @pre;
		# On affiche, pour la phase de test : print "Nombre d'elements: $long\n";

		# On ouvre une boucle pour traiter autant de cellules qu'il y a de valeurs dans la liste des gloses: 
		while ($i < $a_traiter)
		{
			# on récupère l'élément d'index i. Cas particulier : si c'est la forme de citation, on la reprend de $citform, après traitements déjà effectués dessus.
			if ($i == 0) {
				$cell = $citform;
			}
			else {$cell = $LIGNE[$i];
			}
			# Certaines des données ne sont pas copiées telles quelles, mais interprétées pour créer une forme. Par exemple la forme phonologique, 
			# construite d'après le ton et les segments, en colonne 2 d'Excel (donc indice 1 dans Perl). 
			# On ne la construit que si la cellule concernée contient une notation phonétique, avec des tons : si c'est une mention telle que "xxxx", 
			# qui signale qu'il faut voir avec un locuteur pour ajouter cette entrée, ça n'a pas de sens de faire des traitements sur cette chaîne.
			if (($i == 1) && ($citform =~ /"˩|˧|˥"/) )	{
				### Création de la forme sous-jacente.
				# On découpe la forme de citation selon ces caractères
				my @sylls = split /@tones/, $citform;
				# En phase de test on peut afficher : print "Les syllabes, sans tons: @sylls\n";
				# on relève le nombre de syllabes
				my $nbsyll = @sylls;
				# En phase de test on peut afficher : print "Mot de $nbsyll syllabes\n";
				# on initialise une variable undform, "underlying form", et on y ajoute les tons. Pour les tons M et LM: aucun changement nécessaire.
				my $undform = '';
				$ton = $LIGNE[1];
				# Séquence de if et elsif : avais essayé plus élégant, avec given ($ton) { when ('#H') {} } etc mais ça faisait planter l'interpréteur Perl.
				if ($ton eq '#H') {
					# Ton H flottant: différent selon qu'il s'agit d'un monosyllabe ou d'un disyllabe. 
					# Le ton #H sur disyllabe ne doit pas être confondu avec H#; on ne peut noter les deux comme syll˧syll˥
					# Solution adoptée : noter syll˧syll#˥ pour le ton #H sur disyllabe.
					if ($nbsyll == 1) {
						$undform = $sylls[$nbsyll - 1]."˥";
						# Pour monosyllabes : noter simplement par H en fin de dernière syllabe. 
						# Rappel: les indices commencent à zéro dans Perl, il faut donc soustraire 1 au nombre de syllabes.
						# on obtient la ligne entière à ajouter dans le fichier texte pour Toolbox
						$ln_out = "\\$pre[$i]\t$undform\n";
					}
					elsif ($nbsyll > 1) {
						$undform = $sylls[$nbsyll - 1]."#˥";
						# On tient le compte du nombre de syllabes de la forme sous-jacente reconstruite
						my $nbsyllunder = 1;
						while ($nbsyllunder < $nbsyll) {
							# on ajoute un ton M à toute autre syllabe. D'abord on trouve l'indice de la syll. à traiter :
							my $sylltraitee = $nbsyll - $nbsyllunder;
							# puis on l'ajoute à la forme sous-jacente. Rappel : les indices commencent à zéro dans Perl, il faut donc soustraire 1.
							$undform = $sylls[$sylltraitee - 1]."˧".$undform;
							# on incrémente le nombre de syllabes traitées
							$nbsyllunder++;
						} # fin de la boucle pour le traitement des syllabes non finales
						# on obtient la ligne entière à ajouter dans le fichier texte pour Toolbox
						$ln_out = "\\$pre[$i]\t$undform\n";
					} # fin de la condition pour les mots disyllabiques ou polysyllabiques au ton #H
				} # fin de la boucle pour le traitement du cas "ton #H"
				elsif ($ton eq 'L') {
					# Façon de procéder : on remplace toutes les marques tonales par L, puis on supprime les doublons.
					# on remplace tous les tons par L :
					$citform =~ tr /˧|˥/˩/;
					# on simplifie les séquences de ˩ : par exemple, ˧˥ est transformé en ˩˩ par la ligne qui précède; il faut le simplifier en ˩.
					$citform =~ tr///cs;
					$undform = $citform;
					# on obtient la ligne entière à ajouter dans le fichier texte pour Toolbox
					$ln_out = "\\$pre[$i]\t$undform\n";
				}
				elsif ($ton eq 'L+#H') {
					# remplacer le M final par un H
					$citform =~ tr/˧/˥/;
					$undform = $citform;
					# on obtient la ligne entière à ajouter dans le fichier texte pour Toolbox
					$ln_out = "\\$pre[$i]\t$undform\n";
				}
				elsif ($ton eq 'LML') {
					# ajouter un L final
					$undform = $citform."˩";
					$ln_out = "\\$pre[$i]\t$undform\n";
				}
				elsif ($ton eq 'H$') { 
					# remplacer le H final par H$ : on commence par récupérer la chaîne sans son dernier caractère
					$undform = substr($citform, 0, -1);
					# puis on y préfixe \u ; et on y suffixe ˥$ et une fin de ligne
					$ln_out = "\\$pre[$i]\t$undform˥\$\n";
				}
				else {
					# Dans les autres cas : on ne met rien comme forme sous-jacente puisqu'elle est identique à la forme de citation.
					$ln_out = '';
				}
			} # fin du IF portant sur le type de ton
			
			else { # Si on traite une autre colonne de données que le ton sous-jacent :
				# On met la cellule dans un fichier en sortie, précédé du préfixe demandé par Toolbox. 
				# Si la cellule est vide : on ne crée la ligne que si c'est une catégorie indispensable.
				# Il faut aussi une condition sur $i: on ne regarde plus les données après la 26e colonne, soit i == 25.
				if ($i <= 25) {
					my $target = $pre[$i];
					# On détermine si le préfixe est l'un des préfixes obligatoires. 
					my $oblig = grep /^$target$/, @pre_obl; 
					if ( ($cell ne "") or ( $oblig == 1) ) {
						# on ajoute le préfixe et une tabulation au début, et un retour chariot à la fin, créant une variable $ln_out.
						# Surprise pour moi : le compilateur demande à ce que la syntaxe soit $pre et non @pre dans l'expression qui suit.
						$ln_out = "\\$pre[$i]\t$cell\n";
					}
					else 	{ 	# sinon : ligne vide. 
						$ln_out = "";
					} # fin de la condition "existence d'une donnée ou ligne obligatoire"
				} # fin de la condition "ne pas dépasser la 26e colonne"
			} # fin du traitement appliqué aux données autres que 1e colonne
			# On écrit cette variable (contenant 1 ligne) dans le fichier en sortie. 
			print $out $ln_out;
			# on incrémente i. Rappel: les indices commencent à zéro dans Perl.
			$i++;
		}
		# On ajoute les formes alternatives des tons à la fin de l'entrée. 
		# Choix provisoire : indiquer comme seule forme alternative la forme tout au ton L, 
		# sauf dans le cas des mots pour lesquels une forme alternative est indiquée "en dur" dans le fichier en entrée, dans la colonne 31.
		# Pour les mots ayant déjà un ton L, ce n'est pas la peine d'indiquer de forme alternative.
		if ($ton ne 'L') { 
			# Formes alternatives : tout au ton L, suite à l'arasement des tons H. On commence par mettre la forme de citation
			# dans la variable $alternatives, précédée du préfixe demandé par Toolbox: \a  (sauf bien sûr si cette forme de citation ne contient pas de tons, auquel cas c'est juste une note du type "à voir" ou "xxxx" et pas une entrée lexicale.
			if ($citform =~ /"˩|˧|˥|"/)  {
				$alternatives = "\\a $citform\n";
			}
			else {
				$alternatives = "\\a \n";
			}
			# on remplace tous les tons par L :
			$alternatives =~ tr /˧|˥/˩/;
			# on simplifie les séquences de ˩ : par exemple, ˧˥ est transformé en ˩˩ par la ligne qui précède; il faut le simplifier en ˩.
			$alternatives =~ tr///cs;
			print $out $alternatives;
		}
		# Ici : pas de ELSE : dans le cas où le ton est L, aucun traitement à apporter.

		# On sépare les entrées successives du dictionnaire par une ligne vide, \n
		print $out "\n";
	# Fin de la condition sur la ligne non vide
	}
	else { # Si la ligne est vide : on en garde trace en conservant son numéro dans une chaîne.
		$vides = "$vides $nb_ln";
	}
} # On ferme la boucle des lignes (WHILE)

# On signale à l'utilisateur les lignes vides
print "Ligne vides trouvees :".$vides."."."\n";
print $nb_ln." lignes traitées.\n";

# fermeture des fichiers (handles)
close $in;
close $out;