import unittest
import calc

class Testcalc(unittest.TestCase):
    
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)