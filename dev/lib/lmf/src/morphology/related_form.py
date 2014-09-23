#! /usr/bin/env python

from core.form import Form
from common.range import semanticRelation_range

class RelatedForm(Form):
    def __init__(self, lexeme=None):
        # Initialize 'variantForm' and 'type' attributes
        Form.__init__(self)
        self.semanticRelation = None
        # Related LexicalEntry lexeme
        self.targets = lexeme
        ## Pointer to an existing LexicalEntry
        # There is one LexicalEntry pointer by RelatedForm instance
        self.__lexical_entry = None

    def set_semanticRelation(self, semantic_relation):
        """! @brief Set semantic relation.
        @param semantic_relation The semantic relation to set.
        @return RelatedForm instance.
        """
        # Check semantic relation value
        if semantic_relation not in semanticRelation_range:
            raise AttributeError
        self.semanticRelation = semantic_relation
        return self

    def get_semanticRelation(self):
        """! @brief Get semantic relation.
        @return RelatedForm attribute 'semanticRelation'.
        """
        return self.semanticRelation

    def get_lexeme(self):
        """! @brief Get related LexicalEntry lexeme.
        @return RelatedForm attribute 'targets'.
        """
        return self.targets

    def set_lexical_entry(self, lexical_entry):
        """! @brief Set pointer to the related lexical entry instance. This function can only be called once the full dictionary has been parsed.
        @param lexical_entry The related LexicalEntry.
        @return RelatedForm instance.
        """
        self.__lexical_entry = lexical_entry
        return self

    def get_lexical_entry(self):
        """! @brief Get related LexicalEntry.
        @return RelatedForm private attribute '__lexical_entry'.
        """
        return self.__lexical_entry
