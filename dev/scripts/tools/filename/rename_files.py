#! /usr/bin/env python

"""! This script renames files containing a number on 3 digits at the beginning: 'nnnXXX.xxx'. Number of digits, pattern, and value range can be easily modified in following lines.
    Run 'python rename_files.py -h' to have more details on how to use this script.
"""
DIGITS_NB = 3
PATTERN = r"^(\d{" + str(DIGITS_NB) + "})(.*)$"
# Define value range
MIN_VALUE = 0
MAX_VALUE = int(DIGITS_NB * '9')

def parse_options():
    """! @brief Get command line arguments.
    @return Options as attributes of the namespace.
    """
    # Import needed module
    from optparse import OptionParser
    # Options management
    parser = OptionParser()
    parser.add_option("-i", "--integer", dest="integer", action="store", default=0, help="value to increment/decrement the filename number [default=0]")
    parser.add_option("-p", "--path", dest="path", action="store", default='.', help="path containing files to rename [default=\".\"]")
    return parser.parse_args()[0]

def rename_file(integer, path, filename):
    """Increment or decrement the number contained in a filename.
    @param integer An integer value to add to the number contained in filename. A negative value decrements the number.
    @param path Path of the file to rename, including trailing slash or backslash.
    @param filename Name of the file containing a number to increment or decrement.
    """
    import re, os
    # Use regex to find the number to increment/decrement in filename
    result = re.match(PATTERN, filename)
    # If filename does not contain a number as expected, do not rename it
    if result is not None:
        # Increment/decrement the number
        value = int(result.group(1)) + integer
        # If the new number is out-of-range, do not rename the file, and inform user
        if value < MIN_VALUE or value > MAX_VALUE:
            print "Error with file '%s': obtained an out-of-range value (%d)" % (filename, value)
        else:
            # Convert new value from integer to string with requested number of digits
            value = ("%0"+ str(DIGITS_NB) + "d") % value
            # Rename file with the new number
            os.rename(path + filename, path + value + result.group(2))

if __name__ == '__main__':
    # Import needed modules
    import os, sys
    # Get command line options
    options = parse_options()
    # Convert value from string to integer
    options.integer = int(options.integer)
    # Add trailing slash or backslash to path
    if os.name is 'posix':
        options.path += '/'
    else:
        options.path += r'\\'
    # Get a list of files to process
    filenames = os.listdir(options.path)
    # Rename each file of the list
    for filename in filenames:
        rename_file(options.integer, options.path, filename)
    # Exit program properly
    sys.exit(0)
