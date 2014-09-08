#! /usr/bin/env python

from representation import Representation

class FormRepresentation(Representation):
    def __init__(self):
        self.transliteration = None
        self.tone = None
        self.geographicalVariant = None
        self.phoneticForm = None
        self.contextualVariation = None
        self.spellingVariant = None
        self.citationForm = None
        self.dialect = None
        self.language = None
        self.scriptName = None
