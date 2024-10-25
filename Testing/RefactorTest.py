import unittest

def add(a, b):
    return a + b

# Original test
#class TestMathFunctions(unittest.TestCase):
#    def test_add(self):
#        self.assertEqual(add(2, 3), 5)

# Refactored test for improved readability
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
