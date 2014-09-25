#! /usr/bin/env python

"""! @package morphosyntax
"""

class Paradigm():
    """! Paradigm is a class representing a morphological paradigm.
    """
    def __init__(self):
        """! @brief Constructor.
        Paradigm instances are owned by Sense.
        @return A Paradigm instance.
        """
        self.paradigmLabel = None
        self.paradigm = None
        self.language = None
        self.morphology = None
        ## Pointer to an existing LexicalEntry
        # There is zero or one LexicalEntry pointer per Paradigm instance
        self.__lexical_entry = None
