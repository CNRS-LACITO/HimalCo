#! /usr/bin/env python

from utils.io import open_write

try:
    from xml.etree.cElementTree import Element, SubElement, parse, dump, ElementTree, fromstring, tostring, XML
except ImportError:
    from xml.etree.ElementTree import Element, SubElement, parse, dump, ElementTree, fromstring, tostring, XML

def prettify(element):
    """! @brief Return a pretty-printed XML string for the given XML element.
    @param element An XML element.
    @return A Python string containing the printed version of the XML element.
    """
    from xml.dom import minidom
    rough_string = tostring(element, 'UTF-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def write_result(element, filename, encoding=None):
    """! @brief Write an XML element into a pretty XML output file.
    @param element An XML element.
    @param filename The name of the XML file to write with full path, for instance 'user/output.xml'.
    @param encoding Encoding mode. Default value is None.
    """
    unicode_str = prettify(element)
    output_file = open_write(filename, encoding=encoding)
    output_file.write(unicode_str)
    output_file.close()

def parse_xml(filename):
    """! @brief Parse an XML file.
    @param filename The name of the XML file to parse with full path, for instance 'user/input.xml'.
    @return The root XML element.
    """
    tree = parse(filename)
    root = tree.getroot()
    return root
