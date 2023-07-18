from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Testing for the Base class"""
    def setUp(self):
        """Setup test instances for methods and attributes"""
        Base._Base__nb_objects = 0
        self.inst1 = Base()
        self.inst2 = Base()
        self.inst3 = Base(10)
        self.inst4 = Base()

    def test_id(self):
        """Test id of created object"""
        self.assertEqual(self.inst1.id, 1)
        self.assertEqual(self.inst2.id, 2)
        self.assertEqual(self.inst3.id, 10) 
        self.assertEqual(self.inst4.id, 3)
