#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# python xls2xml/py/xls2mdf.py

# Import system Python module
import sys
# Import utilities
sys.path.append(".")
from common import *

# Default values of command line arguments
DEFAULT_INPUT = DICT_NA
DEFAULT_OUTPUT = None
DEFAULT_GRAMMAR = GRAMMAR_NA
DEFAULT_TEST = None

class Xls2Mdf(InOut, XlsFormat):
    def __init__(self):
        XlsFormat.__init__(self)
        self.tmp_filename = None
        self.txt_filename = None

    def parse_options(self):
        """Get command line arguments.
        """
        # Options management
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print more details to stdout [default=False]")
        parser.add_option("-i", "--input", dest="input", action="store", default=DEFAULT_INPUT, help="input Excel file [default=" + str(DEFAULT_INPUT) + "]")
        parser.add_option("-o", "--output", dest="output", action="store", default=DEFAULT_OUTPUT, help="output MDF file [default=" + str(DEFAULT_OUTPUT) + "]")
        parser.add_option("-g", "--grammar", dest="grammar", action="store", default=DEFAULT_GRAMMAR, help="grammar to use [default=" + str(DEFAULT_GRAMMAR) + "]")
        parser.add_option("-t", "--test", dest="test", action="store", default=DEFAULT_TEST, help="test to run [default=" + str(DEFAULT_TEST) + "]")
        self.options = parser.parse_args()[0]
        # Tests
        if self.options.test is not None:
            if self.options.test == "na1":
                self.options.input = "test/na/input/na1.xls"
            else:
                sys.exit(-1)
        # Compute output filename
        if self.options.output is None:
            self.options.output = "./obj/" + self.options.input[self.options.input.rfind('/') + 1:self.options.input.rfind('.') + 1] + "mdf"
        # Compute intermediary filenames
        mdf_filename_wo_ext = self.options.output.rstrip(".mdf")
        self.tmp_filename = mdf_filename_wo_ext + ".tmp"
        self.txt_filename = mdf_filename_wo_ext + ".txt"

    def get_marker(self, col_nb):
        """Get the marker associated with a cell.
        """
        # Keep only first 3 characters '\xx'
        return self.get_contents(0, col_nb)[:3]

    def display_markers(self):
        """Display all found markers.
        """
        if self.options.verbose:
            for col_nb in range (0, self.sheet.ncols):
                print str(col_nb), self.get_marker(col_nb)

    def write_fields(self):
        """Write out all the fields with their associated marker.
        """
        from xlrd.biffh import XL_CELL_EMPTY, XL_CELL_BLANK
        tmp_file = self.open_write(self.tmp_filename)
        for row_nb in range (1, self.sheet.nrows):
            if row_nb < 5000 and not self.is_row_hidden(row_nb):
                for col_nb in range (0, self.sheet.ncols):
                    if not self.is_col_hidden(col_nb):
                        value = self.get_contents(row_nb, col_nb)
                        if value is not XL_CELL_EMPTY and value is not XL_CELL_BLANK:
                            tmp_file.write(self.get_marker(col_nb) + " " + value + "\n")
                tmp_file.write("\n")
        # Close file after processing
        tmp_file.close()

    def format_fields(self):
        """Format MDF fields.
        """
        tmp_file = self.open_read(self.tmp_filename)
        mdf_file = self.open_write(self.options.output)
        examples = ''
        for line in tmp_file.readlines():
            l = line.split()
            # Keep blank lines to separate lexemes
            if l == [] or (len(l) >=2 and l[0] == '\\lx' and l[1].find('ENTRY') != -1):
                mdf_file.write(self.format_lx(line))
            elif len(l) > 1 and l[0] == '\\xv':
                examples += line
            elif len(l) > 1 and l[0] == '\\xf':
                examples += line
                # Process all 'xv' and 'xf' examples once
                mdf_file.write(self.format_example(examples))
                examples = ''
            elif len(l) > 1 and l[0] == '\\va':
                mdf_file.write(self.format_va(line))
            else:
                mdf_file.write(line)
        tmp_file.close()
        mdf_file.close()

    def remove_fields(self):
        """Remove empty and useless fields (\ms *).
        """
        mdf_file = self.open_read(self.options.output)
        txt_file = self.open_write(self.txt_filename)
        for line in mdf_file.readlines():
            l = line.split()
            # Keep blank lines to separate lexemes
            if l == [] or (len(l) >= 2 and l[1] != '*'):
                txt_file.write(line)
        mdf_file.close()
        txt_file.close()

    def format_lx(self, line):
        """Format 'lx' field.
        """
        if line.find('_SUBENTRY') != -1:
            return "\se " + line.split()[1].split('_')[0] + "\n"
        else:
            return line.replace('_MAINENTRY', '')

    def format_example(self, all_examples):
        """Format 'xv' and 'xf' fields.
        """
        # Import regular expression Python module
        import re
        # String to return in an MDF format: "\xv ...\n\xf ...\n\xv ...\n\xf ...\n" etc.
        std_examples = ''
        # Examples are separated by " <number>"
        pattern = re.compile(r" <\d*>")
        # Remove markers and split into 'xv' and 'xf' examples
        all_examples = all_examples.lstrip("\\xv ")
        all_examples = all_examples.split("\\xf ")
        # Now, put each example in a separated element of a double list: [0] for 'xv' and [1] for 'xf'
        list_examples = []
        for line in all_examples:
            # Remove leading end of line
            line = line.rstrip('\n')
            list_examples.append(re.split(pattern, line))
        # Check that there are as many 'xv' as 'xf' examples
        if len(list_examples[0]) != len(list_examples[1]):
                sys.exit(-1)
        # Alternate 'xv' and 'xf'
        for i in range (0, len(list_examples[0])):
            std_examples += "\\xv " + list_examples[0][i] + '\n' + "\\xf " + list_examples[1][i] + '\n'
        return std_examples

    def format_va(self, line):
        """Format 'va' field into 'va' and 'vf' fields.
        """
        # 'va' field is formatted as follows: "va (vf) (vf)" etc.
        va = line.split('(')
        # String to return in an MDF format: "\va ...\n\vf ...\n\vf ...\n" etc.
        std_va = va[0].rstrip('\n ') + "\n"
        for i in range (1, len(va)):
            # Remove leading end of line and closing parenthesis
            std_va += "\\vf " + va[i].rstrip('\n )') + "\n"
        return std_va

    def main(self):
        import os
        self.create_obj()
        self.parse_options()
        self.open_book()
        self.get_sheet()
        # Display in verbose mode
        self.display_sheet()
        self.display_markers()
        # Convert to MDF => .tmp
        self.write_fields()
        # Format MDF fields => .mdf
        self.format_fields()
        # Remove empty and useless fields (\ms *) => .txt
        self.remove_fields()
        # Delete temporary file
        os.system("rm " + self.tmp_filename)

if __name__ == '__main__':
    converter = Xls2Mdf()
    converter.main()
    # Exit program properly
    sys.exit(0)
