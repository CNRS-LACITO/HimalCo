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
