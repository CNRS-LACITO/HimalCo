#! /usr/bin/env python

"""! @package core
"""

class Form():
    """! "Form is an abstract class representing a lexeme, a morphological variant of a lexeme or a morph. The Form class allows subclasses." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Form instances are owned by LexicalEntry.
        @return A Form instance.
        """
        self.variantForm = None
        self.type = None
        ## FormRepresentation instances are owned by Form
        # There is zero to many FormRepresentation instances per Form
        self.form_representation = []
