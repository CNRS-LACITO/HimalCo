#! /usr/bin/env python

"""! @package core
"""

class GlobalInformation():
    """! "Global Information is a class for administrative information and other general attributes, such as /language coding/ or /script coding/, which are valid for the entire lexical resource." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        GlobalInformation instance is owned by LexicalResource.
        @return A GlobalInformation instance.
        """
        self.languageCode = None
        self.author = None
        self.version = None
        self.lastUpdate = None
        self.license = None
        self.characterEncoding = None
        self.dateCoding = None
        self.creationDate = None
        self.projectName = None
        self.description = None
        self.bibliographicCitation = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass
