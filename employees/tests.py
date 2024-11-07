import unittest
from .main import sum_func, divide


class TestFunctions(unittest.TestCase):

    def test_sum_func(self):
        a = 5
        b = 3
        expected_result = 8
        actual_result = sum_func(a, b)
        self.assertEqual(expected_result, actual_result)
    
    def test_divide(self):
        a=6
        b=2
        expected_result = 3
        actual_result = divide(a, b)
        self.assertEqual(expected_result, actual_result)
    

    def test_divide_by_zero(self):
        a = 5
        b = 0
        with self.assertRaises(ZeroDivisionError):
            divide(a, b)


if __name__ == '__main__':
    unittest.main()