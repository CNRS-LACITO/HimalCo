#! /usr/bin/env python

from resource import Resource

class HumanResource(Resource):
    def __init__(self):
        self.name = None
        self.anonymizationFlag = None
        self.reference = None
        self.source = None
