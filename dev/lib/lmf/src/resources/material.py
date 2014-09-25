#! /usr/bin/env python

from resource import Resource

"""! @package resources
"""

class Material(Resource):
    """! Material is a Resource subclass. Material is an abstract class representing an audiovisual resource: an audio recording, a picture or a video. The Material class allows subclasses.
    """
    def __init__(self):
        """! @brief Constructor.
        Material instances are owned by FormRepresentation.
        @return A Material instance.
        """
        self.mediaType = None
        self.fileName = None
        self.author = None
