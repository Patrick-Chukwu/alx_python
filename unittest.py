import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_multiply(self):
        result = self.calculator.multiply(3, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
