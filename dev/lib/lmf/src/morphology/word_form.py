#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form

class WordForm(Form):
    """! "Word Form is a Form subclass representing a form that a lexeme can take when used in a sentence or a phrase." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        WordForm instances are owned by LexicalEntry.
        @return A WordForm instance.
        """
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
