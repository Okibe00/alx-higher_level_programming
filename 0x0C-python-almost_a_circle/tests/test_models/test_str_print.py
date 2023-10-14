#!/usr/bin/python3
'''
Test the __str__ method
'''
from models.rectangle import Rectangle
import unittest
import io
from unittest.mock import patch


class test_str_method(unittest.TestCase):
    '''
        test the __str__ method
    '''
    def setUp(self):
        self.s0 = Rectangle(4, 6, 2, 1, 12)

    def test_string_method(self):
        '''
        test string method
        '''
        @patch("sys.stdout", new_callable=io.StringIO)
        def print_str(self, mock_output):
            print(self.s0)
            output = mock_output.getValue.strip()
            expected_output = f"[Rectangle] (12) 2/1 - 4/6)"
            self.assertEqual(output, expected_output)
