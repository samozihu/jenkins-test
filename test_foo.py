#!/usr/bin/env python
# encoding: utf-8

import unittest
import foo

class SimpleTest(unittest.TestCase):
    '''Test the funtion of division
    '''

    def test1(self):
        self.assertEqual(foo.divide(2, 2), 1)

    def test2(self):
        self.assertEqual(foo.divide(0, 1), 0)

if __name__ == "__main__":
    unittest.main()
