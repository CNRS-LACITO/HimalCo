#! /usr/bin/env python

from human_resource import HumanResource

"""! @package resources
"""

class Speaker(HumanResource):
    """! Speaker is a HumanResource subclass. The Speaker is a class representing a speaker.
    """
    def __init__(self):
        """! @brief Constructor.
        Speaker instances are owned by LexicalResource.
        @return A Speaker instance.
        """
        # Initialize HumanResource attributes: 'name', 'anonymizationFlag', 'reference' and 'source'
        self.__new__()
        self.speakerID = None
