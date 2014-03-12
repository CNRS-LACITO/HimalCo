#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *

## Test InOut class

class TestInOutFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a InOut object
        self.in_out = InOut()

    def tearDown(self):
        # Release instantiated objects
        del self.in_out

    def test_create_obj(self):
        import os, shutil
        shutil.rmtree("obj/", ignore_errors=True)
        # Test when "obj/" folder does not exist
        self.in_out.create_obj()
        self.assertTrue(os.path.exists("obj"))
        # Test when "obj/" folder already exists
        self.in_out.create_obj()
        self.assertTrue(os.path.exists("obj"))

    def test_open_file(self):
        import os
        test_filename = "obj/test_file.txt"
        test_string = "toto"
        # Test write
        test_file = self.in_out.open_file(test_filename, 'w')
        test_file.write(test_string)
        test_file.close()
        # Test read
        test_file = self.in_out.open_file(test_filename, 'r')
        self.assertEqual(test_file.readline(), test_string)
        test_file.close()
        os.remove(test_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestInOutFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
