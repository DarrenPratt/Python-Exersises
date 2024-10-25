import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_not_equal(self):
        self.assertNotEqual(add(2, 3), 6)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
