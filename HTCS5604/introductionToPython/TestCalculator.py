import unittest
import HTCS5604.introductionToPython.calculation as g

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = g.add(5,6)
        self.assertEqual(11,result)

    def test_subtract(self):
        result = g.subtract(8,2)
        self.assertEqual(6,result)

    def test_multiply(self):
        result = g.multiply(10,3)
        self.assertEqual(30,result)

    def test_division(self):
        result = g.divide(10,2)
        self.assertEqual(5,result)

    def test_power(self):
        result = g.power(2,2)
        self.assertEqual(4,result)

if __name__ == '__main__':
    unittest.main()