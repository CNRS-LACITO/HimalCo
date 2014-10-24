#! /usr/bin/env python

from startup import *
from utils.attr import check_attr_type, check_attr_range
from utils.error_handling import Error

## Test attribute functions

class TestAttrFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_attr_type(self):
        check_attr_type(1, int, "int")
        check_attr_type("1", str, "str")
        check_attr_type(set(), set, "set")
        check_attr_type(dict(), dict, "dict")
        check_attr_type(list(), list, "list")
        test = False
        try:
            check_attr_type(dict(), list, "error")
        except Error:
            test = True
        self.assertTrue(test)

    def test_check_attr_range(self):
        range = [1, "allowed value", [2, 3]]
        mapping = {10 : 1}
        self.assertEqual(check_attr_range(1, range, "ok"), range[0])
        self.assertEqual(check_attr_range("allowed value", range, "ok"), range[1])
        self.assertEqual(check_attr_range([2, 3], range, "ok"), range[2])
        self.assertEqual(check_attr_range(10, range, "ok", mapping), range[0])
        test = False
        try:
            check_attr_range(10, range, "error")
        except Error:
            test = True
        test = False
        try:
            check_attr_range(11, range, "error", mapping)
        except Error:
            test = True
        self.assertTrue(test)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAttrFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
