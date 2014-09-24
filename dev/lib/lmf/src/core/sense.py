#! /usr/bin/env python

"""! @package core
"""

class Sense():
    """! "Sense is a class representing one meaning of a lexical entry. The Sense class allows for hierarchical senses in that a sense may be more specific than another sense of the same lexical entry." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Sense instances are owned by LexicalEntry.
        @return A Sense instance.
        """
        self.senseNumber = None
        self.id = None
        ## Definition instances are owned by Sense
        # There is zero to many Definition instances per Sense
        self.definition = []
        ## Sense instances are owned by Sense
        # There is zero to many Sense instances per Sense
        self.sense = []
        ## Equivalent instances are owned by Sense
        # There is zero to many Equivalent instances per Sense
        self.equivalent = []
        ## Context instances are owned by Sense
        # There is zero to many Context instances per Sense
        self.context = []
        ## SubjectField instances are owned by Sense
        # There is zero to many SubjectField instances per Sense
        self.subject_field = []
