#! /usr/bin/env python

"""! @package core
"""

from morphology.lemma import Lemma

class LexicalEntry():
    """! This class represents a lexical entry.
    """
    def __init__(self):
        """! @brief Constructor.
        @return A LexicalEntry instance.
        """
        self.homonymNumber = None
        self.status = None
        self.date = None
        self.partOfSpeech = None
        self.independentWord = None
        self.bibliography = None
        ## Unique IDentifier is managed at the Lexicon level
        self.id = 0
        ## Lemma instance is owned by LexicalEntry
        # There is one Lemma instance by LexicalEntry instance
        self.lemma = None

    def set_partOfSpeech(self, part_of_speech):
        """! @brief Set grammatical category.
        @param part_of_speech The grammatical category to set.
        @return LexicalEntry instance.
        """
        self.partOfSpeech = part_of_speech
        return self

    def get_partOfSpeech(self):
        """! @brief Get grammatical category.
        @return LexicalEntry attribute 'partOfSpeech'.
        """
        return self.partOfSpeech

    def set_status(self, status):
        """! @brief Set lexical entry status.
        @param status The status to set.
        @return LexicalEntry instance.
        """
        self.status = status
        return self

    def get_status(self):
        """! @brief Get lexical entry status.
        @return LexicalEntry attribute 'status'.
        """
        return self.status

    def get_id(self):
        """! @brief Get Unique IDentifier.
        @return LexicalEntry attribute 'id'.
        """
        return self.id

    def set_lexeme(self, lexeme):
        """! @brief Set lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @param lexeme The lexeme to set.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_lexeme(lexeme)
        return self

    def get_lexeme(self):
        """! @brief Get lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @return Lemma attribute 'lexeme' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_lexeme()
        else:
            return None
