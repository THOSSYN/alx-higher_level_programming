from models.rectangle import Rectangle
from models.base import Base
import unittest
import io
import contextlib


class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        """Setup test class for methods and attributes of classes"""
        Base._Base__nb_objects = 0
        self.inst1 = Rectangle(10, 2)
        self.inst2 = Rectangle(9, 4)
        self.inst3 = Rectangle(5, 8, 0, 0, 9)
        self.inst4 = Rectangle(10, 2, 1, 3)
        self.inst5 = Rectangle(10, 2, 3, 1)
        self.inst6 = Rectangle(3, 2, 1, 2)
        self.inst7 = Rectangle(4, 6, 2, 1, 12)
    
    def test_width(self):
        """Test for width attribute"""
        self.assertEqual(self.inst1.width, 10)
        self.assertEqual(self.inst2.width, 9)
        self.assertEqual(self.inst3.width, 5)

        with self.assertRaises(ValueError):
            self.inst = Rectangle(-5, 20, 1, 2)

        with self.assertRaises(TypeError):
            self.inst = Rectangle("", 7, 5, 2)
    
    def test_height(self):
        """Test for height attribute"""
        self.assertEqual(self.inst1.height, 2)
        self.assertEqual(self.inst2.height, 4)
        self.assertEqual(self.inst3.height, 8)

        with self.assertRaises(ValueError):
            self.inst = Rectangle(5, -20, 1, 2)

        with self.assertRaises(TypeError):
            self.inst = Rectangle(4, "", 5, 2)

    
    def test_x(self):
        """test for x attribute"""
        self.assertEqual(self.inst3.x, 0)
        self.assertEqual(self.inst4.x, 1)
        self.assertEqual(self.inst5.x, 3)

        with self.assertRaises(ValueError):
            self.inst = Rectangle(5, 20, -1, 2)

        with self.assertRaises(TypeError):
            self.inst = Rectangle(5, 20, "1", 2)

    def test_y(self):
        """Test for y attributes"""
        self.assertEqual(self.inst3.y, 0)
        self.assertEqual(self.inst4.y, 3)
        self.assertEqual(self.inst5.y, 1)

        with self.assertRaises(ValueError):
            self.inst = Rectangle(5, 20, 1, -2)

        with self.assertRaises(TypeError):
            self.inst = Rectangle(5, 20, 1, "2")

    def test_area(self):
        """Test for area method"""
        self.assertEqual(self.inst1.area(), 20)
        self.assertEqual(self.inst3.area(), 40)

    #self.inst6 = Rectangle(3, 2, 1, 2)
    def test_print_area_in_string(self):
        """Test for String Representation f area method"""
        expected_output = '\n\n ###\n ###\n'

        with io.StringIO() as mockStdout, contextlib.redirect_stdout(mockStdout):
            self.inst6.display()
            actual_output = mockStdout.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_overriden_str_method(self):
        """Test for overriden str() method"""
        output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(self.inst7), output)

    def test_update_args_method(self):
        """Test for args update method"""
        self.inst7.update(89)
        self.assertEqual(str(self.inst7), "[Rectangle] (89) 2/1 - 4/6")
        self.inst6.update(89, 9)
        self.assertEqual(str(self.inst6), "[Rectangle] (89) 1/2 - 9/2")
        self.inst6.update(89, 9, 8, 7, 6)
        self.assertEqual(str(self.inst6), "[Rectangle] (89) 7/6 - 9/8")

    def test_update_kwargs_method(self):
        """Test for kwargs in update method"""
        self.inst7.update(height=1)
        self.assertEqual(str(self.inst7), "[Rectangle] (12) 2/1 - 4/1")
        self.inst6.update(id=89, width=9)
        self.assertEqual(str(self.inst6), "[Rectangle] (89) 1/2 - 9/2")
        self.inst6.update(id=89, height=8, y=7, width=7, x=6)
        self.assertEqual(str(self.inst6), "[Rectangle] (89) 6/7 - 7/8")

    def test_id_inherit_for_rectangle(self):
        """Test for inherited id attribute"""
        self.assertEqual(self.inst1.id, 1)
        self.assertEqual(self.inst2.id, 2)
        self.assertEqual(self.inst3.id, 9)
    
