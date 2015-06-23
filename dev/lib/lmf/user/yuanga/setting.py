#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import ps_partOfSpeech, mdf_lmf, set_bw
from common.range import partOfSpeech_range
from config.tex import partOfSpeech_tex
from utils.io import EOL, ENCODING
from common.defs import VERNACULAR, NATIONAL, ENGLISH, REGIONAL
from utils.error_handling import Warning

## To define languages and fonts
import config
FRENCH = "French"

## Semantic domains
order = [
    ("TITLE 1", "1. le corps humain"),
    [
        ("corps", "1.1. anatomie"),
        ("fonct.nat", "1.2. fonctions naturelles"),
        ("TITLE 2", "1.3. santé, maladie, médecine"),
        [
            ("santé", "1.3.1. santé, maladie"),
            ("médecine", "1.3.2. remèdes, médecine")
        ],
        ("TITLE 2", "1.4. vêtements, parure, soins du corps"),
        [
            ("habillement", "1.4.1. vêtements, parure"),
            ("soins", "1.4.2. soins du corps")
        ],
        ("TITLE 2", "1.5. positions, déplacements, mouvements, actions"),
        [
            ("position", "1.5.1. préfixes verbaux de position"),
            ("mouvement", "1.5.2. préfixes verbaux de mouvement"),
            ("déplacement", "1.5.3. déplacements, mouvements avec les pieds"),
            ("portage", "1.5.4. portage"),
            ("action tête", "1.5.5. mouvements ou actions avec la tête, les yeux, la bouche"),
            ("action corps", "1.5.6. mouvements de bras, de mains"),
            ("action", "1.5.7. verbes d'action (en général)"),
            ("manière", "1.5.8. postverbes de manière")
        ]
    ],
    ("TITLE 1", "2. techniques"),
    [
        ("TITLE 2", "2.1. habitat"),
        [
            ("habitat", "2.1.1. habitat"),
            ("maison", "2.1.2. types de maison, architecture de la maison")
        ],
        ("TITLE 2", "2.2. cultures plantations récoltes"),
        [
            ("cultures", "2.2.1. cultures"),
            ("champs", "2.2.2. types de champs")
        ],
        ("TITLE 2", "2.3. chasse guerre"),
        [
            ("armes", "2.3.1. armes"),
            ("chasse", "2.3.2. chasse"),
            ("guerre", "2.3.3. guerre")
        ],
        ("pêche", "2.4. pêche"),
        ("navigation", "2.5. navigation"),
        ("feu", "2.6. feu"),
        ("TITLE 2", "2.7. cuisine alimentation"),
        [
            ("ustensiles", "2.7.1. ustensiles"),
            ("prép.aliments", "2.7.2. préparation des aliments"),
            ("cuisson", "2.7.3. modes de cuisson"),
            ("alimentation", "2.7.4. alimentation")
        ],
        ("TITLE 2", "2.8. tressage (nattes paniers) cordes noeuds paquets"),
        [
            ("tressage", "2.8.1. tressage"),
            ("nattes", "2.8.2. nattes"),
            ("paniers", "2.8.3. paniers"),
            ("cordes", "2.8.4. cordes"),
            ("couture", "2.8.5. couture"),
            ("paquet", "2.8.6. paquetages")
        ],
        ("TITLE 2", "2.9. travail du bois forme et consistance des objets"),
        [
            ("outils", "2.9.1. outils, matériaux"),
            ("travail bois", "2.9.2. travail bois"),
            ("carac.objet", "2.9.3. description des objets, formes, consistance")
        ]
    ],
    ("TITLE 1", "3. individu - société"),
    [
        ("étapes vie", "3.1. cours de la vie"),
        ("TITLE 2", "3.2. fonctions intellectuelles, sentiments"),
        [
            ("fonct.intellectuelles", "3.2.1. fonctions intellectuelles"),
            ("sentiments", "3.2.2. sentiments")
        ],
        ("TITLE 2", "3.3. parenté alliance"),
        [
            ("parenté", "3.3.1. parenté"),
            ("appellation parenté", "3.3.2. appellation parenté"),
            ("désignation parenté", "3.3.3. désignation parenté"),
            ("alliance", "3.3.4. alliance"),
            ("couple parenté", "3.3.5. couple parenté")
        ],
        ("TITLE 2", "3.4. organisation sociale richesses dons échanges"),
        [
            ("société", "3.4.1. organisation sociale"),
            ("richesse", "3.4.2. richesses, monnaies traditionnelles"),
            ("échanges", "3.4.3. dons, échanges, achat et vente, vol")
        ],
        ("religion", "3.5. religion"),
        ("TITLE 2", "3.6. fêtes danse chant jeux"),
        [
            ("fête", "3.6.1. fêtes"),
            ("jeux", "3.6.2. jeux divers")
        ],
        ("TITLE 2", "3.7. traditions orales relations inter-individuelles"),
        [
            ("oralité", "3.7.1. tradition orale"),
            ("discours", "3.7.2. échanges verbaux"),
            ("exclamations", "3.7.3. exclamations"),
            ("interaction", "3.7.4. relations"),
        ]
    ],
    ("TITLE 1", "4. nature"),
    [
        ("TITLE 2", "4.1. ciel"),
        [
            ("astres", "4.1.1. astres"),
            ("temps", "4.1.2. découpage du temps"),
            ("vent", "4.1.3. vent"),
            ("climat", "4.1.4. phénomènes atmosphériques"),
            ("couleurs", "4.1.5. couleurs")
        ],
        ("TITLE 2", "4.2. terre"),
        [
            ("terrain", "4.2.1. les terrains et leur constitution"),
            ("topographie", "4.2.2. topographie"),
            ("orientation", "4.2.3. orientation")
        ],
        ("eau", "4.3. eau (eau douce mer)")
    ],
    ("TITLE 1", "5. zoologie"),
    [
        ("oiseaux", "5.1. oiseaux"),
        ("TITLE 2", "5.2. mammifères"),
        [
            ("mammifères", "5.2.1. mammifères"),
            ("mammifères marins", "5.2.2. mammifères marins")
        ],
        ("TITLE 2", "5.3. reptiles"),
        [
            ("reptiles", "5.3.1. reptiles"),
            ("reptiles marins", "5.3.2. reptiles marins")
        ],
        ("crustacés", "5.4. crustacés"),
        ("échinodermes", "5.5. échinodermes"),
        ("insectes", "5.6. insectes"),
        ("mollusques", "5.7. mollusques"),
        ("poissons", "5.8. poissons"),
    ],
    ("TITLE 1", "6. botanique"),
    [
        ("arbre", "6.1. arbre"),
        ("plantes", "6.2. description des végétaux"),
        ("cocotier", "6.3. cocotier"),
        ("ignames", "6.4. ignames"),
        ("taros", "6.5. taros"),
        ("patates douces", "6.6. patates douces"),
        ("canne à sucre", "6.7. canne à sucre"),
        ("bananiers", "6.8. bananiers"),
        ("manioc", "6.9. manioc")
    ],
    ("classificateur", "7. classificateur"),
    ("quantificateur", "8. quantificateur")
]

def read_order(order, sd_order, rank, sd_list):
    for element in order:
        if type(element) is not list:
            sd = element[0]
            if not sd.startswith("TITLE"):
                rank += 1
                sd_order.update({sd.decode(ENCODING) : rank})
            sd_list.append(element)
        else:
            (sd_order, rank, sd_list) = read_order(element, sd_order, rank, sd_list)
    return (sd_order, rank, sd_list)

sd_order = dict()
rank = 0
sd_list = list()
(sd_order, rank, sd_list) = read_order(order, sd_order, rank, sd_list)
sd_order.update({"-" : rank + 1})

def compare_sd(x, y):
    """Compare 2 semantic domains between each other.
    """
    try:
        # Both equal => do nothing
        if sd_order[x] == sd_order[y]:
            return 0
        # If the 1st one is lower than the 2nd one, its rank is decremented
        if sd_order[x] < sd_order[y]:
            return -1
        # If the 1st one is greater than the 2nd one, its rank is incremented
        elif sd_order[x] > sd_order[y]:
            return 1
    except KeyError:
        print Warning("Cannot compare " + x.encode(ENCODING) + " and " + y.encode(ENCODING))
        return -1

sd_errors = set()
def get_is(lexical_entry):
    for sd in lexical_entry.get_semantic_domains():
        # Consider only the first semantic domain
        if sd in sd_order.keys():
            return sd
        sd_errors.add(sd)
    return "-"
items=lambda lexical_entry: get_is(lexical_entry)

def get_gf(lexical_entry):
    for sense in lexical_entry.get_senses():
        for gloss in sense.find_glosses(language=config.xml.French):
            return gloss
    return "-"
reverse_items=lambda lexical_entry: get_gf(lexical_entry)

## Functions to process some MDF fields (input)
def retrieve_dialect_name(text):
    text = text.replace("BO", u"Bondé")
    text = text.replace("PA", "Paimboa")
    text = text.replace("GO(s)", "Gomen Sud")
    text = text.replace("GO(n)", "Gomen Nord")
    text = text.replace("GO", "Gomen")
    text = text.replace("WEM", "WEM")
    text = text.replace("WE", "WE")
    return text

mdf_lmf.update({
    "dialx" : lambda dialx, lexical_entry: lexical_entry.set_usage_note(retrieve_dialect_name(dialx), language="nua"),
    "empr"  : lambda empr, lexical_entry: set_bw(empr, lexical_entry)
})

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps_partOfSpeech.update({
    "ACC"                                                                                           : "XXX",

    "adresse honorifique"                                                                           : "XXX",

    "AGT"                                                                                           : "XXX",
    "AGT ???"                                                                                       : "XXX",

    "ART PL"                                                                                        : "XXX",

    "ADV LOC (spatio-temporel) ANAPH ???"                                                           : "XXX",
    "ADV LOC DX2"                                                                                   : "XXX",
    "ADV LOC"                                                                                       : "XXX",
    "ADV QNT"                                                                                       : "XXX",
    "ADV MODIF"                                                                                     : "XXX",
    "ADV ATTEN (ordre) (forme de politesse) ; ponctuel"                                             : "XXX",
    "ADV TIME"                                                                                      : "XXX",
    "ADV SEQ (continuatif)"                                                                         : "XXX",
    "ADV ???"                                                                                       : "XXX",

    "ANAPH"                                                                                         : "XXX",
    "ANAPH (discours ou passé ???)"                                                                 : "XXX",
    "ANAPH (discours)"                                                                              : "XXX",

    "ASSOC"                                                                                         : "XXX",

    "ASP DUR"                                                                                       : "XXX",
    "ASP ou RESTR"                                                                                  : "XXX",
    "ASP PERS"                                                                                      : "XXX",
    "ASP (itératif)"                                                                                : "XXX",
    "ASP (révolu)"                                                                                  : "XXX",
    "ASP HAB"                                                                                       : "XXX",
    "ASP ACC"                                                                                       : "XXX",
    "ASP INACC"                                                                                     : "XXX",
    "ASP (post-verbal)"                                                                             : "XXX",

    "atténuatif ???"                                                                                : "XXX",

    "BENEF"                                                                                         : "XXX",

    "c"                                                                                             : "XXX",

    "CLF"                                                                                           : "XXX",
    "CLF NUM (morceaux) PA [pas à Gomen]"                                                           : "XXX",
    "CLF (multiples)"                                                                               : "XXX",
    "CLF (armes)"                                                                                   : "XXX",
    "CLF (objets ronds)"                                                                            : "XXX",
    "CLF (maisons)"                                                                                 : "XXX",
    "CLF NUM (animés)"                                                                              : "XXX",
    "CLF NUM"                                                                                       : "XXX",
    "CLF NUM (morceaux de bois)"                                                                    : "XXX",
    "CLF NUM (feuilles)"                                                                            : "XXX",
    "CLF NUM (tissus et étoffes végétales)"                                                         : "XXX",
    "CLF NUM (lots : fête de la nouvelle igname, contexte cérémoniel)"                              : "XXX",
    "CLF NUM (lots cérémoniels)"                                                                    : "XXX",
    "CLF NUM (pour compter des paquets d'ignames constitués de trois ignames)"                      : "XXX",
    "CLF NUM (générique et des objets ronds)"                                                       : "XXX",
    "CLF NUM (objets longs)"                                                                        : "XXX",
    "CLF NUM (bois, arbres, certaines racines comestibles, cordes, objets longs, sagaies, doigts)"  : "XXX",

    "CLF POSS"                                                                                      : "XXX",

    "CNJ ; THEM"                                                                                    : "XXX",
    "CNJ TIME"                                                                                      : "XXX",
    "CNJ (complémentation)"                                                                         : "XXX",
    "CNJ HYP"                                                                                       : "XXX",
    "CNJ (but)"                                                                                     : "XXX",
    "CNJ REL"                                                                                       : "XXX",

    "COI"                                                                                           : "XXX",

    "COLL"                                                                                          : "XXX",
    "COLL + PRO"                                                                                    : "XXX",

    "CONN"                                                                                          : "XXX",

    "contraste"                                                                                     : "XXX",
    "contraste ; état"                                                                              : "XXX",

    "COORD"                                                                                         : "XXX",

    "couple PAR"                                                                                    : "XXX",

    "DEIC DIR"                                                                                      : "XXX",
    "DEIC DX3"                                                                                      : "XXX",
    "DEIC PL DX1 ou ANAPH"                                                                          : "XXX",
    "DEIC PL"                                                                                       : "XXX",
    "DEIC DX1 duel ou ANAPH"                                                                        : "XXX",
    "DEIC DX3 duel (latéralement)"                                                                  : "XXX",
    "DEIC DX3 (visible)"                                                                            : "XXX",

    "DEM duel"                                                                                      : "XXX",
    "DEM duel ou PL"                                                                                : "XXX",
    "DEM DX"                                                                                        : "XXX",
    "DEM ANAPH"                                                                                     : "XXX",
    "DEM DX2"                                                                                       : "XXX",
    "DEM DX1"                                                                                       : "XXX",
    "DEM DX3"                                                                                       : "XXX",
    "DEM SG"                                                                                        : "XXX",
    "DEM (médial ou proche)"                                                                        : "XXX",
    "DEM PL"                                                                                        : "XXX",
    "DEM PL (post-nom)"                                                                             : "XXX",
    "DEM duel (post-nom)"                                                                           : "XXX",
    "DEM DIR"                                                                                       : "XXX",
    "DEM DX2 duel et ANAPH"                                                                         : "XXX",
    "DEM DX2 ; ANAPH ; assertif"                                                                    : "XXX",
    "DEM DX3 PL"                                                                                    : "XXX",
    "DEM DX3 ou ANAPH"                                                                              : "XXX",
    "DEM DX3 duel"                                                                                  : "XXX",
    "DEM DX3 DEIC ou ANAPH"                                                                         : "XXX",
    "DEM DX3 (distal)"                                                                              : "XXX",
    "DEM DX4"                                                                                       : "XXX",

    "déterminant ; DEM duel"                                                                        : "XXX",
    "déterminant duel"                                                                              : "XXX",
    "déterminant ; PRO DEIC DX1"                                                                    : "XXX",

    "DIR (transverse)"                                                                              : "XXX",
    "DIR (ventif)"                                                                                  : "XXX",
    "DIR (centrifuge)"                                                                              : "XXX",

    "dire du mal de qqn"                                                                            : "XXX",

    "dispersif ; DISTR"                                                                             : "XXX",

    "DISTR"                                                                                         : "XXX",

    "doute"                                                                                         : "XXX",

    "duel"                                                                                          : "XXX",

    "DUR"                                                                                           : "XXX",

    "DX1"                                                                                           : "XXX",
    "DX1 ; ANAPH"                                                                                   : "XXX",
    "DX2 ; ANAPH ; ASS"                                                                             : "XXX",

    "FOC ; RESTR (antéposé au GN) (za ... nye ...)"                                                 : "XXX",

    "forme déterminée de mwa ; PREF (désignant un contenant)"                                       : "XXX",

    "FREQ"                                                                                          : "XXX",

    "FUT"                                                                                           : "XXX",

    "génitif (déterminant non-spécifique, générique ???)"                                           : "XXX",

    "INCH"                                                                                          : "XXX",
    "INCH, en cours"                                                                                : "XXX",

    "indétermination"                                                                               : "XXX",

    "INJONC"                                                                                        : "XXX",

    "INT LOC (dynamique)"                                                                           : "XXX",
    "INT LOC (statique)"                                                                            : "XXX",
    "INT (statique : humains, PRO, n)"                                                              : "XXX",
    "INT (statique)"                                                                                : "XXX",
    "INT (indéfini)"                                                                                : "XXX",
    "INT CMPAR"                                                                                     : "XXX",

    "INTENS"                                                                                        : "XXX",
    "INTENS ; assertif (devant le prédicat)"                                                        : "XXX",

    "interlocative"                                                                                 : "XXX",

    "interpellation"                                                                                : "XXX",
    "interpellation ou DEM"                                                                         : "XXX",

    "INTJ (pitié, affection)"                                                                       : "XXX",
    "INTJ ; v"                                                                                      : "XXX",
    "INTJ ; appel respectueux à une pers."                                                          : "XXX",

    "ITER"                                                                                          : "XXX",

    "LOC DIR"                                                                                       : "XXX",
    "LOC DX2"                                                                                       : "XXX",
    "LOC DX3"                                                                                       : "XXX",
    "LOC ANAPH"                                                                                     : "XXX",
    "LOC DEIC DX3"                                                                                  : "XXX",
    "LOC ; n"                                                                                       : "XXX",
    "LOC (spatio-temporel)"                                                                         : "XXX",
    "LOC CMPAR"                                                                                     : "XXX",
    "pré-LOC + LOC"                                                                                 : "XXX",

    "LOCUT"                                                                                         : "XXX",
    "LOCUT ADV"                                                                                     : "XXX",
    "LOCUT INT"                                                                                     : "XXX",

    "MDL n"                                                                                         : "XXX",
    "MDL INTJ"                                                                                      : "XXX",

    "MODIF"                                                                                         : "XXX",

    "morphème de THEM (nrowö ... ca)"                                                               : "XXX",

    "n-fois"                                                                                        : "XXX",

    "n (inaliénable)"                                                                               : "XXX",
    "n ; CLF POSS"                                                                                  : "XXX",
    "n ; PAR REC"                                                                                   : "XXX",
    "n (composition)"                                                                               : "XXX",
    "n LOC"                                                                                         : "XXX",
    "n BENEF"                                                                                       : "XXX",
    "n ORD"                                                                                         : "XXX",
    "n ; v"                                                                                         : "XXX",
    "n ; v STAT"                                                                                    : "XXX",
    "n ; LOC"                                                                                       : "XXX",
    "n (référence)"                                                                                 : "XXX",
    "n SG"                                                                                          : "XXX",
    "n ; CLF NUM"                                                                                   : "XXX",
    "n QNT"                                                                                         : "XXX",
    "n CNJ"                                                                                         : "XXX",
    "n ; PRO"                                                                                       : "XXX",
    "n LOC (forme POSS de pwamwa)"                                                                  : "XXX",
    "n LOC ; v"                                                                                     : "XXX",
    "n CMPAR"                                                                                       : "XXX",
    "n (terme d'appellation ou référence)"                                                          : "XXX",
    "n INTJ"                                                                                        : "XXX",

    "NEG (en réponse à une question)"                                                               : "XXX",

    "NUM (animés)"                                                                                  : "XXX",
    "NUM ORD"                                                                                       : "XXX",
    "NUM (pour certains types de dons coutumiers)"                                                  : "XXX",
    "NUM (pour certains types de dons coutumiers qui se comptent par deux)"                         : "XXX",
    "NUM (pour certains types de dons coutumiers qui se comptent par deux) Bretteville"             : "XXX",

    "objet"                                                                                         : "XXX",

    "ORD"                                                                                           : "XXX",

    "PAR REC ???"                                                                                   : "XXX",
    "PAR REC"                                                                                       : "XXX",

    "passé"                                                                                         : "XXX",

    "POSS (certains lexèmes)"                                                                       : "XXX",
    "POSS IND"                                                                                      : "XXX",
    "POSS 1° pers. duel incl."                                                                      : "XXX",
    "POSS 1° pers. incl."                                                                           : "XXX",

    "PRED NEG"                                                                                      : "XXX",
    "PRED NEG (humain)"                                                                             : "XXX",

    "PREF"                                                                                          : "XXX",
    "PREF (n agent)"                                                                                : "XXX",
    "PREF (référant à une surface extérieure)"                                                      : "XXX",
    "PREF (instrumental, NOMR)"                                                                     : "XXX",
    "PREF ORD"                                                                                      : "XXX",
    "PREF CLF NUM (mains de banane)"                                                                : "XXX",
    "PREF (couples PAR)"                                                                            : "XXX",
    "PREF (relations duelles)"                                                                      : "XXX",
    "PREF (indiquant une position couchée)"                                                         : "XXX",
    "PREF NOMR"                                                                                     : "XXX",
    "PREF (lieu)"                                                                                   : "XXX",
    "PREF CAUS"                                                                                     : "XXX",
    "PREF REC ; COLL"                                                                               : "XXX",
    "PREF (position assise)"                                                                        : "XXX",

    "PREP (objet indirect)"                                                                         : "XXX",
    "PREP ; ADV ; CNJ"                                                                              : "XXX",
    "PREP LOC"                                                                                      : "XXX",
    "PREP (ablatif)"                                                                                : "XXX",
    "PREP (spatio-temporelle)"                                                                      : "XXX",
    "PREP BENEF"                                                                                    : "XXX",
    "PREP (instrumentale) ; AGT ???"                                                                : "XXX",
    "PREP (régime indirect)"                                                                        : "XXX",
    "PREP ; CNJ"                                                                                    : "XXX",
    "PREP (instrument)"                                                                             : "XXX",

    "PRO 1° pers. incl. (OBJ ou POSS)"                                                              : "XXX",
    "PRO 1° pers. excl. PL (sujet)"                                                                 : "XXX",
    "PRO 1° pers. excl. PL (OBJ ou POSS)"                                                           : "XXX",
    "PRO (OBJ) ou POSS 1° pers. triel incl."                                                        : "XXX",
    "PRO 1° pers. SG (sujet ou OBJ)"                                                                : "XXX",
    "PRO (OBJ) ou POSS 1° pers. SG"                                                                 : "XXX",
    "PRO 1° pers. incl. PL (sujet)"                                                                 : "XXX",
    "PRO 1° pers. triel incl. (sujet)"                                                              : "XXX",
    "PRO 1° pers. duel incl. (sujet)"                                                               : "XXX",
    "PRO 1° pers. triel excl. (sujet, OBJ ou POSS)"                                                 : "XXX",
    "PRO 1° pers. duel excl. (sujet, OBJ ou POSS)"                                                  : "XXX",
    "PRO 1° pers. duel excl. (OBJ ou POSS)"                                                         : "XXX",
    "PRO (OBJ) ou POSS 1° pers. duel incl."                                                         : "XXX",
    "PRO 1° pers. incl. PL"                                                                         : "XXX",
    "PRO 1° pers. incl. PL (OBJ ou POSS)"                                                           : "XXX",
    "PRO 1° pers. duel incl. (OBJ ou POSS)"                                                         : "XXX",
    "PRO 1° pers. SG (OBJ ou POSS)"                                                                 : "XXX",
    "PRO 1° pers. triel incl. (OBJ ou POSS)"                                                        : "XXX",
    "PRO 2° pers. duel (sujet)"                                                                     : "XXX",
    "PRO 2° pers. SG (sujet ou OBJ)"                                                                : "XXX",
    "PRO 2° pers. PL (sujet)"                                                                       : "XXX",
    "PRO 2° pers. PL"                                                                               : "XXX",
    "PRO (OBJ) ou POSS 2° pers. duel"                                                               : "XXX",
    "PRO 2° pers. SG (sujet, OBJ ou POSS)"                                                          : "XXX",
    "PRO (OBJ) ; POSS 2° pers. PL"                                                                  : "XXX",
    "PRO 2° pers. PL (sujet, OBJ ou POSS)"                                                          : "XXX",
    "PRO 2° pers. duel (OBJ ou POSS)"                                                               : "XXX",
    "PRO 2° pers. PL (OBJ ou POSS)"                                                                 : "XXX",
    "PRO 3° pers. SG (sujet)"                                                                       : "XXX",
    "PRO 3° pers. SG (OBJ)"                                                                         : "XXX",
    "PRO 3° pers. masc. PL"                                                                         : "XXX",
    "PRO 3° pers. masc. duel (DX ou ANAPH)"                                                         : "XXX",
    "PRO 3° pers. PL (sujet)"                                                                       : "XXX",
    "PRO 3° pers. PL (OBJ ou POSS)"                                                                 : "XXX",
    "PRO (OBJ) ou POSS 3° pers. duel"                                                               : "XXX",
    "PRO 3° pers. duel (sujet)"                                                                     : "XXX",
    "PRO 3° pers. triel (sujet, OBJ ou POSS)"                                                       : "XXX",
    "PRO 3° pers. duel (OBJ ou POSS)"                                                               : "XXX",
    "PRO 3° pers. triel (OBJ ou POSS)"                                                              : "XXX",
    "PRO 3° pers. SG (OBJ ou POSS)"                                                                 : "XXX",
    "PRO (OBJ) ou POSS 3° pers. triel"                                                              : "XXX",
    "PRO (OBJ) ou POSS 3° pers. SG"                                                                 : "XXX",
    "PRO (sujet) (aspiré)"                                                                          : "XXX",
    "PRO DEIC DX2 (latéral)"                                                                        : "XXX",
    "PRO DEIC ou ANAPH DX3"                                                                         : "XXX",
    "PRO DEM PL"                                                                                    : "XXX",
    "PRO DX2 3° pers. masc. SG"                                                                     : "XXX",
    "PRO DX2 3° pers. masc. PL"                                                                     : "XXX",
    "PRO DX3 3° pers. masc. PL"                                                                     : "XXX",
    "PRO DX2 3° pers. fém. PL"                                                                      : "XXX",
    "PRO DX2 3° pers. PL"                                                                           : "XXX",
    "PRO DX3 3° pers. fém. PL"                                                                      : "XXX",
    "PRO DX3 3° pers."                                                                              : "XXX",
    "PRO INDEP 1° pers. duel excl."                                                                 : "XXX",
    "PRO INDEP 3° pers."                                                                            : "XXX",
    "PRO INDEP 2° pers. duel"                                                                       : "XXX",
    "PRO INDEP 3° pers. PL"                                                                         : "XXX",
    "PRO INDEP 3° pers. triel ou paucal"                                                            : "XXX",
    "PRO INDEP 1° pers. triel excl."                                                                : "XXX",
    "PRO INDEP 1° pers."                                                                            : "XXX",
    "PRO INDEP 1° pers. triel incl."                                                                : "XXX",
    "PRO INDEP 1° pers. excl. PL"                                                                   : "XXX",
    "PRO INDEP 2° pers. PL"                                                                         : "XXX",
    "PRO INDEP 2° pers. triel"                                                                      : "XXX",
    "PRO INDEP 2° pers. SG"                                                                         : "XXX",
    "PRO INDEP 3° pers. duel"                                                                       : "XXX",
    "PRO INT"                                                                                       : "XXX",
    "PRO NEG"                                                                                       : "XXX",

    "PROH"                                                                                          : "XXX",

    "PTCL MDL (adversatif, hypothétique)"                                                           : "XXX",
    "PTCL ASP (post-verbal)"                                                                        : "XXX",
    "PTCL (assertive)"                                                                              : "XXX",
    "PTCL ASP"                                                                                      : "XXX",

    "QNT (réduplication de pe- ???)"                                                                : "XXX",
    "QNT DISTR"                                                                                     : "XXX",
    "QNT ; atténuation"                                                                             : "XXX",
    "QNT ???"                                                                                       : "XXX",

    "REL ou DEM ???"                                                                                : "XXX",

    "RESTR"                                                                                         : "XXX",
    "RESTR ; ASP"                                                                                   : "XXX",
    "RESTR + NUM"                                                                                   : "XXX",
    "RESTR ???"                                                                                     : "XXX",

    "relateur"                                                                                      : "XXX",

    "REV ; ITER GO(s)"                                                                              : "XXX",

    "révolu (u ... mwã)"                                                                            : "XXX",

    "saturateur transitif ???"                                                                      : "XXX",

    "SEQ"                                                                                           : "XXX",

    "sujet ; AGT ???"                                                                               : "XXX",

    "SUFF DIR"                                                                                      : "XXX",
    "SUFF POSS 1° pers."                                                                            : "XXX",
    "SUFF POSS 2° pers."                                                                            : "XXX",
    "SUFF POSS 3° pers. SG"                                                                         : "XXX",
    "SUFF POSS INT"                                                                                 : "XXX",
    "SUFF (transitif)"                                                                              : "XXX",
    "SUFF NOMR"                                                                                     : "XXX",

    "THEM"                                                                                          : "XXX",
    "THEM (nrowö ... ca)"                                                                           : "XXX",

    "transition, répétition, réversif"                                                              : "XXX",

    "triel"                                                                                         : "XXX",

    "v ; MODIF ; INTENS RFLX"                                                                       : "XXX",
    "v LOC ; progressif"                                                                            : "XXX",
    "v STAT ; n"                                                                                    : "XXX",
    "v LOC"                                                                                         : "XXX",
    "v ; ASP"                                                                                       : "XXX",
    "v ; PREP"                                                                                      : "XXX",
    "v ; QNT"                                                                                       : "XXX",
    "v ; n"                                                                                         : "XXX",
    "v DIR"                                                                                         : "XXX",
    "v STAT"                                                                                        : "XXX",
    "v MDL"                                                                                         : "XXX",
    "v ; ADV"                                                                                       : "XXX",
    "v STAT ; ADV"                                                                                  : "XXX",
    "v INT"                                                                                         : "XXX",
    "v IMPERS"                                                                                      : "XXX",
    "v STAT ???"                                                                                    : "XXX",
    "v (non-humains)"                                                                               : "XXX",
    "v (en composition)"                                                                            : "XXX",
    "v ; n ; CLF POSS"                                                                              : "XXX",
    "v CMPAR"                                                                                       : "XXX",
    "v ; INTJ"                                                                                      : "XXX",
    "v REC"                                                                                         : "XXX",
    "v ; INTJ ; n"                                                                                  : "XXX",
    "v STAT ; QNT"                                                                                  : "XXX",
    "v STAT ; MODIF"                                                                                : "XXX",
    "v ASP"                                                                                         : "XXX",
    "v ; ADV"                                                                                       : "XXX",
    "vi ; n"                                                                                        : "XXX",
    "vt (+ PRO pers.)"                                                                              : "XXX",
    "vt (+ PRO)"                                                                                    : "XXX",
    "v ; n ; CLF NUM"                                                                               : "XXX",
    "v STAT ; v"                                                                                    : "XXX",
    "v ; n STAT"                                                                                    : "XXX",

    "vocatif"                                                                                       : "XXX",

    "voyelle euphonique"                                                                            : "XXX",

    "???"                                                                                           : "XXX"
})

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range.update([
    "XXX"
])

## Functions to process some MDF fields (input)

## Functions to process some MDF fields (output)

## Mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout (output)
partOfSpeech_tex.update({
    "XXX" : "unknown"
})

## Functions to process some LaTeX fields (output)

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
def lmf2tex(lexical_entry, font):
    import output.tex as tex
    tex_entry = ""
    # lexeme, id and phonetic variants
    tex_entry += tex.format_lexeme(lexical_entry, font)
    # sound
    tex_entry += tex.format_audio(lexical_entry, font)
    # part of speech
    tex_entry += tex.format_part_of_speech(lexical_entry, font)
    # grammatical notes
    tex_entry += tex.format_notes(lexical_entry, font)
    # Order by sense number
    senses = lexical_entry.get_senses()
    senses.sort(key=lambda sense: sense.get_senseNumber(integer=True))
    for sense in senses:
        if sense.get_senseNumber() is not None:
            tex_entry += sense.get_senseNumber() + ") "
        # definition/gloss and translation
        tex_entry += tex.format_definitions(sense, font, languages=[config.xml.vernacular, config.xml.French, config.xml.national])
        # example
        tex_entry += tex.format_examples(sense, font)
        # usage note
        tex_entry += tex.format_usage_notes(sense, font)
        # encyclopedic information
        tex_entry += tex.format_encyclopedic_informations(sense, font)
        # restriction
        tex_entry += tex.format_restrictions(sense, font)
    # synonym, antonym, morphology, related form
    tex_entry += tex.format_related_forms(lexical_entry, font)
    # borrowed word
    tex_entry += tex.format_borrowed_word(lexical_entry, font)
    # etymology
    tex_entry += tex.format_etymology(lexical_entry, font)
    # paradigms
    tex_entry += tex.format_paradigms(lexical_entry, font)
    tex_entry += tex.format_paradigms(lexical_entry, font)
    # semantic domain
    tex_entry += tex.format_semantic_domains(lexical_entry, font)
    # source
    tex_entry += tex.format_source(lexical_entry, font)
    # status
    tex_entry += tex.format_status(lexical_entry, font)
    # date
    tex_entry += tex.format_date(lexical_entry, font)
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    # Special formatting
    tex_entry = tex.handle_pinyin(tex_entry)
    tex_entry = tex.handle_caps(tex_entry)
    return tex_entry + EOL
