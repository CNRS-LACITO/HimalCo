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
