#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *

## Test XlsFormat class

class TestXlsFormatFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a XlsFormat object
        self.xls_format = XlsFormat()
        self.xls_format.options = Options()
        self.xls_format.options.input = "obj/test_file.xls"
        self.xls_format.options.verbose = False
        # Write input file
        self.book = self.xls_format.create_book()
        self.sheet = self.book.add_sheet("sheet")
        self.sheet.write(0, 0, label="00")
        self.sheet.write(0, 1, label="01")
        self.sheet.write(0, 2, label="02")
        self.sheet.write(1, 0, label="10")
        self.sheet.write(1, 1, label="11")
        self.sheet.write(1, 2, label="12")
        self.book.save(self.xls_format.options.input)

    def tearDown(self):
        import os
        os.remove(self.xls_format.options.input)
        # Release instantiated objects
        del self.sheet, self.book, self.xls_format.options, self.xls_format

    def test_init(self):
        self.assertIsNone(self.xls_format.sheet)
        self.assertIsNone(self.xls_format.wb)

    def test_create_book(self):
        import xlwt
        self.assertIsInstance(self.xls_format.create_book(), xlwt.Workbook)

    def test_open_book(self):
        import xlrd
        self.xls_format.open_book()
        self.assertIsInstance(self.xls_format.wb, xlrd.book.Book)

    def test_get_sheets(self):
        self.xls_format.open_book()
        self.assertListEqual(self.xls_format.get_sheets(), ["sheet"])

    def test_get_sheet(self):
        import xlrd
        self.xls_format.open_book()
        self.xls_format.get_sheet()
        self.assertIsInstance(self.xls_format.sheet, xlrd.sheet.Sheet)

    def test_display_sheet(self):
        self.xls_format.open_book()
        self.xls_format.get_sheet()
        self.xls_format.display_sheet()

    def test_is_row_hidden(self):
        self.xls_format.open_book()
        self.xls_format.get_sheet()
        self.assertFalse(self.xls_format.is_row_hidden(0))

    def test_get_contents(self):
        self.xls_format.open_book()
        self.xls_format.get_sheet()
        self.assertEqual(self.xls_format.get_contents(1,2), "12")

suite = unittest.TestLoader().loadTestsFromTestCase(TestXlsFormatFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
