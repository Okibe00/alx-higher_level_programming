#!/usr/bin/python3
'''
Module to test the dislay function
'''
from models.rectangle import Rectangle
from unittest.mock import patch
import unittest
import io


class test_display(unittest.TestCase):
    '''
    test display function
    '''
    def setUp(self):
        self.d1 = Rectangle(4, 6)

    def test_display_f(self):
        @patch("sys.stdout", new_callable=io.StringIO)
        def test_print_display(self, mock_output):
            self.d1.display()
            output = mock_output.getValue.strip()
            expected_output = "####\n####\n####\n####\n####\n####\n"
            self.assertEqual(output, expected_output)
