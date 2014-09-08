#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form

class Lemma(Form):
    """! This class represents a lemma.
    """
    def __init__(self):
        """! @brief Constructor.
        @return A Lemma instance.
        """
        self.hyphenation = None
        self.lexeme = None

    def set_lexeme(self, lexeme):
        """! @brief Set lexeme.
        @param lexeme The lexeme to set.
        @return Lemma instance.
        """
        self.lexeme = lexeme
        return self

    def get_lexeme(self):
        """! @brief Get lexeme.
        @return Lemma attribute 'lexeme'.
        """
        return self.lexeme
