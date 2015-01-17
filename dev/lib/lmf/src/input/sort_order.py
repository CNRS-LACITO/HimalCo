#! /usr/bin/env python

"""! @package input
"""

from utils.xml_format import parse_xml
from utils.error_handling import InputError

def sort_order_read(filename):
    """! @brief Read an XML file giving sort order.
    @param filename The name of the XML file to read with full path, for instance 'user/sort_order.xml'.
    @return A Python dictionary of ordered characters.
    """
    order = dict()
    root = parse_xml(filename)
    # Parse XML elements
    for rules in root:
        # XML elements "rules" have 1 XML attribute: "level"
        if rules.tag != "rules":
            raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
        for rule in rules:
            # XML elements "rule" have 2 XML attributes: one for the character ("str"), a second for the rank value ("rank")
            if rule.tag != "rule":
                raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
            order.update({rule.attrib["str"] : float(rule.attrib["rank"])})
    return order
