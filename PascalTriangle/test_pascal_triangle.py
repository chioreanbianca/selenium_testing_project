import unittest
from pascal_triangle import pascal 

class TestPascalFunction(unittest.TestCase):

    def test_valid_cases(self):
        self.assertEqual(pascal(0, 2), 1)
        self.assertEqual(pascal(1, 2), 2)
        self.assertEqual(pascal(1, 3), 3)
        self.assertEqual(pascal(2, 4), 6)
        self.assertEqual(pascal(2, 3), 3)
        self.assertEqual(pascal(3, 4), 4)
        self.assertEqual(pascal(0, 4), 1)

    def test_invalid_cases(self):
        with self.assertRaises(ValueError):
            pascal(-1, 2)
        
        with self.assertRaises(ValueError):
            pascal(1, -1)
        
        with self.assertRaises(ValueError):
            pascal(2, 1)
        
        with self.assertRaises(ValueError):
            pascal(5, 3)
