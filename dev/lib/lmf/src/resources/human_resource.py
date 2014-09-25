#! /usr/bin/env python

from resource import Resource

"""! @package resources
"""

class HumanResource(Resource):
    """! HumanResource is a Resource subclass. HumanResource is an abstract class representing a speaker. The HumanResource class allows subclasses.
        """
    def __init__(self):
        """! @brief Constructor.
        HumanResource instances are owned by LexicalResource.
        @return A HumanResource instance.
        """
        self.name = None
        self.anonymizationFlag = None # boolean
        self.reference = None
        self.source = None
