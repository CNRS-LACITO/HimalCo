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
    ("TITLE 1", "1. Le corps : humains et animaux"),
    [
        ("TITLE 2", "1.1. Anatomie"),
        [
            ("corps", "1.1.1. Corps humain"),
            ("corps_animaux", "1.1.2. Corps animal")
        ],
        ("TITLE 2", "1.2. Fonctions naturelles"),
        [
            ("fonct.nat", "1.2.1. Fonctions naturelles humain"),
            ("fonct.nat.animaux", "1.2.2. Fonctions naturelles animaux")
        ],
        ("TITLE 2", "1.3. Santé, maladie, médecine"),
        [
            ("santé", "1.3.1. Santé, maladie"),
            ("médecine", "1.3.2. Remèdes, médecine")
        ],
        ("TITLE 2", "1.4. Vêtements, parure, soins du corps"),
        [
            ("habillement", "1.4.1. Vêtements, parure"),
            ("soin", "1.4.2. Soins du corps")
        ],
        ("TITLE 2", "1.5. Positions, déplacements, mouvements, actions"),
        [
            ("position", "1.5.1. Préfixes verbaux de position"),
            ("mouvement", "1.5.2. Préfixes verbaux de mouvement"),
            ("déplacement", "1.5.3. Déplacements, mouvements avec les pieds"),
            ("portage", "1.5.4. Portage"),
            ("action.tête", "1.5.5. Mouvements ou actions avec la tête, les yeux, la bouche"),
            ("action_corps", "1.5.6. Mouvements de bras, de mains"),
            ("action", "1.5.7. Verbes d'action (en général)"),
            ("action_corps_animaux", "1.5.8. Verbes d'action faite par des animaux"),
            ("action eau, liquide, fumée", "1.5.9. Actions liées aux éléments"),
            ("action.plantes","1.5.10. Actions liées aux plantes"),
            ("manière", "1.5.11. Postverbes de manière"),
            ("action_outils", "1.5.12. Actions avec un instrument, un outil")
        ]
    ],
    ("TITLE 1", "2. Caractéristiques et propriétés"),
    [
        ("son", "2.1. Sons, bruits"),
        ("couleur", "2.2. Couleurs"),
        ("caract.personne", "2.3. Caractéristiques et propriétés des personnes"),
        ("caract.animal", "2.4. Caractéristiques et propriétés des animaux"),
        ("TITLE 2", "2.5. Caractéristiques et propriétés des objets"),
        [
            ("caract.objet", "2.5.1. Description des objets, formes, consistance, taille"),
            ("configuration", "2.5.2. Configuration des objets")
        ],
    ],
    ("TITLE 1", "3. Techniques"),
    [
        ("TITLE 2", "3.1. Habitat"),
        [
            ("habitat", "3.1.1. Habitat"),
            ("maison", "3.1.2. Types de maison, architecture de la maison"),
            ("maison.objet", "3.1.3. Objets et meubles de la maison"),
        ],
        ("TITLE 2", "3.2. Cultures, plantations, récoltes, végétation"),
        [
            ("cultures", "3.2.1. Cultures, techniques, boutures"),
            ("cultures_objet", "3.2.2. Objets, outils"),
            ("champs", "3.2.3. Types de champs"),
            ("végétation", "3.2.4. Végétation")
        ],
        ("TITLE 2", "3.3. Chasse guerre"),
        [
            ("armes", "3.3.1. Armes"),
            ("chasse", "3.3.2. Chasse"),
            ("guerre", "3.3.3. Guerre")
        ],
        ("pêche", "3.4. Pêche"),
        ("navigation", "3.5. Navigation"),
        ("feu", "3.6. Feu"),
        ("TITLE 2", "3.7. Cuisine alimentation"),
        [
            ("ustensile", "3.7.1. Ustensiles"),
            ("prép.aliments", "3.7.2. Préparation des aliments"),
            ("cuisson", "3.7.3. Modes de cuisson"),
            ("nourriture", "3.7.4. Alimentation"),
            ("nourriture_goût", "3.7.5. Goût des aliments")
        ],
        ("TITLE 2", "3.8. Tressage (nattes paniers) cordes noeuds paquets"),
        [
            ("tressage", "3.8.1. Tressage"),
            ("natte", "3.8.2. Nattes"),
            ("paniers", "3.8.3. Paniers"),
            ("cordes", "3.8.4. Cordes"),
            ("couture", "3.8.5. Couture"),
            ("paquet", "3.8.6. Paquetages")
        ],
        ("TITLE 2", "3.9. Bois et travail du bois, outils"),
        [
            ("bois", "3.9.1. Bois"),
            ("bois_travail", "3.9.2. Travail bois")
        ],
        ("TITLE 2", "3.10. Outils, instruments, matériaux, chose"),
        [
            ("outils", "3.10.1. Outils"),
            ("instrument", "3.10.2. Instruments")
        ]
    ],
    ("TITLE 1", "4. Individu - société"),
    [
        ("étapes.vie", "4.1. Cours de la vie"),
        ("TITLE 2", "4.2. Fonctions intellectuelles, sentiments"),
        [
            ("fonct.intell.", "4.2.1. fonctions intellectuelles"),
            ("sentiments", "4.2.2. Sentiments"),
            ("temps", "4.2.3. Découpage du temps, jours")
        ],
        ("TITLE 2", "4.3. Parenté alliance"),
        [
            ("parenté", "4.3.1. Parenté"),
            ("appellation parenté", "4.3.2. Appellation parenté"),
            ("désignation parenté", "4.3.3. Désignation parenté"),
            ("alliance", "4.3.4. Alliance"),
            ("parenté_couple", "4.3.5. Couple parenté")
        ],
        ("TITLE 2", "4.4. Organisation sociale richesses dons échanges"),
        [
            ("société", "4.4.1. Organisation sociale"),
            ("richesses", "4.4.2. Richesses, monnaies traditionnelles"),
            ("échanges", "4.4.3. Dons, échanges, achat et vente, vol"),
            ("coutumes_objet", "4.4.4. Objets coutumiers"),
            ("coutumes", "4.4.5. Coutumes")
        ],
        ("religion", "4.5. Religion"),
        ("TITLE 2", "4.6. Fêtes danse chant jeux"),
        [
            ("fête", "4.6.1. Fêtes"),
            ("danse", "4.6.2. Danses"),
            ("musique", "4.6.3. Musique"),
            ("jeu", "4.6.4. Jeux divers")
        ],
        ("TITLE 2", "4.7. Traditions orales relations inter-individuelles"),
        [
            ("oralité", "4.7.1. Tradition orale"),
            ("discours", "4.7.2. Discours, échanges verbaux"),
            ("interaction", "4.7.3. Relations"),
            ("interpellation", "4.7.4. Interpellation"),
            ("exclamation", "4.7.5. Exclamation")
        ]
    ],
    ("TITLE 1", "5. Nature"),
    [
        ("TITLE 2", "5.1. Ciel"),
        [
            ("astre", "5.1.1. Astres"),
            ("vent", "5.1.2. Vent"),
            ("temps_atmosphérique", "5.1.3. Phénomènes atmosphériques et naturels"),
            ("température", "5.1.4. Température")
        ],
        ("TITLE 2", "5.2. Terre"),
        [
            ("terrain", "5.2.1. Les terrains et leur constitution"),
            ("terrain_pierre", "5.2.2. Pierre, roche"),
            ("terrain_terre", "5.2.3. Terre"),
            ("topographie", "5.2.4. Topographie"),
            ("orientation", "5.2.5. Orientation"),
            ("locatif", "5.2.6. Locatifs")
        ],
        ("eau", "5.3. Eau (eau douce mer)"),
        ("matière", "5.4. Matière, matériaux"),
        ("lumière", "5.5. Lumière")
    ],
    ("TITLE 1", "6. Zoologie"),
    [
        ("oiseau", "6.1. Oiseaux"),
        ("TITLE 2", "6.2. Mammifères"),
        [
            ("mammifères", "6.2.1. Mammifères"),
            ("mammifères marins", "6.2.2. Mammifères marins")
        ],
        ("TITLE 2", "6.3. Reptiles"),
        [
            ("reptile", "6.3.1. Reptiles"),
            ("reptiles marins", "6.3.2. Reptiles marins")
        ],
        ("crustacés", "6.4. Crustacés, crabes"),
        ("échinoderme", "6.5. Echinodermes"),
        ("mollusque", "6.6. Mollusques"),
        ("coquillage", "6.7. Coquillages"),
        ("poisson", "6.8. Poissons"),
        ("anguille", "6.9. Anguilles"),
        ("insecte", "6.10. Insectes")
    ],
    ("TITLE 1", "7. Botanique"),
    [
        ("arbre", "7.1. Arbre"),
        ("TITLE 2", "7.2. Description des végétaux"),
        [
            ("plantes", "7.2.1. Nom des plantes"),
            ("plantes_partie", "7.2.2. Parties de plantes"),
            ("plantes_processus", "7.2.3. Processus")
        ],
        ("arbre_cocotier", "7.3. Cocotiers"),
        ("igname", "7.4. Ignames"),
        ("taro", "7.5. Taros"),
        ("bananier", "7.6. Bananiers et bananes"),
        ("cucurbitacée", "7.7. Cucurbitacées"),
        ("plantes.fruit", "7.8. Fruits")
    ],
    ("TITLE 1", "8. Classificateur"),
    [
        ("classificateur numérique", "8.1. Classificateurs numériques"),
        ("classificateur possessif", "8.2. Classificateurs possessifs"),
        ("classificateur nourriture", "8.3. Classificateurs de la nourriture"),
        ("classificateur sémantique", "8.4. Classificateurs sémantiques")
    ],
    ("quantificateur", "9. Quantificateur"),
    ("TITLE 1", "10. Eléments grammaticaux"),
    [
        ("grammaire_adverbe", "10.1. Adverbe"),
        ("grammaire_agent", "10.2. Agent"),
        ("grammaire_article", "10.3. Article"),
        ("grammaire_article_indéfini", "10.4. Article indéfini"),
        ("grammaire_aspect", "10.5. Aspect"),
        ("grammaire_aspect_modalité", "10.6. Aspect, modalité"),
        ("grammaire_assertif", "10.7. Assertif"),
        ("grammaire_but", "10.8. But"),
        ("grammaire_causatif", "10.9. Causatif"),
        ("grammaire_collectif", "10.10. Collectif"),
        ("grammaire_comparaison", "10.11. Comparaison"),
        ("grammaire_conjonction", "10.12. Conjonction"),
        ("grammaire_contraste", "10.13. Contraste"),
        ("grammaire_démonstratif", "10.14. Démonstratif"),
        ("grammaire_dérivation", "10.15. Dérivation"),
        ("grammaire_déterminant_duel", "10.16. Déterminant duel"),
        ("grammaire_direction", "10.17. Direction"),
        ("grammaire_directionnel", "10.18. Directionnel"),
        ("discours_interjection", "10.19. Discours interjection"),
        ("grammaire_distributif", "10.20. Distributif"),
        ("grammaire_existentiel", "10.21. Existentiel"),
        ("grammaire_injonction", "10.22. Injonction"),
        ("grammaire_intensificateur", "10.23. Intensificateur"),
        ("grammaire_interjection", "10.24. Interjection"),
        ("grammaire_interpellation", "10.25. Interpellation"),
        ("grammaire_interrogatif", "10.26. Interrogatif"),
        ("grammaire_IS", "10.27. IS"),
        ("grammaire_locatif", "10.28. Locatif"),
        ("grammaire_marque_sujet", "10.29. Marque sujet"),
        ("grammaire_marque_transitive", "10.30. Marque transitive"),
        ("grammaire_modalité", "10.31. Modalité"),
        ("grammaire_négation", "10.32. Négation"),
        ("grammaire_négation_existentiel", "10.33. Négation existentiel"),
        ("grammaire_nombre", "10.34. Nombre"),
        ("grammaire_numéral", "10.35. Numéral"),
        ("grammaire_ordinal", "10.36. Ordinal"),
        ("grammaire_parenté", "10.37. Parenté"),
        ("grammaire_possession", "10.38. Possession"),
        ("grammaire_préfixe", "10.39. Préfixe"),
        ("grammaire_préposition", "10.40. Préposition"),
        ("grammaire_présentatif", "10.41. Présentatif"),
        ("grammaire_pronom", "10.42. Pronom"),
        ("grammaire_pronom_négatif", "10.43. Pronom négatif"),
        ("grammaire_propriété", "10.44. Propriété"),
        ("grammaire_quantificateur", "10.45. Quantificateur"),
        ("grammaire_quantificateur_degré", "10.46. Quantificateur degré"),
        ("grammaire_quantification", "10.47. Quantification"),
        ("grammaire_réciproque", "10.48. Réciproque"),
        ("grammaire_réfléchi", "10.49. Réfléchi"),
        ("grammaire_relateur", "10.50. Relateur"),
        ("grammaire_restrictif", "10.51. Restrictif"),
        ("grammaire_suff.trans.", "10.52. Suff. trans."),
        ("grammaire_temps", "10.53. Temps"),
        ("grammaire_vocatif", "10.54. Vocatif")
    ]
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
def set_ce(ce, lexical_entry):
    related_form = lexical_entry.get_last_related_form()
    if related_form is not None:
        related_form.create_and_add_form_representation(written_form=ce, language=config.xml.French)

def retrieve_dialect_name(text):
    text = text.replace("BO", u"Bondé")
    text = text.replace("PA", "Paimboa")
    text = text.replace("GO(s)", "Gomen Sud")
    text = text.replace("GO(n)", "Gomen Nord")
    text = text.replace("GO", "Gomen")
    text = text.replace("WEM", "WEM")
    text = text.replace("WE", "WE")
    return text

def force_caps(text):
    """Force first letter to be in upper case.
    """
    return text[0].upper() + text[1:]

mdf_lmf.update({
    # dialx : dialecte BO / PA / GO / GO(s) / GO(n) + WEM / WE => OK
    "dialx" : lambda dialx, lexical_entry: lexical_entry.set_usage_note(dialx.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"), language="nua"),
    # empr : emprunt => OK
    "empr"  : lambda empr, lexical_entry: set_bw(empr, lexical_entry),
    # sc : nom scientifique => OK
    "sc"    : lambda sc, lexical_entry: lexical_entry.set_scientific_name(force_caps(sc)),
    # ge : French gloss
    "ge"    : lambda ge, lexical_entry: lexical_entry.set_gloss(force_caps(ge.replace('_', ' ').replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE")), language=config.xml.French),
    # xn : French example
    "xn"    : lambda xn, lexical_entry: lexical_entry.add_example(force_caps(xn), language=config.xml.French),
    # xe : English example
    "xe"    : lambda xe, lexical_entry: lexical_entry.add_example(force_caps(xe), language=config.xml.English),
    # sge : French gloss of the subentry
    "sge"   : lambda sge, lexical_entry: lexical_entry.set_gloss(force_caps(sge), language=config.xml.French),
    # de : French definition
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(force_caps(de), language=config.xml.French),
    # gr : note grammaticale => [Note grammaticale : ] à la suite de [Note : ]
    "gr"    : lambda gr, lexical_entry: lexical_entry.set_note(gr, type="grammar", language=config.xml.regional),
    # gt: traduction de gr en français => [Note grammaticale : 'gr' (en gras) 'gt' (non gras)]
    "gt"    : lambda gt, lexical_entry: lexical_entry.set_note(force_caps(gt), type="grammar", language=config.xml.French),
    # ce : French translation of cf => cf : 'cf' (en gras) 'ce' (non gras)
    "ce"    : lambda ce, lexical_entry: set_ce(force_caps(ce), lexical_entry),
    # nt : note => OK
    "nt"    : lambda nt, lexical_entry: lexical_entry.set_note(nt, type="general"),
    # ng : note grammaticale => OK
    "ng"    : lambda ng, lexical_entry: lexical_entry.set_note(ng, type="grammar", language=config.xml.vernacular),
    # np : note phonologique => OK
    "np"    : lambda np, lexical_entry: lexical_entry.set_note(np, type="phonology"),
    # na : note anthropologique => OK
    "na"    : lambda na, lexical_entry: lexical_entry.set_note(na, type="anthropology"),
    # ve : dialect(s) of variant BO / PA / GO / GO(s) / GO(n) + WEM / WE / vx / BO [BM] / BO (Corne) / BO (Corne, BM)
    "ve"    : lambda ve, lexical_entry: lexical_entry.set_dialect(ve.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE")),
    # xv : vernacular example => OK
    "xv"    : lambda xv, lexical_entry: lexical_entry.create_and_add_example(xv.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"), language=config.xml.vernacular),
    # cf : confer => OK
    "cf"    : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(cf.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"), "simple link")
})

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps = [
    "ACC",

    "adresse honorifique",

    "AGT",
    "AGT ???",

    "ART",
    "ART PL",

    "ADJ",

    "ADV",
    "ADV LOC (spatio-temporel) ANAPH ???",
    "ADV LOC DX2",
    "ADV LOC",
    "ADV QNT",
    "ADV MODIF",
    "ADV ATTEN (ordre) (forme de politesse) ; ponctuel",
    "ADV TIME",
    "ADV SEQ (continuatif)",
    "ADV ???",

    "ANAPH",
    "ANAPH (discours ou passé ???)",
    "ANAPH (discours)",

    "ASSOC",

    "ASP",
    "ASP DUR",
    "ASP ou RESTR",
    "ASP PERS",
    "ASP (itératif)",
    "ASP (révolu)",
    "ASP HAB",
    "ASP ACC",
    "ASP INACC",
    "ASP (post-verbal)",

    "atténuatif ???",

    "BENEF",

    "c",

    "CLF",
    "CLF NUM (morceaux) PA [pas à Gomen]",
    "CLF (multiples)",
    "CLF (armes)",
    "CLF (objets ronds)",
    "CLF (maisons)",
    "CLF NUM (animés)",
    "CLF NUM",
    "CLF NUM (morceaux de bois)",
    "CLF NUM (feuilles)",
    "CLF NUM (tissus et étoffes végétales)",
    "CLF NUM (lots : fête de la nouvelle igname, contexte cérémoniel)",
    "CLF NUM (lots cérémoniels)",
    "CLF NUM (pour compter des paquets d'ignames constitués de trois ignames)",
    "CLF NUM (générique et des objets ronds)",
    "CLF NUM (objets longs)",
    "CLF NUM (bois, arbres, certaines racines comestibles, cordes, objets longs, sagaies, doigts)",

    "CLF POSS",

    "CNJ",
    "CNJ ; THEM",
    "CNJ TIME",
    "CNJ (complémentation)",
    "CNJ HYP",
    "CNJ (but)",
    "CNJ REL",

    "COI",

    "COLL",
    "COLL + PRO",

    "CONN",

    "contraste",
    "contraste ; état",

    "COORD",

    "couple PAR",

    "DEIC",
    "DEIC DIR",
    "DEIC DX3",
    "DEIC PL DX1 ou ANAPH",
    "DEIC PL",
    "DEIC DX1 duel ou ANAPH",
    "DEIC DX3 duel (latéralement)",
    "DEIC DX3 (visible)",

    "DEM",
    "DEM duel",
    "DEM duel ou PL",
    "DEM DX",
    "DEM ANAPH",
    "DEM DX2",
    "DEM DX1",
    "DEM DX3",
    "DEM SG",
    "DEM (médial ou proche)",
    "DEM PL",
    "DEM PL (post-nom)",
    "DEM duel (post-nom)",
    "DEM DIR",
    "DEM DX2 duel et ANAPH",
    "DEM DX2 ; ANAPH ; assertif",
    "DEM DX3 PL",
    "DEM DX3 ou ANAPH",
    "DEM DX3 duel",
    "DEM DX3 DEIC ou ANAPH",
    "DEM DX3 (distal)",
    "DEM DX4",

    "déterminant ; DEM duel",
    "déterminant duel",
    "déterminant ; PRO DEIC DX1",

    "DIR",
    "DIR (transverse)",
    "DIR (ventif)",
    "DIR (centrifuge)",

    "dire du mal de qqn",

    "dispersif ; DISTR",

    "DISTR",

    "doute",

    "duel",

    "DUR",

    "DX1",
    "DX1 ; ANAPH",
    "DX2 ; ANAPH ; ASS",

    "FOC",
    "FOC ; RESTR (antéposé au GN) (za ... nye ...)",

    "forme déterminée de mwa ; PREF (désignant un contenant)",

    "FREQ",

    "FUT",

    "génitif (déterminant non-spécifique, générique ???)",

    "INCH",
    "INCH, en cours",

    "indétermination",

    "INJONC",

    "INT",
    "INT LOC (dynamique)",
    "INT LOC (statique)",
    "INT (statique : humains, PRO, n)",
    "INT (statique)",
    "INT (indéfini)",
    "INT CMPAR",

    "INTENS",
    "INTENS ; assertif (devant le prédicat)",

    "interlocative",

    "interpellation",
    "interpellation ou DEM",

    "INTJ",
    "INTJ (pitié, affection)",
    "INTJ ; v",
    "INTJ ; appel respectueux à une pers.",

    "ITER",

    "LOC",
    "LOC DIR",
    "LOC DX2",
    "LOC DX3",
    "LOC ANAPH",
    "LOC DEIC DX3",
    "LOC ; n",
    "LOC (spatio-temporel)",
    "LOC CMPAR",
    "pré-LOC + LOC",

    "LOCUT",
    "LOCUT ADV",
    "LOCUT INT",

    "MDL",
    "MDL n",
    "MDL INTJ",

    "MODIF",

    "morphème de THEM (nrowö ... ca)",

    "n-fois",

    "n",
    "n (inaliénable)",
    "n ; CLF POSS",
    "n ; PAR REC",
    "n (composition)",
    "n LOC",
    "n BENEF",
    "n ORD",
    "n ; v",
    "n ; v STAT",
    "n ; LOC",
    "n (référence)",
    "n SG",
    "n ; CLF NUM",
    "n QNT",
    "n CNJ",
    "n ; PRO",
    "n LOC (forme POSS de pwamwa)",
    "n LOC ; v",
    "n CMPAR",
    "n (terme d'appellation ou référence)",
    "n INTJ",

    "NEG",
    "NEG (en réponse à une question)",

    "NOMR",

    "NUM",
    "NUM (animés)",
    "NUM ORD",
    "NUM (pour certains types de dons coutumiers)",
    "NUM (pour certains types de dons coutumiers qui se comptent par deux)",
    "NUM (pour certains types de dons coutumiers qui se comptent par deux) Bretteville",

    "objet",

    "ORD",

    "PAR REC ???",
    "PAR REC",

    "passé",

    "POSS (certains lexèmes)",
    "POSS IND",
    "POSS 1° pers. duel incl.",
    "POSS 1° pers. incl.",

    "PRED NEG",
    "PRED NEG (humain)",

    "PREF",
    "PREF (n agent)",
    "PREF (référant à une surface extérieure)",
    "PREF (instrumental, NOMR)",
    "PREF ORD",
    "PREF CLF NUM (mains de banane)",
    "PREF (couples PAR)",
    "PREF (relations duelles)",
    "PREF (indiquant une position couchée)",
    "PREF NOMR",
    "PREF (lieu)",
    "PREF CAUS",
    "PREF REC ; COLL",
    "PREF (position assise)",

    "PREP",
    "PREP (objet indirect)",
    "PREP ; ADV ; CNJ",
    "PREP LOC",
    "PREP (ablatif)",
    "PREP (spatio-temporelle)",
    "PREP BENEF",
    "PREP (instrumentale) ; AGT ???",
    "PREP (régime indirect)",
    "PREP ; CNJ",
    "PREP (instrument)",

    "PRO",
    "PRO 1° pers. incl. (OBJ ou POSS)",
    "PRO 1° pers. excl. PL (sujet)",
    "PRO 1° pers. excl. PL (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 1° pers. triel incl.",
    "PRO 1° pers. SG (sujet ou OBJ)",
    "PRO (OBJ) ou POSS 1° pers. SG",
    "PRO 1° pers. incl. PL (sujet)",
    "PRO 1° pers. triel incl. (sujet)",
    "PRO 1° pers. duel incl. (sujet)",
    "PRO 1° pers. triel excl. (sujet, OBJ ou POSS)",
    "PRO 1° pers. duel excl. (sujet, OBJ ou POSS)",
    "PRO 1° pers. duel excl. (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 1° pers. duel incl.",
    "PRO 1° pers. incl. PL",
    "PRO 1° pers. incl. PL (OBJ ou POSS)",
    "PRO 1° pers. duel incl. (OBJ ou POSS)",
    "PRO 1° pers. SG (OBJ ou POSS)",
    "PRO 1° pers. triel incl. (OBJ ou POSS)",
    "PRO 2° pers. duel (sujet)",
    "PRO 2° pers. SG (sujet ou OBJ)",
    "PRO 2° pers. PL (sujet)",
    "PRO 2° pers. PL",
    "PRO (OBJ) ou POSS 2° pers. duel",
    "PRO 2° pers. SG (sujet, OBJ ou POSS)",
    "PRO (OBJ) ; POSS 2° pers. PL",
    "PRO 2° pers. PL (sujet, OBJ ou POSS)",
    "PRO 2° pers. duel (OBJ ou POSS)",
    "PRO 2° pers. PL (OBJ ou POSS)",
    "PRO 3° pers. SG (sujet)",
    "PRO 3° pers. SG (OBJ)",
    "PRO 3° pers. masc. PL",
    "PRO 3° pers. masc. duel (DX ou ANAPH)",
    "PRO 3° pers. PL (sujet)",
    "PRO 3° pers. PL (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 3° pers. duel",
    "PRO 3° pers. duel (sujet)",
    "PRO 3° pers. triel (sujet, OBJ ou POSS)",
    "PRO 3° pers. duel (OBJ ou POSS)",
    "PRO 3° pers. triel (OBJ ou POSS)",
    "PRO 3° pers. SG (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 3° pers. triel",
    "PRO (OBJ) ou POSS 3° pers. SG",
    "PRO (sujet) (aspiré)",
    "PRO DEIC DX2 (latéral)",
    "PRO DEIC ou ANAPH DX3",
    "PRO DEM PL",
    "PRO DX2 3° pers. masc. SG",
    "PRO DX2 3° pers. masc. PL",
    "PRO DX3 3° pers. masc. PL",
    "PRO DX2 3° pers. fém. PL",
    "PRO DX2 3° pers. PL",
    "PRO DX3 3° pers. fém. PL",
    "PRO DX3 3° pers.",
    "PRO INDEP 1° pers. duel excl.",
    "PRO INDEP 3° pers.",
    "PRO INDEP 2° pers. duel",
    "PRO INDEP 3° pers. PL",
    "PRO INDEP 3° pers. triel ou paucal",
    "PRO INDEP 1° pers. triel excl.",
    "PRO INDEP 1° pers.",
    "PRO INDEP 1° pers. triel incl.",
    "PRO INDEP 1° pers. excl. PL",
    "PRO INDEP 2° pers. PL",
    "PRO INDEP 2° pers. triel",
    "PRO INDEP 2° pers. SG",
    "PRO INDEP 3° pers. duel",
    "PRO INT",
    "PRO NEG",

    "PROH",

    "PTCL MDL (adversatif, hypothétique)",
    "PTCL ASP (post-verbal)",
    "PTCL (assertive)",
    "PTCL ASP",

    "QNT",
    "QNT (réduplication de pe- ???)",
    "QNT DISTR",
    "QNT ; atténuation",
    "QNT ???",

    "REC",

    "REL",
    "REL ou DEM ???",

    "RESTR",
    "RESTR ; ASP",
    "RESTR + NUM",
    "RESTR ???",

    "relateur",

    "REV ; ITER GO(s)",

    "révolu (u ... mwã)",

    "RFLX",

    "saturateur transitif ???",

    "SEQ",

    "sujet ; AGT ???",

    "SUFF DIR",
    "SUFF POSS 1° pers.",
    "SUFF POSS 2° pers.",
    "SUFF POSS 3° pers. SG",
    "SUFF POSS INT",
    "SUFF (transitif)",
    "SUFF NOMR",

    "THEM",
    "THEM (nrowö ... ca)",

    "transition, répétition, réversif",

    "triel",

    "v",
    "vt",
    "vi",
    "v ; MODIF ; INTENS RFLX",
    "v LOC ; progressif",
    "v STAT ; n",
    "v LOC",
    "v ; ASP",
    "v ; PREP",
    "v ; QNT",
    "v ; n",
    "v DIR",
    "v STAT",
    "v MDL",
    "v ; ADV",
    "v STAT ; ADV",
    "v INT",
    "v IMPERS",
    "v STAT ???",
    "v (non-humains)",
    "v (en composition)",
    "v ; n ; CLF POSS",
    "v CMPAR",
    "v ; INTJ",
    "v REC",
    "v ; INTJ ; n",
    "v STAT ; QNT",
    "v STAT ; MODIF",
    "v ASP",
    "v ; ADV",
    "vi ; n",
    "vt (+ PRO pers.)",
    "vt (+ PRO)",
    "v ; n ; CLF NUM",
    "v STAT ; v",
    "v ; n STAT",

    "vocatif",

    "voyelle euphonique",

    "???"
]
for item in ps:
    ps_partOfSpeech.update({item : item.decode(ENCODING)})

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range.update(ps_partOfSpeech.values())

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
