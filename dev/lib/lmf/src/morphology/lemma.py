#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form

class Lemma(Form):
    """! "Lemma is a Form subclass representing a form chosen by convention to designate the Lexical Entry. The lemma is usually equivalent to one of the inflected forms, the root, stem or compound phrase." (LMF).
    """
    def __init__(self):
        """! @brief Constructor.
        Lemma instance is owned by LexicalEntry.
        @return A Lemma instance.
        """
        # Initialize Form attributes: 'variantForm', 'type' and 'form_representation'
        self.__new__()
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
