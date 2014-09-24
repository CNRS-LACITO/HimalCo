#! /usr/bin/env python

"""! @package core
"""

class LexicalResource():
    """! "Lexical Resource is a class representing the entire resource and is a container for one or more lexicons. There is only one Lexical Resource instance." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        @return A LexicalResource instance.
        """
        self.dtdVersion = None
        ## GlobalInformation instance is owned by LexicalResource
        # There is one GlobalInformation for one LexicalResource
        self.global_information = None
        ## Lexicon instances are owned by LexicalResource
        # There is one or more Lexicon instances for one unique LexicalResource
        self.lexicon = []
