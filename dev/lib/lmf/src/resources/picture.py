#! /usr/bin/env python

from material import Material

class Picture(Material):
    def __init__(self):
        self.filename = None
        self.reference = None
        self.width = None
        self.height = None
        self.format = None
