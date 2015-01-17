#! /usr/bin/env python

from startup import *
from input.sort_order import sort_order_read

## Test sort order functions

class TestSortOrderFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sort_order_read(self):
        import sys
        utest_path = sys.path[0] + '/'
        sort_order_filename = utest_path + "../src/config/sort_order.xml"
        # Read XML sort order file and test result
        order = sort_order_read(sort_order_filename)
        expected_order = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        self.assertEqual(order, expected_order)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSortOrderFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
