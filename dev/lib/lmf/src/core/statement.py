#! /usr/bin/env python

"""! @package core
"""

from utils.attr import check_attr_type, check_attr_range
from common.range import noteType_range

class Statement():
    """! "Statement is a class representating a narrative description that refines or complements Definition." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Statement instances are owned by Definition.
        @return A Statement instance.
        """
        self.noteType = None
        self.note = None
        self.language = None
        self.encyclopedicInformation = None
        self.usageNote = None
        self.restriction = None
        self.derivation = None
        self.borrowedWord = None
        self.writtenForm = None
        self.sense = None
        self.etymology = None
        self.etymologyComment = None
        self.etymologyGloss = None
        self.etymologySource = None
        self.termSourceLanguage = None
        self.targetLexicalEntry = None
        self.scientificName = None
        ## TextRepresentation instances are owned by Statement
        # There is zero to many TextRepresentation instances per Statement
        self.text_representation = []

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]

    def set_note(self, note, type=None, language=None):
        """! @brief Set note.
        @param note Note to set.
        @param type Type of the note.
        @param language Language used for the note.
        @return Statement instance.
        """
        self.note = note
        if type is not None:
            self.set_noteType(type)
        if language is not None:
            self.set_language(language)
        return self

    def get_note(self, type=None, language=None):
        """! @brief Get note.
        @param type If this argument is given, get note only if its type corresponds.
        @param language If this argument is given, get note only if written in this language.
        @return The filtered Statement attribute 'note'.
        """
        if type is None:
            if language is None or self.get_language() == language:
                return self.note
        elif self.get_noteType() == type:
            if language is None or self.get_language() == language:
                return self.note

    def set_language(self, language):
        """! @brief Set language used for the note.
        @param language Language used for the note.
        @return Statement instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for the note.
        @return Statement attribute 'language'.
        """
        return self.language

    def set_noteType(self, note_type):
        """! @brief Set type of the note.
        @param note_type Type of the note.
        @return Statement instance.
        """
        error_msg = "Note type value '%s' is not allowed" % note_type
        check_attr_type(note_type, [str, unicode], error_msg)
        check_attr_range(note_type, noteType_range, error_msg)
        self.noteType = note_type
        return self

    def get_noteType(self):
        """! @brief Get type of the note.
        @return Statement attribute 'noteType'.
        """
        return self.noteType

    def set_usageNote(self, usage_note, language=None):
        """! @brief Set usage note.
        @param usage_note Usage note to set.
        @param language Language used for the usage note.
        @return Statement instance.
        """
        self.usageNote = usage_note
        if language is not None:
            self.set_language(language)
        return self

    def get_usageNote(self, language=None):
        """! @brief Get usage note.
        @param language If this argument is given, get usage note only if written in this language.
        @return The filtered Statement attribute 'usageNote'.
        """
        if language is None:
            return self.usageNote
        if self.get_language() == language:
            return self.usageNote

    def set_encyclopedicInformation(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language used for the encyclopedic information.
        @return Statement instance.
        """
        self.encyclopedicInformation = encyclopedic_information
        if language is not None:
            self.set_language(language)
        return self

    def get_encyclopedicInformation(self, language=None):
        """! @brief Get encyclopedic information.
        @param language If this argument is given, get encyclopedic information only if written in this language.
        @return The filtered Statement attribute 'encyclopedicInformation'.
        """
        if language is None:
            return self.encyclopedicInformation
        if self.get_language() == language:
            return self.encyclopedicInformation

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction.
        @param restriction Restriction to set.
        @param language Language used for the restriction.
        @return Statement instance.
        """
        self.restriction = restriction
        if language is not None:
            self.set_language(language)
        return self

    def get_restriction(self, language=None):
        """! @brief Get restriction.
        @param language If this argument is given, get restriction only if written in this language.
        @return The filtered Statement attribute 'restriction'.
        """
        if language is None:
            return self.restriction
        if self.get_language() == language:
            return self.restriction
