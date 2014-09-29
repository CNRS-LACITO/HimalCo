#! /usr/bin/env python

"""! @package mrd
"""

class Equivalent():
    """! "Equivalent is a class representing the translation equivalent of the word form managed by the Lemma class." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Equivalent instances are owned by Sense.
        @return An Equivalent instance.
        """
        self.language = None
        self.translation = None
        ## TextRepresentation instances are owned by Equivalent
        # There is zero to many TextRepresentation instances per Equivalent
        self.text_representation = []

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]
