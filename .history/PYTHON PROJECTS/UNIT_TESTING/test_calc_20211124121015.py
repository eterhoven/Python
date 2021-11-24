import unittest
import calc

class Testcalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)

if __name__ == '__main__':
    unittest.main()