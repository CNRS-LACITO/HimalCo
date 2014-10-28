#! /usr/bin/env python

"""! @package core
"""

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
