#! /usr/bin/env python

"""! @package core
"""

from core.global_information import GlobalInformation
from utils.error_handling import Error

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
        self.global_information = GlobalInformation()
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

    def set_creationDate(self, date):
        """! @brief Set creation date.
        Attribute 'creationDate' is owned by GlobalInformation.
        @param date The date to set, in format YYYY-MM-DD.
        """
        try:
            self.global_information.set_creationDate(date)
            return self
        except Error as exception:
            exception.handle()

    def get_creationDate(self):
        """! @brief Get creation date.
        Attribute 'creationDate' is owned by GlobalInformation.
        @return GlobalInformation attribute 'creationdDate'.
        """
        return self.global_information.get_creationDate()

    def set_lastUpdate(self, date):
        """! @brief Set last update.
        Attribute 'lastUpdate' is owned by GlobalInformation.
        @param date The date to set, in format YYYY-MM-DD.
        """
        try:
            self.global_information.set_lastUpdate(date)
            return self
        except Error as exception:
            exception.handle()

    def get_lastUpdate(self):
        """! @brief Get last update.
        Attribute 'lastUpdate' is owned by GlobalInformation.
        @return GlobalInformation attribute 'lastUpdate'.
        """
        return self.global_information.get_lastUpdate()

    def set_author(self, author):
        """! @brief Set author.
        Attribute 'author' is owned by GlobalInformation.
        @param author The author's name to set.
        """
        self.global_information.set_author(author)
        return self

    def get_author(self):
        """! @brief Get author.
        Attribute 'author' is owned by GlobalInformation.
        @return GlobalInformation attribute 'author'.
        """
        return self.global_information.get_author()

    def set_description(self, description):
        """! @brief Set description.
        Attribute 'description' is owned by GlobalInformation.
        @param description The description to set.
        """
        self.global_information.set_description(description)
        return self

    def get_description(self):
        """! @brief Get description.
        Attribute 'description' is owned by GlobalInformation.
        @return GlobalInformation attribute 'description'.
        """
        return self.global_information.get_description()

    def get_bibliographicCitation(self):
        """! @brief Get bibliographic citation.
        Attribute 'bibliographicCitation' is owned by GlobalInformation.
        @return GlobalInformation attribute 'bibliographicCitation'.
        """
        return self.global_information.get_bibliographicCitation()
