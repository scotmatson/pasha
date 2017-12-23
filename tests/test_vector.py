import unittest
from pasha.vector import Vector

class TestVectorClass(unittest.TestCase):

    def test_isvector(self):
        self.assertTrue(isinstance(Vector([1, 2, 3]), Vector))

    def test_non_integer(self):
        with self.assertRaises(ValueError):
            Vector(['1', 2, 3])

    def test_empty_vector(self):
        with self.assertRaises(ValueError):
            Vector([])

    def test_noniterable(self):
        with self.assertRaises(TypeError):
            Vector(1, 2, 3)

    def test_str(self):
        self.assertTrue('Vector: (1, 2, 3)' == Vector([1, 2, 3]).__str__())

    def test_eq(self):
        self.assertTrue(Vector([1, 2, 3]).__eq__(Vector([1, 2, 3])))
