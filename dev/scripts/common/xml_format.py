#! /usr/bin/env python
# -*- coding: utf-8 -*-

from defs import CODEC
from in_out import InOut

try:
    from xml.etree.cElementTree import dump, fromstring, parse, tostring, XML, Element, ElementTree
except ImportError:
    from xml.etree.ElementTree import dump, fromstring, parse, tostring, XML, Element, ElementTree

class XmlFormat(InOut):
    def __init__(self):
        self.first_element = None
        self.options = None
        self.tree = None

    def dump(self):
        if self.options.verbose:
            dump(self.first_element)

    def prettify(self, element):
        """Return a pretty-printed XML string for the Element.
        """
        from xml.dom import minidom
        rough_string = tostring(element, 'UTF-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="    ")

    def write_xml(self, encoding=CODEC):
        """Write into an XML output file.
        """
        self.tree.write(self.options.output, encoding=encoding)

    def write_result(self, encoding=CODEC):
        """Write into a pretty XML output file.
        """
        unicode_str = self.prettify(self.first_element)
        output = self.open_write(self.options.output, encoding=encoding)
        output.write(unicode_str)
        output.close()

    def display_result(self):
        """Display result.
        """
        print len(self.tree.getroot()) - 1, "record(s)"
        if self.options.verbose:
            for element in self.tree.getroot():
                print element.tag

    def parse_xml(self, filename):
        """Parse XML file.
        """
        tree = parse(filename)
        root = tree.getroot()
        for element in root:
            for subelement in element:
                pass
