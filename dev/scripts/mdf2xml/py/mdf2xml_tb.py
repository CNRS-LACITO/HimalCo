#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Go under dev/scripts/ and launch this script using the following command:
# python mdf2xml/py/mdf2xml_tb.py

# Import system Python module
import sys
# Import utilities
sys.path.append(".")
from common import *

# Default values of command line arguments
DEFAULT_INPUT = DICT_JAP
DEFAULT_OUTPUT = None
DEFAULT_DATABASE = LP_DB_JAP
DEFAULT_GRAMMAR = GRAMMAR_JAP1
DEFAULT_STRUCT = TB_STRUCT_JAP
DEFAULT_TEST = None

# XmlFormat inherits from InOut
class Mdf2Xml(MdfFormat, XmlFormat):
    def __init__(self):
        MdfFormat.__init__(self)
        self.tmp_filename = None
        self.txt_filename = None

    def parse_options(self):
        """Get command line arguments.
        """
        # Options management
        from optparse import OptionParser
        parser = OptionParser()
        parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print more details to stdout [default=False]")
        parser.add_option("-i", "--input", dest="input", action="store", default=DEFAULT_INPUT, help="input text file [default=" + str(DEFAULT_INPUT) + "]")
        parser.add_option("-o", "--output", dest="output", action="store", default=DEFAULT_OUTPUT, help="output xml file [default=" + str(DEFAULT_OUTPUT) + "]")
        parser.add_option("-d", "--database", dest="database", action="store", default=DEFAULT_DATABASE, help="database to open [default=" + str(DEFAULT_DATABASE) + "]")
        parser.add_option("-g", "--grammar", dest="grammar", action="store", default=DEFAULT_GRAMMAR, help="grammar to use [default=" + str(DEFAULT_GRAMMAR) + "]")
        parser.add_option("-s", "--struct", dest="struct", action="store", default=DEFAULT_STRUCT, help="toolbox hierarchy [default=" + str(DEFAULT_STRUCT) + "]")
        parser.add_option("-t", "--test", dest="test", action="store", default=DEFAULT_TEST, help="test to run [default=" + str(DEFAULT_TEST) + "]")
        self.options = parser.parse_args()[0]
        # Tests
        if self.options.test is not None:
            if self.options.test == "japhug1":
                self.options.input = "test/japhug/input/japhug1.txt"
                self.options.grammar = GRAMMAR_JAP1
            elif self.options.test == "japhug2":
                self.options.input = "test/japhug/input/japhug2.txt"
                self.options.grammar = GRAMMAR_JAP2
            elif self.options.test == "khaling1":
                self.options.input = "test/khaling/input/khaling1.txt"
                self.options.grammar = GRAMMAR_KLR1
            elif self.options.test == "khaling2":
                self.options.input = "test/khaling/input/khaling2.txt"
                self.options.grammar = GRAMMAR_KLR2
            else:
                sys.exit(-1)
        # Compute output filename
        if self.options.output is None:
            self.options.output = "./obj/" + self.options.input[self.options.input.rfind('/') + 1:self.options.input.rfind('.') + 1] + "xml"
        # Compute intermediary filenames
        mdf_filename_wo_ext = self.options.output.rstrip(".xml")
        self.tmp_filename = mdf_filename_wo_ext + ".tmp"
        self.txt_filename = mdf_filename_wo_ext + ".txt"

    def remove_fields(self):
        """Remove empty fields.
        """
        mdf_file = self.open_read(self.options.input)
        tmp_file = self.open_write(self.tmp_filename)
        for line in mdf_file.readlines():
            l = line.split()
            # Keep blank lines to separate lexemes and keep header
            if l == [] or len(l) >= 2 or (len(l) == 1 and l[0] == "\_DateStampHasFourDigitYear"):
                tmp_file.write(line)
        mdf_file.close()
        tmp_file.close()

    def format_fields(self):
        """Format MDF fields.
        """
        pd = set(['\\1s', '\\1p', '\\1d', '\\1e', '\\2s', '\\2p', '\\3s', '\\3p', '\\3d', '\\4s'])
        tmp_file = self.open_read(self.tmp_filename)
        txt_file = self.open_write(self.txt_filename)
        for line in tmp_file.readlines():
            l = line.split()
            if len(l) > 1 and (l[0] == '\\lx' or l[0] == '\\se' or l[0] == '\\a' or l[0] == '\\xv'):
                txt_file.write(self.format_lx(line))
            elif len(l) > 1 and l[0] in pd:
                txt_file.write(self.format_pd(line))
            else:
                txt_file.write(line)
        tmp_file.close()
        txt_file.close()

    def format_lx(self, line):
        """Remove '_', '^', '$', '&' character at the beginning of 'lx', 'se', 'a', 'xv' fields.
        """
        lx = line.split()
        line = lx[0] + " " + lx[1].lstrip('_^$&') + "\n"
        return line

    def format_pd(self, line):
        """Format paradigms fields.
        """
        import re
        return re.sub(r"^(\\)(\d\w) (.*)", r"\1" + 'a' + r"\2" + ' ' + r"\3", line)

    def main(self):
        import os
        self.create_obj()
        self.parse_options()
        # Remove empty fields => .tmp
        self.remove_fields()
        # Format MDF fields => .txt
        self.format_fields()
        # NLTK processing
        self.options.input = self.txt_filename
        self.process_data()
        # Write output XML
        self.write_result()
        self.display_result()
        # Delete temporary file
        os.remove(self.tmp_filename)

if __name__ == '__main__':
    converter = Mdf2Xml()
    converter.main()
    # Exit program properly
    sys.exit(0)
