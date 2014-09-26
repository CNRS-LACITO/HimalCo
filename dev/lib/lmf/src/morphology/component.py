#! /usr/bin/env python

"""! @package morphology
"""

class Component():
    def __init__(self):
        """! @brief Constructor.
        Component instances are owned by ListOfComponents.
        @return A Component instance.
        """
        self.position = None
        # Composed LexicalEntry lexeme
        self.targets = None
        ## Pointer to an existing LexicalEntry
        # There is one LexicalEntry pointer by Component instance
        self.__lexical_entry = None

    def get_lexical_entry(self):
        """! @brief Get pointed lexical entry.
        @return Component private attribute '__lexical_entry'.
        """
        return self.__lexical_entry
