#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import ps_partOfSpeech
from common.range import partOfSpeech_range
from config.tex import lmf_to_tex, partOfSpeech_tex
from utils.io import EOL
from common.defs import VERNACULAR, NATIONAL, ENGLISH, REGIONAL

## To define languages and fonts
import config
FRENCH = "French"

## Semantic domains
sd_order = [
    ("TITLE", "1. le corps humain"),
    [
        ("corps", "1.1. anatomie"),
        ("fonct.nat", "1.2. fonctions naturelles"),
        ("SUBTITLE", "1.3. santé, maladie, médecine"),
        [
            ("santé", "1.3.1. santé, maladie"),
            ("médecine", "1.3.2. remèdes, médecine")
        ],
        ("SUBTITLE", "1.4. vêtements, parure, soins du corps"),
        [
            ("habillement", "1.4.1. vêtements, parure"),
            ("soins", "1.4.2. soins du corps")
        ],
        ("SUBTITLE", "1.5. positions, déplacements, mouvements, actions"),
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
    ("TITLE", "2. techniques"),
    [
        ("SUBTITLE", "2.1. habitat"),
        [
            ("habitat", "2.1.1. habitat"),
            ("maison", "2.1.2. types de maison, architecture de la maison")
        ],
        ("SUBTITLE", "2.2. cultures plantations récoltes"),
        [
            ("cultures", "2.2.1. cultures"),
            ("champs", "2.2.2. types de champs")
        ],
        ("SUBTITLE", "2.3. chasse guerre"),
        [
            ("armes", "2.3.1. armes"),
            ("chasse", "2.3.2. chasse"),
            ("guerre", "2.3.3. guerre")
        ],
        ("pêche", "2.4. pêche"),
        ("navigation", "2.5. navigation"),
        ("feu", "2.6. feu"),
        ("SUBTITLE", "2.7. cuisine alimentation"),
        [
            ("ustensiles", "2.7.1. ustensiles"),
            ("prép.aliments", "2.7.2. préparation des aliments"),
            ("cuisson", "2.7.3. modes de cuisson"),
            ("alimentation", "2.7.4. alimentation")
        ],
        ("SUBTITLE", "2.8. tressage (nattes paniers) cordes noeuds paquets"),
        [
            ("tressage", "2.8.1. tressage"),
            ("nattes", "2.8.2. nattes"),
            ("paniers", "2.8.3. paniers"),
            ("cordes", "2.8.4. cordes"),
            ("couture", "2.8.5. couture"),
            ("paquet", "2.8.6. paquetages")
        ],
        ("SUBTITLE", "2.9. travail du bois forme et consistance des objets"),
        [
            ("outils", "2.9.1. outils, matériaux"),
            ("travail bois", "2.9.2. travail bois"),
            ("carac.objet", "2.9.3. description des objets, formes, consistance")
        ]
    ],
    ("TITLE", "3. individu - société"),
    [
        ("étapes vie", "3.1. cours de la vie"),
        ("SUBTITLE", "3.2. fonctions intellectuelles, sentiments"),
        [
            ("fonct.intellectuelles", "3.2.1. fonctions intellectuelles"),
            ("sentiments", "3.2.2. sentiments")
        ],
        ("SUBTITLE", "3.3. parenté alliance"),
        [
            ("parenté", "3.3.1. parenté"),
            ("appellation parenté", "3.3.2. appellation parenté"),
            ("désignation parenté", "3.3.3. désignation parenté"),
            ("alliance", "3.3.4. alliance"),
            ("couple parenté", "3.3.5. couple parenté")
        ],
        ("SUBTITLE", "3.4. organisation sociale richesses dons échanges"),
        [
            ("société", "3.4.1. organisation sociale"),
            ("richesse", "3.4.2. richesses, monnaies traditionnelles"),
            ("échanges", "3.4.3. dons, échanges, achat et vente, vol")
        ],
        ("religion", "3.5. religion"),
        ("SUBTITLE", "3.6. fêtes danse chant jeux"),
        [
            ("fête", "3.6.1. fêtes"),
            ("jeux", "3.6.2. jeux divers")
        ],
        ("SUBTITLE", "3.7. traditions orales relations inter-individuelles"),
        [
            ("oralité", "3.7.1. tradition orale"),
            ("discours", "3.7.2. échanges verbaux"),
            ("exclamations", "3.7.3. exclamations"),
            ("interaction", "3.7.4. relations"),
        ]
    ],
    ("TITLE", "4. nature"),
    [
        ("SUBTITLE", "4.1. ciel"),
        [
            ("astres", "4.1.1. astres"),
            ("temps", "4.1.2. découpage du temps"),
            ("vent", "4.1.3. vent"),
            ("climat", "4.1.4. phénomènes atmosphériques"),
            ("couleurs", "4.1.5. couleurs")
        ],
        ("SUBTITLE", "4.2. terre"),
        [
            ("terrain", "4.2.1. les terrains et leur constitution"),
            ("topographie", "4.2.2. topographie"),
            ("orientation", "4.2.3. orientation")
        ],
        ("eau", "4.3. eau (eau douce mer)")
    ],
    ("TITLE", "5. zoologie"),
    [
        ("oiseaux", "5.1. oiseaux"),
        ("SUBTITLE", "5.2. mammifères"),
        [
            ("mammifères", "5.2.1. mammifères"),
            ("mammifères marins", "5.2.2. mammifères marins")
        ],
        ("SUBTITLE", "5.3. reptiles"),
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
    ("TITLE", "6. botanique"),
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

def get_is(lexical_entry):
    for sd in lexical_entry.get_semantic_domains():
        # Consider only the first semantic domain
        return sd
    return "-"
items=lambda lexical_entry: get_is(lexical_entry)

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps_partOfSpeech.update({
    # HimalCo
    "adj"           : "adjective",                  # adjective
    "adv"           : "adverb",                     # adverb(ial)
    "class"         : "classifier",                 # classifier (MDF)
    "clf"           : "classifier",                 # classifier (Leipzig)
    "cnj"           : "conjunction",                # conjunction
    "disc.PTCL"     : "particle",                   # discourse particle
    "ideo"          : "ideophone",                  # ideophones
    "intj"          : "interjection",               # interjection
    "interj"        : "interjection",               # interjection -> khaling
    "lnk"           : "coordinating conjunction",   # linker
    "n"             : "noun",                       # noun
    "Np"            : "possessed noun",             # possessed nouns
    "_poss._pref"   : "possessed noun",             # possessed nouns -> koyi
    "neg"           : "negation",                   # negative
    "num"           : "numeral",                    # number
    "prep"          : "preposition",                # preposition
    "pro"           : "pronoun",                    # pronoun/pronominal
    "vi.s"          : "stative intransitive verb",  # stative intransitive verb
    # yuanga
    "voyelle euphonique"                                                                                            : "XXX",
    "pronom sujet 2 pluriel"                                                                                        : "XXX",
    "relatif (ou) démonstratif?"                                                                                    : "XXX",
    "préfixe des noms d'agent"                                                                                      : "XXX",
    "classificateur numéerique des animées"                                                                         : "XXX",
    "marque de possession (de certains lexèmes)"                                                                    : "XXX",
    "démonstratif"                                                                                                  : "XXX",
    "DX1 ; anaphorique"                                                                                             : "XXX",
    "pronom 1° inclusif pluriel objet ou  possessif"                                                                : "XXX",
    "pronom DX2 3°  pers. masc. sg"                                                                                 : "XXX",
    "préfixe référant à une surface extérieure"                                                                     : "XXX",
    "démonstratif (duel ou pluriel)"                                                                                : "XXX",
    "pronom DX2 3°  pers. masc. pluriel"                                                                            : "XXX",
    "pronom 3°  pers. masc. pluriel"                                                                                : "XXX",
    "pronom DX3 3°  pers. masc. pluriel"                                                                            : "XXX",
    "pronom 3°  pers. masc. duel (DX ou anaphorique)"                                                               : "XXX",
    "démonstratif DX"                                                                                               : "XXX",
    "numéral animés"                                                                                                : "XXX",
    "numéral (animés)"                                                                                              : "XXX",
    "démonstratif anaphorique"                                                                                      : "XXX",
    "pronom DX3 3°  pers."                                                                                          : "XXX",
    "démonstratif DX2"                                                                                              : "XXX",
    "interrogatif locatif (dynamique)"                                                                              : "XXX",
    "préfixe instrumental, nominalisant"                                                                            : "XXX",
    "particule modale (adversatif ; hypothétique, )"                                                                : "XXX",
    "préfixe des ordinaux"                                                                                          : "XXX",
    "classificateur numérique"                                                                                      : "XXX",
    "nom inaliénable"                                                                                               : "XXX",
    "collectif"                                                                                                     : "XXX",
    "ordinal"                                                                                                       : "XXX",
    "modalité (nom)"                                                                                                : "XXX",
    "classificateur numéral (des morceaux de bois)"                                                                 : "XXX",
    "pronom 1° duel exclusif (sujet, objet ou"                                                                      : "XXX",
    "pronom 1° duel exclusif (objet ou possessif)"                                                                  : "XXX",
    "adresse honorifique"                                                                                           : "XXX",
    "interj. de pitié, d'affection"                                                                                 : "XXX",
    "marque d'objet indirect"                                                                                       : "XXX",
    "interrogatif dynamique locatif"                                                                                : "XXX",
    "préposition (objet indirect)"                                                                                  : "XXX",
    "n, classificateur possessif"                                                                                   : "XXX",
    "pronom sujet 2°  duel"                                                                                         : "XXX",
    "pronom 2° singulier sujet ou objet"                                                                            : "XXX",
    "v ; modificateur; itensif (reflechi)"                                                                          : "XXX",
    "préfixe classificateur numérique des mains de banane"                                                          : "XXX",
    "classificateur numérique des feuilles"                                                                         : "XXX",
    "préfixe des couples de parenté"                                                                                : "XXX",
    "directionnel transverse"                                                                                       : "XXX",
    "adverbe (marque d')"                                                                                           : "XXX",
    "parenté réciproque ???"                                                                                        : "XXX",
    "pronom objet ou possessif 1° duel inclusif"                                                                    : "XXX",
    "adv. locatif spatio-temporel anaphorique ??"                                                                   : "XXX",
    "préfixe de relations duelles"                                                                                  : "XXX",
    "n; parenté réciproque"                                                                                         : "XXX",
    "interrogatif locatif (statique)"                                                                               : "XXX",
    "marque de parenté réciproque"                                                                                  : "XXX",
    "classificateur dénombrant des morceaux PA [pas à Gomen]"                                                       : "XXX",
    "classificateur numérique des tissus et étoffes végétales"                                                      : "XXX",
    "aspect duratif"                                                                                                : "XXX",
    "modalité injonctive"                                                                                           : "XXX",
    "aspect ou restrictif"                                                                                          : "XXX",
    "aspect"                                                                                                        : "XXX",
    "locution"                                                                                                      : "XXX",
    "v. locatif ; progressif"                                                                                       : "XXX",
    "conjonction ; thématisation"                                                                                   : "XXX",
    "particule aspect post-verbal"                                                                                  : "XXX",
    "v.statif; n"                                                                                                   : "XXX",
    "v. locatif"                                                                                                    : "XXX",
    "conjonction de temps"                                                                                          : "XXX",
    "marque de futur"                                                                                               : "XXX",
    "locatif directionnel"                                                                                          : "XXX",
    "déict.-direct."                                                                                                : "XXX",
    "n (en composition)"                                                                                            : "XXX",
    "aspect persistif"                                                                                              : "XXX",
    "intensificateur"                                                                                               : "XXX",
    "marque d'agent"                                                                                                : "XXX",
    "démonstratif DX1"                                                                                              : "XXX",
    "couple de parenté"                                                                                             : "XXX",
    "nom locatif"                                                                                                   : "XXX",
    "locatif DX2"                                                                                                   : "XXX",
    "locatif anaphorique"                                                                                           : "XXX",
    "adv. locatif DX2"                                                                                              : "XXX",
    "locatif déictique DX3"                                                                                         : "XXX",
    "démonstratif DX3"                                                                                              : "XXX",
    "preposition; adv.; conj."                                                                                      : "XXX",
    "interpellation"                                                                                                : "XXX",
    "démonstratif sg"                                                                                               : "XXX",
    "nom marque de bénéficiaire"                                                                                    : "XXX",
    "classificateur possessif"                                                                                      : "XXX",
    "adverbe locatif"                                                                                               : "XXX",
    "v; aspect"                                                                                                     : "XXX",
    "v; préposition"                                                                                                : "XXX",
    "aspect itératif"                                                                                               : "XXX",
    "suffixe directionnel"                                                                                          : "XXX",
    "marque de possession indirecte"                                                                                : "XXX",
    "pronom sujet 3° singulier"                                                                                     : "XXX",
    "interrogatif statique (humains, pronoms, noms)"                                                                : "XXX",
    "possessif 1° duel inclusif"                                                                                    : "XXX",
    "pronom objet (ou) possessif 1° pers. duel inclusif"                                                            : "XXX",
    "interrogatif statique"                                                                                         : "XXX",
    "1ère personne plur. incl."                                                                                     : "XXX",
    "possessif 1° pers. inclusif"                                                                                   : "XXX",
    "pronom indépendant 1°  pers. duel exclusif"                                                                    : "XXX",
    "pronom indépendant 2° personne singulier"                                                                      : "XXX",
    "restrictif"                                                                                                    : "XXX",
    "pronom indépendant 3°  pers."                                                                                  : "XXX",
    "pronom indépendant 2° personne duel"                                                                           : "XXX",
    "pronom indépendant 3°  pers.pluriel"                                                                           : "XXX",
    "pronom DX2 3°  pers. féminin pluriel"                                                                          : "XXX",
    "pronom DX2 3°  pers. pluriel"                                                                                  : "XXX",
    "pronom DX3 3°  pers. féminin pluriel"                                                                          : "XXX",
    "pronom indépendant 3°  pers. duel"                                                                             : "XXX",
    "interpellation ou démonstratif"                                                                                : "XXX",
    "pron. indépendant 3° triel (ou) paucal"                                                                        : "XXX",
    "pronom indépendant 1° triel exclusif"                                                                          : "XXX",
    "pronom indépendant 1° pers."                                                                                   : "XXX",
    "pronom indépendant 1° personne triel inclusif"                                                                 : "XXX",
    "pronom indépendant 1° personne exclusif pluriel"                                                               : "XXX",
    "pronom indépendant 2° personne pluriel"                                                                        : "XXX",
    "pronom indépendant 2° triel"                                                                                   : "XXX",
    "pronom indépendant 2° sg"                                                                                      : "XXX",
    "pronom indépendant 1°  pers. pluriel exclusif"                                                                 : "XXX",
    "pronom indépendant 1° exclusif pluriel"                                                                        : "XXX",
    "v ;"                                                                                                           : "XXX",
    "loc"                                                                                                           : "XXX",
    "duel"                                                                                                          : "XXX",
    "triel"                                                                                                         : "XXX",
    "anaphorique"                                                                                                   : "XXX",
    "DX1"                                                                                                           : "XXX",
    "contraste"                                                                                                     : "XXX",
    "vocatif"                                                                                                       : "XXX",
    "thématisation"                                                                                                 : "XXX",
    "n (ordinal)"                                                                                                   : "XXX",
    "v; quant"                                                                                                      : "XXX",
    "directionnel"                                                                                                  : "XXX",
    "direction"                                                                                                     : "XXX",
    "adverbe"                                                                                                       : "XXX",
    "locatif"                                                                                                       : "XXX",
    "n ; v"                                                                                                         : "XXX",
    "n; v"                                                                                                          : "XXX",
    "nom ; verbe statif"                                                                                            : "XXX",
    "v. statif; n"                                                                                                  : "XXX",
    "v; n"                                                                                                          : "XXX",
    "v ; n"                                                                                                         : "XXX",
    "nom"                                                                                                           : "XXX",
    "interrogatif"                                                                                                  : "XXX",
    "quantificateur"                                                                                                : "XXX",
    "verbe"                                                                                                         : "XXX",
    "v + directionnel"                                                                                              : "XXX",
    "v-directionnel"                                                                                                : "XXX",
    "v directionnel"                                                                                                : "XXX",
    "verbe statif"                                                                                                  : "XXX",
    "v.statif"                                                                                                      : "XXX",
    "v.t"                                                                                                           : "XXX",
    "v.t."                                                                                                          : "XXX",
    "numéral"                                                                                                       : "XXX",
    "préfixe"                                                                                                       : "XXX",
    "classificateur"                                                                                                : "XXX",
    "n ;v"                                                                                                          : "XXX",
    "v.stat."                                                                                                       : "XXX",
    "v. statif"                                                                                                     : "XXX",
    "n (bénéficiaire)"                                                                                              : "XXX",
    "v (modalité)"                                                                                                  : "XXX",
    "n (inaliénable)"                                                                                               : "XXX",
    "adv. quantificateur"                                                                                           : "XXX",
    "négation (en réponse à une question)"                                                                          : "XXX",
    "négatif"                                                                                                       : "XXX",
    "v."                                                                                                            : "XXX",
    "v.i"                                                                                                           : "XXX",
    "conj."                                                                                                         : "XXX",
    "conj"                                                                                                          : "XXX",
    "adv."                                                                                                          : "XXX",
    "adv. modificateur"                                                                                             : "XXX",
    "v; adverbe"                                                                                                    : "XXX",
    "v.i."                                                                                                          : "XXX",
    "2 pl."                                                                                                         : "XXX",
    "pronom indépendant 2°  pluriel"                                                                                : "XXX",
    "pronom indépendant 2°  pers. pluriel"                                                                          : "XXX",
    "modificateur"                                                                                                  : "XXX",
    "modalité"                                                                                                      : "XXX",
    "pronom objet 3° personne singulier"                                                                            : "XXX",
    "pronom déictique Dx2 latéral"                                                                                  : "XXX",
    "DX2 ; anaphorique ; assertif"                                                                                  : "XXX",
    "pronom déictique ou anaphorique Dx3"                                                                           : "XXX",
    "pronom interrogatif"                                                                                           : "XXX",
    "déictique DX3"                                                                                                 : "XXX",
    "démonstratif médial ou proche"                                                                                 : "XXX",
    "connecteur"                                                                                                    : "XXX",
    "pronom objet ou possessif 2°  personne duel"                                                                   : "XXX",
    "coordination"                                                                                                  : "XXX",
    "relatif"                                                                                                       : "XXX",
    "??"                                                                                                            : "XXX",
    "prefixe"                                                                                                       : "XXX",
    "distributif"                                                                                                   : "XXX",
    "n ; locatif"                                                                                                   : "XXX",
    "associatif"                                                                                                    : "XXX",
    "nom ; v. statif"                                                                                               : "XXX",
    "v. statif; adverbe"                                                                                            : "XXX",
    "verbe interrogatif"                                                                                            : "XXX",
    "v. interrogatif"                                                                                               : "XXX",
    "préposition"                                                                                                   : "XXX",
    "négation"                                                                                                      : "XXX",
    "aspect révolu"                                                                                                 : "XXX",
    "prohibitif"                                                                                                    : "XXX",
    "verbe; n"                                                                                                      : "XXX",
    "adv. atténuatif (d'un ordre) (forme de politesse); ponctuel"                                                   : "XXX",
    "prédicat négation"                                                                                             : "XXX",
    "restrictif ; aspect"                                                                                           : "XXX",
    "marque de sujet , d'agent ??"                                                                                  : "XXX",
    "préfixe indiquant une position couchée"                                                                        : "XXX",
    "atténuatif ??"                                                                                                 : "XXX",
    "conjonction (complémentation)"                                                                                 : "XXX",
    "dire du mal de qqn"                                                                                            : "XXX",
    "n (référence)"                                                                                                 : "XXX",
    "prédicat négatif (humain)"                                                                                     : "XXX",
    "marque de bénéficiaire"                                                                                        : "XXX",
    "v. impersonnel"                                                                                                : "XXX",
    "v. statif ??"                                                                                                  : "XXX",
    "v. (non-humains)"                                                                                              : "XXX",
    "aspect habituel"                                                                                               : "XXX",
    "v (en composition)"                                                                                            : "XXX",
    "Classificateur possessif"                                                                                      : "XXX",
    "locatif ; n"                                                                                                   : "XXX",
    "verbe; nom; classificateur possessif"                                                                          : "XXX",
    "nom ; v"                                                                                                       : "XXX",
    "article pluriel"                                                                                               : "XXX",
    "pronom objet ou possessif 3° pluriel"                                                                          : "XXX",
    "pronom 3° personne pluriel (sujet)"                                                                            : "XXX",
    "déictique pluriel DX1 ou anaphorique"                                                                          : "XXX",
    "pronom démonstratif pluriel"                                                                                   : "XXX",
    "déictique pluriel"                                                                                             : "XXX",
    "démonstratif pl"                                                                                               : "XXX",
    "démonstratif duel DX2 et anaphorique"                                                                          : "XXX",
    "démonstratif pluriel (DX3)"                                                                                    : "XXX",
    "démonstratif DX3 ou anaphorique"                                                                               : "XXX",
    "pronom objet ou possessif 3° pers. duel"                                                                       : "XXX",
    "pronom duel 3° personne (sujet)"                                                                               : "XXX",
    "déictique duel DX1 ou anaphorique"                                                                             : "XXX",
    "déterminant, démonstratif duel"                                                                                : "XXX",
    "déictique duel DX3 latéralement"                                                                               : "XXX",
    "démonstratif duel (DX3)"                                                                                       : "XXX",
    "pronom 3° triel (sujet, objet, possessif)"                                                                     : "XXX",
    "pronom objet ou possessif  3° triel"                                                                           : "XXX",
    "pronom sujet (aspiré)"                                                                                         : "XXX",
    "suff. possessif 2° pers."                                                                                      : "XXX",
    "marque d'objet"                                                                                                : "XXX",
    "n; v. statif"                                                                                                  : "XXX",
    "marque de non singulier"                                                                                       : "XXX",
    "inchoatif, en cours"                                                                                           : "XXX",
    "classificateur numérique des lots (fête de la nouvelle igname, contexte cérémoniel)"                           : "XXX",
    "classificateur numéral (pour compter des paquets d'ignames"                                                    : "XXX",
    "n ; classificateur numérique"                                                                                  : "XXX",
    "modif."                                                                                                        : "XXX",
    "démonstratif pluriel (post-nom)"                                                                               : "XXX",
    "pronom"                                                                                                        : "XXX",
    "démonstratif duel (post nom)"                                                                                  : "XXX",
    "nom quantificateur"                                                                                            : "XXX",
    "inchoatif"                                                                                                     : "XXX",
    "pronom 1° personne triel exclusif (sujet, objet ou possessif)"                                                 : "XXX",
    "préfixe nominalisant"                                                                                          : "XXX",
    "déterminant duel"                                                                                              : "XXX",
    "mode"                                                                                                          : "XXX",
    "v. comparatif"                                                                                                 : "XXX",
    "n ;"                                                                                                           : "XXX",
    "nmz"                                                                                                           : "XXX",
    "pronom sujet 1° personne duel inclusif"                                                                        : "XXX",
    "directionnel ventif"                                                                                           : "XXX",
    "pronom sujet 1° personne triel inclusif"                                                                       : "XXX",
    "forme déterminée de mwa ; préfixe désignant un contenant"                                                      : "XXX",
    "adverbe de temps"                                                                                              : "XXX",
    "transition, répétition, réversif"                                                                              : "XXX",
    "révolu (u ...mwã)"                                                                                             : "XXX",
    "pronom sujet 1° inclusif pluriel"                                                                              : "XXX",
    "adv. séquentiel ; continuatif"                                                                                 : "XXX",
    "suff. poss. 3° pers. sing."                                                                                    : "XXX",
    "préposition locative"                                                                                          : "XXX",
    "pron. négatif"                                                                                                 : "XXX",
    "locatif spatio-temporel"                                                                                       : "XXX",
    "conjonction hypothétique"                                                                                      : "XXX",
    "démonstratif DX2 ; anaphorique ; assertif"                                                                     : "XXX",
    "préposition (ablatif)"                                                                                         : "XXX",
    "pré-locatif + locatif"                                                                                         : "XXX",
    "locatif (comparaison)"                                                                                         : "XXX",
    "relateur"                                                                                                      : "XXX",
    "fréquentatif"                                                                                                  : "XXX",
    "préposition spatio-temporelle"                                                                                 : "XXX",
    "suffixe transitif"                                                                                             : "XXX",
    "démonstratif déictique ou anaphorique (DX3)"                                                                   : "XXX",
    "n locatif"                                                                                                     : "XXX",
    "num."                                                                                                          : "XXX",
    "préfixe de lieu"                                                                                               : "XXX",
    "morphème de thématisation (nrowö ... ca)"                                                                      : "XXX",
    "1sg sujet ou objet"                                                                                            : "XXX",
    "pronom objet ou possessif 1er singulier"                                                                       : "XXX",
    "suff. possessif 1° personne"                                                                                   : "XXX",
    "déictique"                                                                                                     : "XXX",
    "démonstratif directionnel"                                                                                     : "XXX",
    "anaphorique (discours  ou passé ???)"                                                                          : "XXX",
    "déterminant ; pronom déictique DX1"                                                                            : "XXX",
    "démonstratif distal DX3"                                                                                       : "XXX",
    "démonstratif DX4"                                                                                              : "XXX",
    "directionnel centrifuge"                                                                                       : "XXX",
    "anaphorique du discours"                                                                                       : "XXX",
    "pronom objet ou possessif 1er triel inclusif"                                                                  : "XXX",
    "classificateur des multiples"                                                                                  : "XXX",
    "aspect accompli"                                                                                               : "XXX",
    "séquentiel"                                                                                                    : "XXX",
    "v ; interjection;"                                                                                             : "XXX",
    "déictique (DX3 visible)"                                                                                       : "XXX",
    "n conjonctif"                                                                                                  : "XXX",
    "restrictif + numéral"                                                                                          : "XXX",
    "n-fois"                                                                                                        : "XXX",
    "préfixe causatif"                                                                                              : "XXX",
    "adv ?"                                                                                                         : "XXX",
    "classificateur des armes"                                                                                      : "XXX",
    "v ;n"                                                                                                          : "XXX",
    "préfixe réciproque; collectif"                                                                                 : "XXX",
    "récip-v"                                                                                                       : "XXX",
    "quantificateur (réduplication de pe- ??)"                                                                      : "XXX",
    "v. réciproque"                                                                                                 : "XXX",
    "collectif + pronom"                                                                                            : "XXX",
    "quantificateur distributif"                                                                                    : "XXX",
    "aspect inacccompli"                                                                                            : "XXX",
    "v; interjection ; n"                                                                                           : "XXX",
    "n ; pronom"                                                                                                    : "XXX",
    "classificateur numérique générique et des objets ronds"                                                        : "XXX",
    "quantificateur ; atténuation"                                                                                  : "XXX",
    "quantificateur ???"                                                                                            : "XXX",
    "v. i"                                                                                                          : "XXX",
    "injonction, optatif"                                                                                           : "XXX",
    "nom locatif (forme possessive de pwamwa)"                                                                      : "XXX",
    "prép.  marque de bénéficiaire"                                                                                 : "XXX",
    "interrog."                                                                                                     : "XXX",
    "classificateur des objets ronds"                                                                               : "XXX",
    "doute"                                                                                                         : "XXX",
    "classificateur des maisons"                                                                                    : "XXX",
    "v  ; n"                                                                                                        : "XXX",
    "v. statif ; adverbe"                                                                                           : "XXX",
    "interj ; v"                                                                                                    : "XXX",
    "c"                                                                                                             : "XXX",
    "v.stat.; quantificateur"                                                                                       : "XXX",
    "particule assertive"                                                                                           : "XXX",
    "interr."                                                                                                       : "XXX",
    "suffixe possessif interrogatif"                                                                                : "XXX",
    "futur"                                                                                                         : "XXX",
    "nom interjection"                                                                                              : "XXX",
    "v. statif; modificateur"                                                                                       : "XXX",
    "v. aspect"                                                                                                     : "XXX",
    "v ; adv."                                                                                                      : "XXX",
    "interjection; appel respectueux à une personne"                                                                : "XXX",
    "v. statif ; n"                                                                                                 : "XXX",
    "restrictif ??"                                                                                                 : "XXX",
    "marque de contraste ; état"                                                                                    : "XXX",
    "locution adverbiale"                                                                                           : "XXX",
    "interrogatif indéfini"                                                                                         : "XXX",
    "v.i; n"                                                                                                        : "XXX",
    "v.t. (+ pron. pers.)"                                                                                          : "XXX",
    "particule aspectuelle"                                                                                         : "XXX",
    "v.t (+ pronoms)"                                                                                               : "XXX",
    "v ; n ; classificateur numérique"                                                                              : "XXX",
    "réfléchi"                                                                                                      : "XXX",
    "v.statif ; n"                                                                                                  : "XXX",
    "accompli"                                                                                                      : "XXX",
    "préposition instrumentale; marque d'agent ??"                                                                  : "XXX",
    "marque d'agent ??"                                                                                             : "XXX",
    "verbe, nom"                                                                                                    : "XXX",
    "dispersif; distributif"                                                                                        : "XXX",
    "préposition régime indirect"                                                                                   : "XXX",
    "marque de focus"                                                                                               : "XXX",
    "suffixe nominalisant"                                                                                          : "XXX",
    "conjonction de but"                                                                                            : "XXX",
    "marque génitive (déterminant non-spécifique, générique ??)"                                                    : "XXX",
    "nom locatif; v"                                                                                                : "XXX",
    "préposition, conjonction"                                                                                      : "XXX",
    "nom comparatif"                                                                                                : "XXX",
    "interrogatif comparatif"                                                                                       : "XXX",
    "classificateur numérique des lots cérémoniels"                                                                 : "XXX",
    "numéral (pour certains types de dons coutumiers"                                                               : "XXX",
    "numéral numéral (pour certains types de dons coutumiers qui"                                                   : "XXX",
    "numéral (pour certains types de dons coutumiers qui se comptent par deux)"                                     : "XXX",
    "interlocution"                                                                                                 : "XXX",
    "classificateur numérique des objets longs"                                                                     : "XXX",
    "numéral ordinal"                                                                                               : "XXX",
    "classificateur numéral (bois, arbres, certaines racines comestibles, cordes ; objets longs  sagaies, doigts )" : "XXX",
    "n ; v. statif"                                                                                                 : "XXX",
    "marque d'indétermination"                                                                                      : "XXX",
    "coord."                                                                                                        : "XXX",
    "marque de passé"                                                                                               : "XXX",
    "conjonction (relatif)"                                                                                         : "XXX",
    "réversif, itératif  GO(s)"                                                                                     : "XXX",
    "préposition (marque d'instrument)"                                                                             : "XXX",
    "saturateur transitif ??"                                                                                       : "XXX",
    "locution interrogative"                                                                                        : "XXX",
    "v. statif ; v"                                                                                                 : "XXX",
    "pronom objet ou possessif 3° singulier"                                                                        : "XXX",
    "pronom 3° sg objet"                                                                                            : "XXX",
    "pronom 2° sg sujet, objet ou possessif"                                                                        : "XXX",
    "n (terme d'appellation ou référence)"                                                                          : "XXX",
    "focalisation ; restrictif (antéposé au GN) (za ... nye...)"                                                    : "XXX",
    "intensificateur ; assertif (devant le prédicat)"                                                               : "XXX",
    "pronom 1° inclusif objet ou possessif"                                                                         : "XXX",
    "itératif"                                                                                                      : "XXX",
    "pronom sujet 1° exclusif pluriel"                                                                              : "XXX",
    "pronom objet ou possessif 1° plur. exclusif"                                                                   : "XXX",
    "pronom sujet 2°  pluriel"                                                                                      : "XXX",
    "pronom objet ; possessif 2° pluriel"                                                                           : "XXX",
    "2° pluriel sujet ou objet ou possessif"                                                                        : "XXX",
    ##
    "cl"            : "classifier",                 # classifier
    "conjonction"   : "conjunction",                # conjunction
    "expression"    : "expression",                 #
    "idph"          : "ideophone",                  # ideophones
    "idph.1"        : "ideophone.1",                # ideophones
    "idph.2"        : "ideophone.2",                # ideophones
    "idph.3"        : "ideophone.3",                # ideophones
    "idph.4"        : "ideophone.4",                # ideophones
    "idph.5"        : "ideophone.5",                # ideophones
    "idph.6"        : "ideophone.6",                # ideophones
    "idph.7"        : "ideophone.7",                # ideophones
    "idph.8"        : "ideophone.8",                # ideophones
    "n N"           : "noun",                       # noun
    "nq"            : "noun",                       # noun
    "np"            : "possessed noun",             # possessed nouns
    "nP"            : "possessed noun",             # possessed nouns
    "Posp"          : "possessed noun",             # possessed nouns
    "Post"          : "possessed noun",             # possessed nouns
    "postp"         : "possessed noun",             # possessed nouns
    "quant"         : "numeral",                    # number
    "part"          : "particle",                   # discourse particle
    "Part"          : "particle",                   # discourse particle
    "vi-"           : "intransitive verb",          # intransitive verb
    "vinh"          : "stative intransitive verb",  # stative intransitive verb
    "vStat"         : "stative intransitive verb",  # stative intransitive verb
    "vst"           : "stative intransitive verb",  # stative intransitive verb
    "vs"            : "stative intransitive verb",  # stative intransitive verb
    "vl"            : "bitransistive verb",         # labial verb
    "vlb"           : "bitransistive verb",         # labial verb
    "vlab"          : "bitransistive verb",         # labial verb
    "T"             : "time noun",                  # ?
    "indef"         : "indefinite determiner"       # ?
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
    # definition/gloss and translation
    tex_entry += tex.format_definitions(lexical_entry, font, languages=[config.xml.vernacular, config.xml.French, config.xml.national])
    # example
    tex_entry += tex.format_examples(lexical_entry, font)
    # usage note
    tex_entry += tex.format_usage_notes(lexical_entry, font)
    # encyclopedic information
    tex_entry += tex.format_encyclopedic_informations(lexical_entry, font)
    # restriction
    tex_entry += tex.format_restrictions(lexical_entry, font)
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
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    # Special formatting
    tex_entry = tex.handle_pinyin(tex_entry)
    tex_entry = tex.handle_caps(tex_entry)
    return tex_entry + EOL
