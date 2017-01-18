#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Script pour passer de lx à lc pour le dictionnaire na.
### Ecrit par Benjamin Galliot en janvier 2017.
### Script repris à zéro faute de parvenir à faire tourner le script préalablement réalisé par C. Buret (2014).
## # Ce script prend en entrée Dictionary.txt et y ajoute un champ \lc pour chaque entrée.

import regex
import os
import time

## Quelques exemples pour les tests
# exemple = 'lo˧ʂv˩', 'MH', 'n'
# exemple = 'lo˧ʂv˩-ʂv˩ʂv˩', 'MH-MH', 'n'
exemple = ' ta˧ta˧-ta˧', ' LM-M ', 'v'


# correspondance_des_tons = {"L": "˩", "M": "˧", "H": "˥"}  # Dictionnaire de correspondances des tons.


def créer_le_dictionnaire_avec_les_lc(chemin_entrée, chemin_sortie):
    with open(chemin_entrée, 'r') as entrée, open(chemin_sortie, 'w') as sortie:
        expression = regex.compile(r"\\np <type=\"tone\"> ([\w̃|#$+-]+)")
        lexème = None
        information_tonale = None
        classe_grammaticale = None
        for index, line in enumerate(entrée.readlines()):
            ##  On recopie la ligne lue telle quelle, de toute façon
            sortie.write(line)
            correspondance = expression.match(line)
            ## Si on tombe sur un lx : on commence une collection de l'ensemble des 3 infos nécessaires pour créer le lc : forme sous-jacente ; ton ; et partie du discours (classe syntaxique : nature du mot).
            if line.startswith('\\lx'):
                ##  On exclut le marqueur pour ne garder que le contenu
                lexème = ' '.join(line.split()[1:])
            elif correspondance:
                ## On note le ton sous-jacent indiqué dans le champ correspondant : note phonologique (np) marquée comme <type = "tone">.
                information_tonale = correspondance.group(1)
            elif line.startswith('\\ps'):
                ##  On note la partie du discours
                classe_grammaticale = line.split()[-1]
            ## Une fois qu'on a sous la main tout le nécessaire :
            if lexème and information_tonale and classe_grammaticale:
                ## affichage à l'écran
                # print("paramètres :", index, lexème, information_tonale, classe_grammaticale)
                ##  on appelle la fonction essentielle qui génère le lc à partir du triplet d'infos
                résultat_de_la_génération = générer_un_lc(lexème, information_tonale, classe_grammaticale)
                sortie.write("\\lc {}\n".format(résultat_de_la_génération))
                ## on ré-initialise les variables
                lexème = None
                information_tonale = None
                classe_grammaticale = None


def générer_un_lc(lexème, information_tonale, classe_grammaticale):
    ######  Fonction centrale.
    # Initialisation de la variable contenant le résultat
    résultat = None
    groupes_tonals = [groupe_tonal.strip().strip('-') for groupe_tonal in lexème.split(
        "|")]  # On sépare par le caractère |, puis on vire les espaces superflus, puis on vire les - en bordure.
    tons_de_groupe = [ton_de_groupe.strip().replace("L", "˩").replace("M", "˧").replace("H", "˥").replace('abcd', '')
                      for ton_de_groupe in information_tonale.split(
            "|")]  # On sépare par le caractère | puis on vire les espaces superflus et les lettres des sous-catégories tonales de verbes, adjectifs, classificateurs...: les a, b, c etc.
    ##  Condition : a-t-on autant de tons que de groupes tonals indiqués? Par exemple pour l'expression \lx lo˧ʂv˩ | -hi˩-nɑ˧mi˧, comme elle contient deux groupes tonals séparés par | il faut deux tons séparés par un même symbole | dans le champ 'ton': \np <type="tone"> L# | L-. Dans ce cas-ci tout est bon.
    if len(groupes_tonals) == len(tons_de_groupe):
        # affichage à l'écran
        # print("groupes_tonals", groupes_tonals)
        # print("tons_de_groupe", tons_de_groupe)
        résultat = []
        for groupe_tonal, ton_de_groupe in zip(groupes_tonals, tons_de_groupe):  # On parcourt en parallèle les 2 listes : celle des groupes tonals et celle de leurs tons phonologiques.
            # print("groupe_tonal", groupe_tonal)
            # print("ton_de_groupe", ton_de_groupe)
            # Une condition : qu'il y ait au moins une marque tonale dans l'expression qui désigne le ton de groupe. Sinon, on ne sait pas comment affecter les tons et une erreur est renvoyée (cf fin de la condition ouverte ici).
            if any([ton in ton_de_groupe for ton in ["˩", "˧", "˥"]]):
                morphèmes = groupe_tonal.split("-")
                tons_des_morphèmes = ton_de_groupe.split("-")
                # Même chose au niveau des morphèmes (re-décomposant d'après les traits d'union) : il faut un ton par morphème. Ou, plus exactement, il faut une indication de division du schème tonal en fonction de la division en morphèmes : si le groupe tonal comprend 2 morphèmes, une indication telle que L- est suffisante pour assigner les tons à 2 morphèmes (L avant la frontière qui sépare ces 2 morphèmes; et par défaut, M après), tandis qu'un simple 'L' ne suffirait pas (on ne sait pas s'il faut l'affecter au 1er morphème ou au 2e).
                if len(morphèmes) == len(tons_des_morphèmes):
                    ton_haut = False  # Règle spéciale du ton haut : un ton haut est toujours suivi de tons bas, jusqu'à la fin du groupe tonal. Au début cette variable binaire est à 'Faux'. Dès lors qu'un ton Haut est associé à une syllabe, elle passe à 'Vrai'.
                    ton_flottant = False  # Variable binaire pour le ton flottant : il ne se fixe pas au morphème qui en est porteur, mais il faut le garder en mémoire pour l'associer à la 1e syllabe du morphème qui suit, s'il y en a un. Pour cela, au début cette variable binaire est à 'Faux'. Dès lors qu'un ton Haut flottant est rencontré, elle passe à 'Vrai'.
                    # On arrive au niveau du morphème.
                    for morphème, ton_de_morphème in zip(morphèmes, tons_des_morphèmes):
                        train_de_syllabes, train_de_tons = analyser_le_morphème(morphème)
                        if not train_de_tons:
                            return résultat
                        for lettre_ton in ["a", "b", "c", "d"]:
                            ton_de_morphème = ton_de_morphème.replace(lettre_ton, '')
                        # print('décomposition :', train_de_syllabes, train_de_tons, ton_de_morphème)
                        # On applique le ton phonologique en utlisant les règles d'association des différents tons lexicaux. La condition est qu'il n'y ait ni ton H flottant, ni ton H associé à une précédente syllabe à l'intérieur du groupe tonal, faute de quoi ce ton H conditionne toute la suite.
                        if not ton_haut and not ton_flottant:
                            if ton_de_morphème == "˧":  # cas du ton M
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes])
                            elif ton_de_morphème.startswith("˧˥"):  # # cas du ton MH. Inclut MH et MH#...
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[0:-1]])
                                résultat.append(train_de_syllabes[-1] + "˧˥")
                            elif ton_de_morphème == "#˥":  # cas du ton H flottant
                                ton_flottant = True
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes])
                            elif ton_de_morphème in ["˥$", "˥#"]:  # cas des tons H final de mot et 'glissant', notés H$ et H#. En isolation, rien ne les distingue.
                                ton_haut = True
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[0:-1]])
                                résultat.append(train_de_syllabes[-1] + "˥")
                            elif ton_de_morphème == "˩":  # cas du ton bas (L)
                                if classe_grammaticale == "n" and len(train_de_syllabes) == 1:
                                    résultat.append(train_de_syllabes[0] + "˧")  # Traitement particulier du nom monosyllabique au ton L : en isolation, il paraît avec un ton M.
                                else:
                                    résultat.extend([syllabe + "˩" for syllabe in train_de_syllabes])
                            elif ton_de_morphème == "˩#":  # cas du ton bas final (L#)
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[0:-1]])
                                résultat.append(train_de_syllabes[-1] + "˩")
                            elif ton_de_morphème == "˩˧+˧˥#":  # cas du ton LM +MH#
                                résultat.append(train_de_syllabes[0] + "˩")
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[1:-1]])
                                résultat.append(train_de_syllabes[-1] + "˧˥")
                            elif ton_de_morphème == "˩˧+˥#":  # cas du ton LM +H#
                                résultat.append(train_de_syllabes[0] + "˩")
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[1:-1]])
                                résultat.append(train_de_syllabes[-1] + "˥")
                            elif ton_de_morphème == "˩˧+#˥":  # cas du ton LM +#H
                                ton_flottant = True
                                résultat.append(train_de_syllabes[0] + "˩")
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[1:]])
                            elif ton_de_morphème == "˩˧":  # cas du ton LM
                                if len(train_de_syllabes) == 1:
                                    résultat.append(train_de_syllabes[0] + "˩˥")
                                else:
                                    résultat.append(train_de_syllabes[0] + "˩")
                                    résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes[1:]])
                            elif ton_de_morphème == "˩+˥#":
                                résultat.extend([syllabe + "˩" for syllabe in train_de_syllabes[0:-1]])
                                résultat.append(train_de_syllabes[-1] + "˥")
                            elif ton_de_morphème == "˩˥":  # Cas du ton LH. Pour les monosyllabes, on met les 2 niveaux tonals L et H sur la première syllabe (et seule) du train. Sinon : L sur premières syll., H sur dernière.
                                if len(train_de_syllabes) == 1:
                                    résultat.append(train_de_syllabes[0] + "˩˥")
                                else:
                                    résultat.extend([syllabe + "˩" for syllabe in train_de_syllabes[0:-1]])  # ajouté par Alexis le soir du 10 janvier. Attention les dégâts :-) Idée : L sur toutes les syllabes, sauf la dernière qui reçoit un H.
                                    résultat.append(train_de_syllabes[-1] + "˥")
                            elif ton_de_morphème == "˥":  # Ton H : n'existe (tel quel) que pour les monosyllabes. On neutralise en ton moyen sur la première syllabe.
                                print("**", ton_de_morphème)
                                résultat.append(train_de_syllabes[0] + "˧")
                            # S'il n'y a pas de ton indiqué : on assigne M par défaut.
                            elif not ton_de_morphème:
                                résultat.extend([syllabe + "˧" for syllabe in train_de_syllabes])
                            else:
                                return "xxxx ton non trouvé, à faire manuellement..."
                        elif ton_flottant:  # Ton flottant : on met un H en 1e syllabe et tout le reste est rabaissé en L
                            résultat.append(train_de_syllabes[0] + "˥")
                            résultat.extend([syllabe + "˩" for syllabe in train_de_syllabes[1:]])
                        elif ton_haut:  # Ton H déjà associé à un morphème précédent, dans le même groupe tonal : tout est rabaissé en L
                            résultat.extend([syllabe + "˩" for syllabe in train_de_syllabes])
                        résultat = ["".join(résultat)]
                    résultat = ["-".join(résultat)]
                    # Ajustement sur des groupes tonals entiers. Si le groupe ne contient que des L, s'y ajoute un H final (post-lexical).
                    if all([ton not in résultat[-1] for ton in ["˧", "˥"]]):
                        résultat[-1] += "˥"
                    # Aussi : neutralisation finale des M et H en H, si précédé uniquement de M. Une fonction spécifique a été réalisée pour cet ajustement.
                    print("x++++>", résultat)
                    résultat[-1] = neutralisation_finale(résultat[-1])
                else:
                    return "xxxx non-correspondance entre le nombre de morphèmes et le nombre de tons de morphèmes"
            else:
                return "xxxx groupe tonal entier sans aucun ton"
        résultat = "|".join(résultat)
    else:
        return "xxxx non-correspondance entre le nombre de groupes tonals et le nombre de tons"
    print("x------->", résultat)
    return résultat


def analyser_le_morphème(morphème):
    expression_non_tonalisée = regex.compile("[˩˧˥]+")
    correspondance_non_tonalisée = expression_non_tonalisée.findall(morphème)
    print("--", morphème, correspondance_non_tonalisée)
    if not correspondance_non_tonalisée:
        syllabes = morphème
        tons = None
    else:
        expression_tonalisée = regex.compile("([\w]+)([˩˧˥#$]+)")  # Groupe 1 : syllabe ; groupe 2 : ton ; groupe 3 : sous-catégorie tonale. Dernier opérateur non gourmand pour éviter que la sous-catégorie tonale soit considérée comme le début d'une nouvelle syllabe.
        correspondance_tonalisée = expression_tonalisée.findall(morphème)
        print("++", correspondance_tonalisée)
        syllabes = [syllabe_tonalisée[0] for syllabe_tonalisée in correspondance_tonalisée]
        tons = [syllabe_tonalisée[1] for syllabe_tonalisée in correspondance_tonalisée]
    return syllabes, tons

def neutralisation_finale(groupe_tonal):
    résultat = groupe_tonal
    tons = [caractère for caractère in groupe_tonal if caractère in ["˩", "˧", "˥"]]
    # print('****', tons)
    if tons[-1] == "˧" and all([ton not in tons[0:-1] for ton in ["˧", "˥"]]) and "˩" in tons[0:-1]:
        résultat = groupe_tonal[0:-1] + "˥"
    print("*******************************************", groupe_tonal, tons, résultat, [ton not in tons[0:-1] for ton in ["˧", "˥"]])
    return résultat

# Exécution du script s'il n'est pas appelé comme un module.
if __name__ == '__main__':
    fichier_entrée = "../Dictionary.txt"
    fichier_sortie = "../Dictionnaire avec lc.txt"

    chemin_entrée = os.path.join(os.getcwd(), fichier_entrée)
    chemin_sortie = os.path.join(os.getcwd(), fichier_sortie)
    créer_le_dictionnaire_avec_les_lc(chemin_entrée, chemin_sortie)

    # a = "ʐv̩˧-adzi˩˩"
    # expression = re.compile("(.+)([˩˧˥#$]*)([abcd]?)")
    # print(expression.findall(a))


# \lx lo˧ʂv˩ | -hi˩-nɑ˧mi˧ \np <type="tone"> L# | L-
