#! /usr/bin/env python

"""! @package core
"""

from utils.attr import check_attr_type

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

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation and Statement instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]
        for statement in self.statement:
            del statement
        del self.statement[:]

    def set_language(self, language):
        """! @brief Set language used for definition and gloss.
        @param language Language used for definition and gloss.
        @return Definition instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        # Check value
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for definition and gloss.
        @return Definition attribute 'language'.
        """
        return self.language

    def set_definition(self, definition, language=None):
        """! @brief Set definition.
        @param definition Definition.
        @param language Language used for the definition.
        @return Definition instance.
        """
        self.definition = definition
        if language is not None:
            self.set_language(language)
        return self

    def get_definition(self, language=None):
        """! @brief Get definition.
        @param language If this argument is given, get definition only if written in this language.
        @return The filtered Definition attribute 'definition'.
        """
        if language is None:
            return self.definition
        if self.language == language:
            return self.definition

    def set_gloss(self, gloss, language=None):
        """! @brief Set gloss.
        @param gloss Gloss.
        @param language Language used for the gloss.
        @return Definition instance.
        """
        self.gloss = gloss
        if language is not None:
            self.set_language(language)
        return self

    def get_gloss(self, language=None):
        """! @brief Get gloss.
        @param language If this argument is given, get gloss only if written in this language.
        @return The filtered Definition attribute 'gloss'.
        """
        if language is None:
            return self.gloss
        if self.language == language:
            return self.gloss
