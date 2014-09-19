#! /usr/bin/env python

class LexicalResource():
    def __init__(self):
        self.dtdVersion = None
        ## GlobalInformation instance is owned by LexicalResource
        # There is one GlobalInformation for one LexicalResource
        self.global_information = None
        ## Lexicon instances are owned by LexicalResource
        # There is one or more Lexicon instances for one unique LexicalResource
        self.lexicon = []
