#! /usr/bin/env python

"""! @package core
"""

from representation import Representation

class TextRepresentation(Representation):
    """! "Text Representation is a class representing the textual content of definition or statement. When there is more than one variant orthography, the Text Representation instance contains a Unicode string representing the textual content as well as unique attribute-value pairs that describe the specific language, script and orthography." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        TextRepresentation instances are owned by Definition and Statement.
        @return A TextRepresentation instance.
        """
        # Initialize Representation attributes: 'comment', 'writtenForm' and 'language'
        self.__new__()
        self.font = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass
