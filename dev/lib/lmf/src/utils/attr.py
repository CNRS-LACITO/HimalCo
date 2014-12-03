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

def check_date_format(date):
    """! @brief Verify that date format is composed as follows: YYYY-MM-DD (ISO 8601).
    If not, raise an Error.
    @param date Date to check.
    """
    import re
    if not re.match("^\d{4}-[01]\d-[0-3]\d$", date):
        raise Error("Date must be formatted as follows: YYYY-MM-DD (given date is %s)" % date)

def check_time_format(time):
    """! @brief Verify that time format is composed as follows: THH:MM:SS,MSMS (ISO 8601: 'T' for Time).
    If not, raise an Error.
    @param time Time to check.
    """
    import re
    if not re.match("^T[0-2]\d:[0-5]\d:[0-5]\d(\,\d+|)$", time):
        raise Error("Time must be formatted as follows: THH:MM:SS,MSMS (given time is %s)" % time)

def check_duration_format(duration):
    """! @brief Verify that duration format is composed as follows: PTxxHxxMxxS (ISO 8601: 'P' for Period).
    If not, raise an Error.
    @param duration Duration to check.
    """
    import re
    if not re.match("^PT[0-2]\dH[0-5]\dM[0-5]\dS$", duration):
        raise Error("Duration must be formatted as follows: PTxxHxxMxxS (given duration is %s)" % duration)
