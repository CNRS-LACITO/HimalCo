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
        self.dtdVersion = 16
        ## GlobalInformation instance is owned by LexicalResource
        # There is one GlobalInformation for one LexicalResource
        self.global_information = None
        ## Lexicon instances are owned by LexicalResource
        # There is one or more Lexicon instances for one unique LexicalResource
        self.lexicon = []
        ## Speaker instances are owned by LexicalResource
        # There is zero to many Speaker instances for one unique LexicalResource
        self.speaker = []

    def __del__(self):
        """! @brief Destructor.
        Release GlobalInformation, Lexicon, Speaker instances.
        """
        for lexicon in self.lexicon:
            del lexicon
        del self.lexicon[:]
        for speaker in self.speaker:
            del speaker
        del self.speaker[:]
        if self.global_information is not None:
            del self.global_information

    def get_lexicons(self):
        """! @brief Get all lexicons maintained by the lexical resource.
        @return A Python list of lexicons.
        """
        return self.lexicon

    def add_lexicon(self, lexicon):
        """! @brief Add a lexicon to the lexical resource.
        @param lexicon A Lexicon instance to add to the Lexical Resource.
        @return Lexical Resource instance.
        """
        self.lexicon.append(lexicon)
        return self

    def remove_lexicon(self, lexicon):
        """! @brief Remove a lexicon from the lexical resource.
        @param lexicon The Lexicon instance to remove from the Lexical Resource.
        @return Lexical Resource instance.
        """
        self.lexicon.remove(lexicon)
        return self
