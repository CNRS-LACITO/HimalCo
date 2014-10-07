#! /usr/bin/env python

from utils.xml_format import write_result, Element, SubElement

def xml_lmf_write(object, filename):
    """! @brief Write an XML LMF file.
    @param object The LMF instance to write as XML.
    @param filename The name of the XML LMF file to write with full path, for instance 'user/output.xml'.
    """
    # Create the root XML element
    root = Element(object.__class__.__name__)
    # Create all XML sub-elements
    build_sub_elements(object, root)
    # Write all created XML elements in the output file
    write_result(root, filename)

def build_sub_elements(object, element):
    """! @brief Create XML sub-elements to an existing XML element by parsing an LMF object instance.
    @param object An LMF object instance.
    @param element XML element for which sub-elements have to be created according to LMF object attributes.
    """
    # Parse instance attributes
    for item in object.__dict__.items():
        attr_name = item[0]
        attr_value = item[1]
        # For each defined public attribute, create an XML sub-element
        if not attr_name.startswith('_'):
            if attr_value is not None:
                # Check if the attribute is itself a class instance
                if type(attr_value) is list:
                    # We suppose that a list always contains objects
                    for item in attr_value:
                        sub_element = SubElement(element, item.__class__.__name__)
                        build_sub_elements(item, sub_element)
                elif type(attr_value) not in [int, str, unicode]:
                    # If this is the case, create an XML element and restart the same operation recursively on this object
                    sub_element = SubElement(element, attr_value.__class__.__name__)
                    build_sub_elements(attr_value, sub_element)
                elif attr_name in ["dtdVersion", "id", "targets"]:
                    # If this is a specical attribute ("id" or "targets"), it must be inserted as an XML element attribute
                    element.attrib.update({attr_name: str(attr_value)})
                else:
                    # In all other cases, an XML sub-element must be created with the keyword name "feat"
                    SubElement(element, "feat", att=attr_name, val=str(attr_value))
