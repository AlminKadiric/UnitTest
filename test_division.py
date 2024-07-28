import unittest
from division import Division


class TestDivision(unittest.TestCase):
    
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            Division.division(10, 0)
    
    def test_string_input_first(self):
        with self.assertRaises(ValueError):
            Division.division("10", 5)
    
    def test_string_input_second(self):
        with self.assertRaises(ValueError):
            Division.division(10, "5")
    
    def test_string_input_both(self):
        with self.assertRaises(ValueError):
            Division.division("10", "5")

# Pokretanje testova
if __name__ == '__main__':
    unittest.main()
