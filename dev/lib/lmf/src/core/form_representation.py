#! /usr/bin/env python

"""! @package core
"""

from representation import Representation

class FormRepresentation(Representation):
    """! "Form Representation is a class representing one variant orthography of a Form." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        FormRepresentation instances are owned by Form.
        @return A FormRepresentation instance.
        """
        # Initialize Representation attributes: 'comment', 'writtenForm' and 'language'
        self.__new__()
        self.transliteration = None
        self.tone = None
        self.geographicalVariant = None
        self.phoneticForm = None
        self.contextualVariation = None
        self.spellingVariant = None
        self.citationForm = None
        self.dialect = None
        self.language = None
        self.scriptName = None
        ## Audio instances are owned by FormRepresentation
        # There is zero to many Audio instances per FormRepresentation
        self.audio = []
        # Speaker id
        self.targets = None
        ## Pointers to an existing Speaker
        # There is zero to many pointers per FormRepresentation instance
        self.__speaker = []

    def get_speakers(self):
        """! @brief Get speakers.
        @return FormRepresentation private attribute '__speaker', a Python list of Speaker instances.
        """
        return self.__speaker
