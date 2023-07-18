from models.square import Square
import unittest
import io
import contextlib


class Test_Square(unittest.TestCase):
    def setUp(self):
        self.inst8 = Square(5)
        self.inst9 = Square(2, 2)

    """
    def test_square_attribute_from_rectangle(self):
        self.assertEqual(str(self.inst8), '[Square] (1), 0/0 - 5')
        self.assertEqual(self.inst8.area(), 25)
        expected1 = '#####\n#####\n#####\n#####\n#####\n'
        with io.StringIO() as captured, contextlib.redirect_stdout(captured):
            self.inst8.display()
            actual_output = captured.getvalue()
        self.assertEqual(actual_output, expected1)
    """ 

    def test_print_padded_hash_symbol_area(self):
        self.assertEqual(str(self.inst9), "[Square] (2), 2/0 - 2")
        self.assertEqual(self.inst9.area(), 4)
        expected2 = '  ##\n  ##\n'
        with io.StringIO() as captured, contextlib.redirect_stdout(captured):
            self.inst9.display()
            actual_output = captured.getvalue()
        self.assertEqual(actual_output, expected2)

