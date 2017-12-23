import unittest
from pasha.vector import Vector

class TestVectorClass(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector([1, 2, 3])

    def test_isvector(self):
        self.assertTrue(isinstance(self.v1, Vector))

    def test_non_integer(self):
        with self.assertRaises(ValueError):
            Vector(['1', 2, 3])

    def test_empty_vector(self):
        with self.assertRaises(ValueError):
            Vector([])

    def test_noniterable(self):
        with self.assertRaises(TypeError):
            Vector(1)

    def test_str(self):
        self.assertTrue('Vector: (1, 2, 3)' == self.v1).__str__())

    def test_eq(self):
        self.assertTrue(self.v1.__eq__(Vector([1, 2, 3])))
