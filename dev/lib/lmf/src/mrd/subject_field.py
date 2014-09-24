#! /usr/bin/env python

"""! @package mrd
"""

class SubjectField():
    """! "Subject Field is a class representing a text string that provides domain or status information." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        SubjectField instances are owned by Sense.
        @return A SubjectField instance.
        """
        self.language = None
        self.semanticDomain = None
        ## SubjectField instances are owned by SubjectField
        # There is zero to many SubjectField instances per SubjectField
        self.subject_field = []
