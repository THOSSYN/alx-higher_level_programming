#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Create a test case object"""
    def test_maxint(self):
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1.2, 3.4, 4.3, 2.1]), 4.3)

        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])

if __name__ == '__main__':
    unittest.main()
