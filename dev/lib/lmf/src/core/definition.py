#! /usr/bin/env python

"""! @package core
"""

class Definition():
    """! "Definition is a class representing a narrative description of a sense. It is provided to help human users understand the meaning of a lexical entry. A Sense instance can have zero to many definitions. Each Definition instance may be associated with zero to many Text Representation instances in order to manage the text defintion in more than one language or script. In addition, the narrative description can be expressed in a different language or script than the one in the Lexical Entry instance." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Definition instances are owned by Sense.
        @return A Definition instance.
        """
        self.language = None
        self.definition = None
        self.gloss = None
        self.literally = None
        ## TextRepresentation instances are owned by Definition
        # There is zero to many TextRepresentation instances per Definition
        self.text_representation = []
        ## Statement instances are owned by Definition
        # There is zero to many Statement instances per Definition
        self.statement = []
