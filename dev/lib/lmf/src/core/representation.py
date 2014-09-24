#! /usr/bin/env python

"""! @package core
"""

class Representation():
    """! "Representation class is an abstract class representing a Unicode string as well as, if needed, the unique attribute-value pairs that describe the specific language, script and orthography." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        @return A Representation instance.
        """
        self.comment = None
        self.writtenForm = None
        self.language = None
