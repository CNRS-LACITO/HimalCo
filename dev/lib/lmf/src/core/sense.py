#! /usr/bin/env python

"""! @package core
"""

from core.definition import Definition

class Sense():
    """! "Sense is a class representing one meaning of a lexical entry. The Sense class allows for hierarchical senses in that a sense may be more specific than another sense of the same lexical entry." (LMF)
    """
    def __init__(self, id=0):
        """! @brief Constructor.
        Sense instances are owned by LexicalEntry.
        @param id IDentifier. If not provided, default value is 0.
        @return A Sense instance.
        """
        self.senseNumber = None
        # ID is managed at the LexicalEntry level
        self.id = id
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
        ## Paradigm instances are owned by Sense
        # There is zero to many Paradigm instances per Sense
        self.paradigm = []

    def __del__(self):
        """! @brief Destructor.
        Release Definition, Sense, Equivalent, Context, SubjectField, Paradigm instances.
        """
        for definition in self.definition:
            del definition
        del self.definition[:]
        for sense in self.sense:
            del sense
        del self.sense[:]
        for equivalent in self.equivalent:
            del equivalent
        del self.equivalent[:]
        for context in self.context:
            del context
        del self.context[:]
        for subject_field in self.subject_field:
            del subject_field
        del self.subject_field[:]
        for paradigm in self.paradigm:
            del paradigm
        del self.paradigm[:]

    def get_id(self):
        """! @brief IDentifier.
        @return Sense attribute 'id'.
        """
        return self.id

    def set_senseNumber(self, sense_number):
        """! @brief Set sense number.
        @param sense_number The sense number to set.
        @return Sense instance.
        """
        self.senseNumber = sense_number
        return self

    def get_senseNumber(self):
        """! @brief Get sense number.
        @return Sense attribute 'senseNumber'.
        """
        return self.senseNumber

    def create_definition(self):
        """! @brief Create a definition.
        @return Definition instance.
        """
        return Definition()

    def add_definition(self, definition):
        """! @brief Add a definition to the sense.
        @param definition The Definition instance to add to the sense.
        @return Sense instance.
        """
        self.definition.append(definition)
        return self

    def get_definitions(self):
        """! @brief Get all definitions maintained by the sense.
        @return A Python list of definitions.
        """
        return self.definition

    def get_last_definition(self):
        """! @brief Get the previously registered Definition instance.
        @return The last element of Sense attribute 'definition'.
        """
        if len(self.get_definitions()) >= 1:
            return self.get_definitions()[-1]

    def find_definitions(self, language):
        """! @brief Find definitions.
        This attribute is owned by Definition.
        @param language The language to consider to retrieve the definition.
        @return A Python list of found Definition attributes 'definition'.
        """
        found_definitions = []
        for definition in self.get_definitions():
            if definition.get_language() == language and definition.get_definition() is not None:
                found_definitions.append(definition.get_definition())
        return found_definitions

    def set_definition(self, definition, language=None):
        """! @brief Set definition and language.
        These attributes are owned by Definition.
        @param definition Definition.
        @param language Language of definition.
        @return Sense instance.
        """
        instance = None
        # Find if there is a Definition instance with this language without definition
        for inst in self.get_definitions():
            if inst.get_language() == language and inst.get_definition() is None:
                # Found the Definition instance to set
                instance = inst
                break
        if instance is None:
            # Set first Definition instance that has no definition nor language
            for inst in self.get_definitions():
                if inst.get_language() is None and inst.get_definition() is None:
                    # Found the Definition instance to set
                    instance = inst
                    break
        if instance is None:
            # Create a Definition instance
            instance = self.create_definition()
            self.add_definition(instance)
        instance.set_definition(definition, language)
        return self

    def find_glosses(self, language):
        """! @brief Find glosses.
        This attribute is owned by Definition.
        @param language The language to consider to retrieve the gloss.
        @return A Python list of found Definition attributes 'gloss'.
        """
        found_glosses = []
        for definition in self.get_definitions():
            if definition.get_language() == language and definition.get_gloss() is not None:
                found_glosses.append(definition.get_gloss())
        return found_glosses

    def set_gloss(self, gloss, language=None):
        """! @brief Set gloss and language.
        These attributes are owned by Definition.
        @param gloss Gloss.
        @param language Language of gloss.
        @return Sense instance.
        """
        instance = None
        # Find if there is a Definition instance with this language without gloss
        for inst in self.get_definitions():
            if inst.get_language() == language and inst.get_gloss() is None:
                # Found the Definition instance to set
                instance = inst
                break
        if instance is None:
            # Set first Definition instance that has no gloss nor language
            for inst in self.get_definitions():
                if inst.get_language() is None and inst.get_gloss() is None:
                    # Found the Definition instance to set
                    instance = inst
                    break
        if instance is None:
            # Create a Definition instance
            instance = self.create_definition()
            self.add_definition(instance)
        instance.set_gloss(gloss, language)
        return self

    def set_note(self, note, type=None, language=None):
        """! @brief Set note, note type and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param note Note to set.
        @param type Type of the note.
        @param language Language used for the note.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_note(note, type, language)
        return self

    def find_notes(self, type):
        """! @brief Find notes.
        This attribute is owned by Statement, which owned by Definition.
        @param type Type of the note to consider to retrieve the note.
        @return A Python list of found Statement attributes 'notes'.
        """
        found_notes = []
        for definition in self.get_definitions():
            found_notes += definition.find_notes(type)
        return found_notes

    def set_usage_note(self, usage_note, language=None):
        """! @brief Set usage note and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param usage_note Usage note to set.
        @param language Language used for the usage note.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_usage_note(usage_note, language)
        return self

    def find_usage_notes(self, language):
        """! @brief Find usage notes.
        This attribute is owned by Statement, which owned by Definition.
        @param language Language to consider to retrieve the usage note.
        @return A Python list of found Statement attributes 'usageNote'.
        """
        found_notes = []
        for definition in self.get_definitions():
            found_notes += definition.find_usage_notes(language)
        return found_notes

    def set_encyclopedic_information(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language used for the encyclopedic information.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_encyclopedic_information(encyclopedic_information, language)
        return self

    def find_encyclopedic_informations(self, language):
        """! @brief Find encyclopedic informations.
        This attribute is owned by Statement, which owned by Definition.
        @param language Language to consider to retrieve the encyclopedic informations.
        @return A Python list of found Statement attributes 'encyclopedicInformation'.
        """
        found_informations = []
        for definition in self.get_definitions():
            found_informations += definition.find_encyclopedic_informations(language)
        return found_informations

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param restriction Restriction to set.
        @param language Language used for the restriction.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_restriction(restriction, language)
        return self

    def find_restrictions(self, language):
        """! @brief Find restrictions.
        This attribute is owned by Statement, which owned by Definition.
        @param language Language to consider to retrieve the restriction.
        @return A Python list of found Statement attributes 'restriction'.
        """
        found_restrictions = []
        for definition in self.get_definitions():
            found_restrictions += definition.find_restrictions(language)
        return found_restrictions

    def set_borrowed_word(self, borrowed_word):
        """! @brief Set source language (in English).
        Attribute 'borrowedWord' is owned by Statement, which is owned by Definition.
        @param borrowed_word Source language.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_borrowed_word(borrowed_word)
        return self

    def get_borrowed_word(self):
        """! @brief Get source language (in English).
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'borrowedWord'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get borrowed word
        if definition is not None:
            return definition.get_borrowed_word()

    def set_written_form(self, written_form):
        """! @brief Set loan word.
        Attribute 'writtenForm' is owned by Statement, which is owned by Definition.
        @param written_form Loan word.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_written_form(written_form)
        return self

    def get_written_form(self):
        """! @brief Get loan word.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'writtenForm'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get loan word
        if definition is not None:
            return definition.get_written_form()

    def set_etymology(self, etymology):
        """! @brief Set etymology.
        Attribute 'etymology' is owned by Statement, which is owned by Definition.
        @param etymology Etymology.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology(etymology)
        return self

    def get_etymology(self):
        """! @brief Get etymology.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'etymology'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology
        if definition is not None:
            return definition.get_etymology()

    def set_etymology_comment(self, etymology_comment, term_source_language=None):
        """! @brief Set etymology comment and language.
        Attributes 'etymologyComment' and 'termSourceLanguage' are owned by Statement, which is owned by Definition.
        @param etymology_comment Etymology comment.
        @param term_source_language Language of the comment.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology_comment(etymology_comment, term_source_language)
        return self

    def get_etymology_comment(self, term_source_language=None):
        """! @brief Get etymology comment.
        This attribute is owned by Statement, which is owned by Definition.
        @param term_source_language The language of the etymology comment to retrieve.
        @return Statement attribute 'etymologyComment'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology comment
        if definition is not None:
            return definition.get_etymology_comment(term_source_language)

    def get_term_source_language(self):
        """! @brief Get language used for the etymology comment.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'termSourceLanguage'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology comment language
        if definition is not None:
            return definition.get_term_source_language()

    def set_etymology_gloss(self, etymology_gloss):
        """! @brief Set etymology gloss.
        Attribute 'etymologyGloss' is owned by Statement, which is owned by Definition.
        @param etymology_gloss Etymology gloss.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology_gloss(etymology_gloss)
        return self

    def get_etymology_gloss(self):
        """! @brief Get etymology gloss.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'etymologyGloss'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology gloss
        if definition is not None:
            return definition.get_etymology_gloss()

    def set_etymology_source(self, etymology_source):
        """! @brief Set etymology source.
        Attribute 'etymologySource' is owned by Statement, which is owned by Definition.
        @param etymology_source Etymology source.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology_source(etymology_source)
        return self

    def get_etymology_source(self):
        """! @brief Get etymology source.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'etymologySource'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology source
        if definition is not None:
            return definition.get_etymology_source()
