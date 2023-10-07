#!/usr/bin/python3
import unittest
'''
Test file module
'''


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        test class for find max integer function
    '''
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_start_list(self):
        self.assertEqual(max_integer([100, 25, 50, 10]), 100)

    def test_max_at_end_list(self):
        self.assertEqual(max_integer([10, 25, 50]), 50)

    def test_one_elem_list(self):
        self.assertEqual(max_integer([1]), 1)
