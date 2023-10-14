#!/usr/bin/python3
'''
module to test rectangle class
'''
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    '''
    Test the rectangle class
    '''
    def setUp(self):
        self.r1 = Rectangle(5, 1)

    def tearDown(self):
        pass

    def test_id(self):
        self.r3 = Rectangle(2, 5, 0, 0, 25)
        self.assertEqual(self.r3.id, 25)

    def test_noarg(self):
        with self.assertRaises(TypeError):
            r0 = Rectangle()

    def test_width(self):
        self.assertEqual(self.r1.width, 5)

        self.r1.width = 80

        self.assertEqual(self.r1.width, 80)

        with self.assertRaises(TypeError):
            self.r1.width = "okibe"

        with self.assertRaises(ValueError):
            self.r1.width = -25

        with self.assertRaises(ValueError):
            self.r1.width = 0

    def test_height(self):
        self.assertEqual(self.r1.height, 1)

        self.r1.height = 80

        self.assertEqual(self.r1.height, 80)

        with self.assertRaises(TypeError):
            self.r1.height = "okibe"

        with self.assertRaises(ValueError):
            self.r1.height = -25

        with self.assertRaises(ValueError):
            self.r1.height = 0

    def test_set_x(self):
        self.assertEqual(self.r1.x, 0)
        self.r1.x = 20
        self.assertEqual(self.r1.x, 20)
        with self.assertRaises(ValueError):
            self.r1.x = -2

    def test_set_y(self):
        self.assertEqual(self.r1.y, 0)
        self.r1.y = 20
        self.assertEqual(self.r1.y, 20)
        with self.assertRaises(ValueError):
            self.r1.y = -2
