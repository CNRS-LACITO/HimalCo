#! /usr/bin/env python

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range = set([
    "adjective",
    "adposition",
    "adverb",
    "conjunction",
    "determiner",
    "interjection",
    "noun",
    "numeral",
    "particle",
    "pronoun",
    "verb",
    "ideophone",
    "transitive verb",
    "intransitive verb",
    "reflexive verb",
    "negation",
    "impersonal verb",
    "classifier",
    "preposition",
    "bitransistive verb",
    "affix",
    "possessive pronouns",
    "particle",
    "onomatope",
    "function word",
    "stative intransitive verb",
    "linker"
])

## Possible values allowed for LMF variant type FormRepresentation attribute
type_variant_range = set([
    "unspecified",
    "orthography",
    "phonetics",
    "archaic"
])

## Possible values allowed for LMF note type Statement attribute
noteType_range = set([
    "comparison",
    "history",
    "semantics",
    "tone",
    "derivation",
    "case",
    "subord",
    "usage",
    "comment",
    "legend",
    "restriction",
    "encyclopedic",
    "anthropology",
    "discourse",
    "grammar",
    "phonology",
    "question",
    "sociolinguistics",
    "general"
])

## Possible values allowed for LMF grammatical number WordForm attribute
grammaticalNumber_range = set([
    "collective",
    "dual",
    "paucal",
    "plural",
    "quadrial",
    "singular",
    "trial"
])

## Possible values allowed for LMF grammatical gender WordForm attribute
grammaticalGender_range = set([
    "common gender",
    "feminine",
    "masculine",
    "neuter"
])

## Possible values allowed for LMF grammatical person WordForm attribute
person_range = set([
    "first person",
    "second person",
    "third person"
])

## Possible values allowed for LMF anymacy WordForm attribute
anymacy_range = set([
    "animate",
    "inanimate",
    "other anymacy"
])

## Possible values allowed for LMF clusivity WordForm attribute
clusivity_range = set([
    "inclusive",
    "exclusive"
])

## Possible values allowed for LMF grammatical tense WordForm attribute
tense_range = set([
    "future",
    "imperfect",
    "past",
    "present"
])

## Possible values allowed for LMF voice WordForm attribute
voice_range = set([
    "active voice",
    "middle voice",
    "passive voice"
])

## Possible values allowed for LMF verb form mood WordForm attribute
verbFormMood_range = set([
    "gerundive",
    "imperative",
    "indicative",
    "infinitive",
    "participle",
    "subjunctive",
    "conditional",
    "relative mood",
    "prohibitive mood",
    "debitive mood"
])

## Possible values allowed for LMF degree WordForm attribute
degree_range = set([
    "comparative degree",
    "positive degree",
    "superlative degree"
])

## Possible values allowed for semantic relation RelatedForm attribute
semanticRelation_range = set([
    "synonym",
    "antonym",
    "homonym",
    "etymology",
    "subentry",
    "main entry",
    "simple link",
    "derived form",
    "root",
    "stem",
    "collocation"
])

## Possible values allowed for paradigm label Paradigm attribute
paradigmLabel_range = set([
    "lexicalized affix",
    "conjugation class",
    "theme of the past", "past stem", # TODO -> japhug
    "comitative", "comitatif", # TODO -> japhug
    "construction",
    "directional", "directionel", # TODO -> japhug
    "irregularity",
    "classifier",
    "emphatic", # TODO -> japhug
    "case", # TODO -> japhug
    "generic negative", # TODO -> japhug
    "perfective stem (1st and 3th persons)" # TODO -> japhug
])

## Possible values allowed for example type Context attribute
type_example_range = set([
    "proverb",
    "locution",
    "example",
    "combination"
])

## Possible values allowed for media type Material attribute
mediaType_range = set([
    "unspecified",
    "unknown",
    "audio",
    "video",
    "document",
    "text",
    "image",
    "drawing"
])

## Possible values allowed for quality Audio attribute
quality_range = set([
    "very low",
    "low",
    "normal",
    "good",
    "very good" # high
])
