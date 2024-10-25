import unittest

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

# Unit tests for the calculator
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(7, 6), 42)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == '__main__':
    unittest.main()
