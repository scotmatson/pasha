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
