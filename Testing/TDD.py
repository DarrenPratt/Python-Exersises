import unittest

# Start by writing the test for a function that calculates the square of a number
class TestMathFunctions(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)

# Now implement the function
def square(n):
    return n * n

if __name__ == '__main__':
    unittest.main()
