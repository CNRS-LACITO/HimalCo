#! /usr/bin/env python
# -*- coding: utf-8 -*-

from defs import CODEC

# Add the repository path before the Python path to use the correct NLTK library
import sys
sys.path.insert(1, "../lib/nltk/nltk-develop")
# Import NLTK Toolbox module
import nltk
from nltk import toolbox as tb

class MdfFormat():
    def __init__(self):
        self.first_element = None
        self.options = None
        self.tree = None

    def process_data(self):
        """NLTK processing.
        """
        data = tb.ToolboxData(filename=self.options.input)
        self.first_element = data.parse(grammar=self.options.grammar, root_label='lxGroup', loop=5, trace=0, encoding=CODEC)
        self.tree = tb.ElementTree(element=self.first_element)
        # Remove all elements and subelements with no text and no child elements
        tb.remove_blanks(self.tree.getroot())
