#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Add the repository path before the Python path to use the correct xlwt and xlrd libraries
import sys
sys.path.insert(1, "../lib/python-excel/xlwt-master")
sys.path.insert(1, "../lib/python-excel/xlrd-master")

class XlsFormat():
    def __init__(self):
        self.options = None
        self.sheet = None
        self.wb = None

    def create_book(self):
        """Create workbook.
        """
        from xlwt import Workbook
        return Workbook(encoding='utf-8')

    def open_book(self):
        """Open workbook.
        """
        import xlrd
        self.wb = xlrd.open_workbook(self.options.input, formatting_info=True, on_demand=True, encoding_override='utf-8')

    def get_sheets(self):
        """Retrieve names of all sheets as a list.
        """
        return self.wb.sheet_names()

    def get_sheet(self):
        """Retrieve the first sheet.
        """
        self.sheet = self.wb.sheet_by_name(self.get_sheets()[0])

    def display_sheet(self):
        """Display the beginning of a sheet.
        """
        if self.options.verbose:
            print "A1: {}".format(self.sheet.cell_value(0, 0))
            print "B1: {}".format(self.sheet.cell_value(0, 1))
            print "C1: {}".format(self.sheet.cell_value(0, 2))
            print "A2: {" + unicode(self.sheet.cell_value(1, 0)) + "}"
            print "B2: {" + unicode(self.sheet.cell_value(1, 1)) + "}"
            print "C2: {" + unicode(self.sheet.cell_value(1, 2)) + "}"

    def is_row_hidden(self, row_nb):
        """Check if a row is hidden.
        """
        return bool(self.sheet.rowinfo_map[row_nb].hidden)

    def is_col_hidden(self, col_nb):
        """Check if a column is hidden.
        """
        try:
            return bool(self.sheet.colinfo_map[col_nb].hidden)
        except KeyError:
            return False

    def get_contents(self, row_nb, col_nb):
        """Get cell contents.
        """
        return unicode(self.sheet.cell_value(row_nb, col_nb))
