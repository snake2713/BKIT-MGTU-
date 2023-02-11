import unittest
import math
from main import get_D, get_D2, get_roots

class TestCalculator(unittest.TestCase):
    def test_get_D(self):
        self.assertEqual(get_D(1, 1, 1), -3)
        self.assertEqual(get_D(0.25, 0, -1), 1)
        self.assertEqual(get_D(0, 10, -1000), 100)

    def test_get_D2(self):
        self.assertEqual(get_D2(1, 3, 5), 1)
        self.assertEqual(get_D2(2, 0, 2), 0.5)
        self.assertEqual(get_D2(13, 0, 0), 0)

    def test_get_roots(self):
        self.assertEqual(get_roots(1, -2, 1), [-1, 1])
        self.assertEqual(get_roots(1, 0, 0), [0])
        self.assertEqual(get_roots(1, -4, 0), [0, 2, -2])
        self.assertEqual(get_roots(1, 1, 1), [])

if __name__ == "__main__":
    unittest.main()