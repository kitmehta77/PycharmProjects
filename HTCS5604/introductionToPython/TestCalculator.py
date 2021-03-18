import unittest
import HTCS5604.introductionToPython.calculation as g

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = g.add(5,6)
        self.assertEqual(11,result)

if __name__ == '__main__':
    unittest.main()