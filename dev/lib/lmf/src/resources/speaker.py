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
        self.speakerID = None
