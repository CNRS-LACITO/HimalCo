#! /usr/bin/env python

from core.form import Form

class WordForm(Form):
    def __init__(self):
        self.grammaticalNumber = None
        self.grammaticalGender = None
        self.person = None
        self.anymacy = None
        self.clusivity = None
        self.tense = None
        self.case = None
        self.degree = None
        self.voice = None
        self.verbFormMood = None
