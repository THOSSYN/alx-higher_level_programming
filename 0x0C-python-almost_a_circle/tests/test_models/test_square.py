from models.square import Square
from models.base import Base
import unittest
import io
import contextlib


class Test_Square(unittest.TestCase):
    """Creates test class for methods and instances"""
    def setUp(self):
        """setup instances of each class or method to be tested"""
        Base._Base__nb_objects = 0
        self.inst8 = Square(5)
        self.inst9 = Square(2, 2)
        self.inst10 = Square(10,2,1)

    def test_square_attribute_from_rectangle(self):
        self.assertEqual(str(self.inst8), '[Square] (1), 0/0 - 5')
        self.assertEqual(self.inst8.area(), 25)
        expected1 = '#####\n#####\n#####\n#####\n#####\n'
        with io.StringIO() as captured, contextlib.redirect_stdout(captured):
            self.inst8.display()
            actual_output = captured.getvalue()
        self.assertEqual(actual_output, expected1)

    def test_print_padded_hash_symbol_area(self):
        """Test for behaviour when string is printed"""
        self.assertEqual(str(self.inst9), "[Square] (2), 2/0 - 2")
        self.assertEqual(self.inst9.area(), 4)
        expected2 = '  ##\n  ##\n'
        with io.StringIO() as captured, contextlib.redirect_stdout(captured):
            self.inst9.display()
            actual_output = captured.getvalue()
        self.assertEqual(actual_output, expected2)

        with self.assertRaises(TypeError):
                Square("2")

    def test_setter_of_size(self):
        """Set value of size"""
        self.inst8.size = 5
        self.assertEqual(str(self.inst8), "[Square] (1), 0/0 - 5")

    def test_getter(self):
        """Test what the getter returns"""
        self.inst8.size = 10
        self.value = self.inst8.size
        self.assertEqual(self.value, 10)

    def test_update(self):
        """Tests update behaviour"""
        self.inst8.update()
        self.assertEqual(str(self.inst8), "[Square] (1), 0/0 - 5")
        self.inst8.update(1, 2, 3, 4)
        self.assertEqual(str(self.inst8), "[Square] (1), 3/4 - 2")
        self.inst8.update(size=1,y= 2, x=3, id=4)
        self.assertEqual(str(self.inst8), "[Square] (4), 3/2 - 1")

    def test_dictionary_return(self):
        """Check a dictionary representation"""
        expected_output = {'id': 3, 'x': 2, 'size': 10, 'y': 1}
        actual_output = self.inst10.to_dictionary()
        self.assertEqual(actual_output, expected_output)
