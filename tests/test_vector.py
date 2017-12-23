import unittest
from pasha.vector import Vector

class TestVectorClass(unittest.TestCase):

    def test_vector(self):
        self.assertTrue(isinstance(Vector([1, 2, 3]), Vector))
        with self.assertRaises(TypeError):
            Vector(1, 2, 3)
        with self.assertRaises(ValueError):
            Vector([])
        with self.assertRaises(ValueError):
            Vector(['1', 2, 3])

    def test_str(self):
        self.assertTrue('Vector: (1, 2, 3)' == Vector([1, 2, 3]).__str__())
