#! /usr/bin/env python

from utils.error_handling import Error

def check_attr_type(val, typ, msg):
    """! @brief Check that attribute value is of specified type.
    @param val The attribute value to check.
    @param typ The allowed Python type(s): simple, or Python set or list.
    @param msg The message to display if value is not of correct type.
    """
    # Python set or list of allowed types
    if type(typ) is set or type(typ) is list:
        if type(val) not in typ:
            raise Error(msg)
    # Simple allowed type
    elif type(val) is not typ:
        raise Error(msg)

def check_attr_range(value, range, msg, mapping=None):
    """! @brief Check that attribute value is in specified range.
    @param value The attribute value to check.
    @param range A Python set giving the range of allowed values.
    @param msg The message to display if value is out-of-range.
    @param mapping A Python dictionary giving mapping between values (i.e. from MDF to LMF)
    @return The value to set, or None if out-of-range.
    """
    # Check value
    if value not in range:
        # Check converted value
        if mapping is not None:
            try:
                converted_value = mapping[value]
            except KeyError:
                raise Error(msg)
            # Converted value to set
            return converted_value
        else:
            raise Error(msg)
    else:
        # Value to set
        return value
