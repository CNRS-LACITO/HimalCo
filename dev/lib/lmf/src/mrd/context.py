#! /usr/bin/env python

"""! @package mrd
"""

class Context():
    """! "Context is a class representing a text string that provides authentic context for the use of the word form managed by the Lemma. This class is to be distinguished from Sense Example." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Context instances are owned by Sense.
        @return A Context instance.
        """
        self.language = None
        self.type = None
        ## TextRepresentation instances are owned by Context
        # There is zero to many TextRepresentation instances per Context
        self.text_representation = []
        # Speaker id
        self.targets = None
        ## Pointer to an existing Speaker
        # There is zero or one Speaker pointer per Context instance
        self.__speaker = None

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]
        # Decrement the reference count on pointed objects
        self.__speaker = None

    def get_speaker(self):
        """! @brief Get speaker.
        @return Context private attribute '__speaker'.
        """
        return self.__speaker
