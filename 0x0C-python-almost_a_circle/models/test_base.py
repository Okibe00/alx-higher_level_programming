#!/usr/bin/python3
'''
test module
'''

import base
import unittest


class test_base(unittest.TestCase):
    '''
    test class
    '''
    def setUp(self):
        self.b1 = base.Base()
        self.b2 = base.Base()
        self.b3 = base.Base()
        self.b4 = base.Base()
        self.b5 = base.Base()

        self.bg1 = base.Base(200)
        self.bg2 = base.Base(0)
        self.bg3 = base.Base(-1)

    def tearDown(self):
        pass

    def test_id(self):
        '''
        test when id is None
        '''
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 5)

    def test_user_id(self):
        '''
        Test large id values and 0 and negative id
        '''
        self.assertEqual(self.bg1.id, 200)
        self.assertEqual(self.bg2.id, 0)
        self.assertNotEqual(self.bg3.id, -1)


if __name__ == "__main__":
    unittest.main()
