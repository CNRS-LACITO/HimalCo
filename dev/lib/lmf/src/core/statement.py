#! /usr/bin/env python

"""! @package core
"""

class Statement():
    """! "Statement is a class representating a narrative description that refines or complements Definition." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Statement instances are owned by Definition.
        @return A Statement instance.
        """
        self.noteType = None
        self.note = None
        self.language = None
        self.encyclopedicInformation = None
        self.usageNote = None
        self.restriction = None
        self.derivation = None
        self.borrowedWord = None
        self.writtenForm = None
        self.sense = None
        self.etymology = None
        self.etymologyComment = None
        self.etymologyGloss = None
        self.etymologySource = None
        self.termSourceLanguage = None
        self.targetLexicalEntry = None
        self.scientificName = None
        ## TextRepresentation instances are owned by Statement
        # There is zero to many TextRepresentation instances per Statement
        self.text_representation = []
