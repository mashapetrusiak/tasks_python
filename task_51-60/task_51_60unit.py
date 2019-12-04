import unittest
from task_51_60 import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_51_check_inheritance(self):
        self.assertTrue(issubclass(NewYorker, American))

    def test_number_52_check_correct_number(self):
        output = (int(Circle(10).area()))
        expected = 314
        self.assertEqual(output, expected)

    def test_number_52_check_negative_number(self):
        output = (int(Circle(-1).area()))
        expected = "Radius cannot be negative"
        self.assertEqual(output, expected)

    def test_number_52_check_zero_number(self):
        output = (int(Circle(0).area()))
        expected = "Radius cannot be zero"
        self.assertEqual(output, expected)

    def test_number_53_check_correct(self):
        output = Rectangle(3, 7).area()
        expected = 21
        self.assertEqual(output, expected)

    def test_number_53_check_zeros(self):
        output = Rectangle(0, 0).area()
        expected = "Input non-zero values"
        self.assertEqual(output, expected)

    def test_number_53_check_one_negative(self):
        output = Rectangle(6, -1).area()
        expected = "Input positive values"
        self.assertEqual(output, expected)

    def test_number_53_check_two_negative(self):
        output = Rectangle(-6, -1).area()
        expected = "Input positive values"
        self.assertEqual(output, expected)

    def test_number_54_is_subclass(self):
        self.assertTrue(issubclass(Square, Shape))

    def test_number_54_check_default_lenght_of_square(self):
        expected = 0
        output = Square().length
        self.assertEqual(expected, output)

    def test_number_54_check_default_area_of_shape(self):
        expected = 0
        output = Shape().area()
        self.assertEqual(expected, output)

    def test_number_54_check_correct(self):
        expected = 256
        output = Square(16).area()
        self.assertEqual(expected, output)

    def test_number_54_check_negative(self):
        expected = "Input positive value"
        output = Square(-4).area()
        self.assertEqual(expected, output)

    def test_number_54_check_zero(self):
        expected = "Input positive value"
        output = Square(0).area()
        self.assertEqual(expected, output)

    def test_number_55_check_error_not_shows(self):
        output = number_55()
        expected = "You are dividing a number by ZERO!"
        self.assertEqual(output, expected)

    def test_number_57_check_empty(self):
        output = number_57("")
        expected = "input your email"
        self.assertEqual(output, expected)

    def test_number_57_check_non_latin(self):
        output = number_57("катя@gmail.com")
        expected = "катя"
        self.assertEqual(output, expected)

    def test_number_57_check_correct(self):
        output = number_57("katya@gmail.com")
        expected = "katya"
        self.assertEqual(output, expected)

    def test_number_58_check_empty_string(self):
        output = number_58("")
        expected = "input your email"
        self.assertEqual(output, expected)

    def test_number_58_check_correct(self):
        output = number_58("katya@gmail.com")
        expected = "gmail"
        self.assertEqual(output, expected)

    def test_number_59_empty_string(self):
        output = "input string"
        expected = number_59("")
        self.assertEqual(output, expected)

    def test_number_59_only_numbers(self):
        output = ['1', '23', '67']
        expected = number_59(" 1 23 67")
        self.assertEqual(output, expected)

    def test_numbers_59_num_and_str(self):
        output = ['1', '23', '67']
        expected = number_59("t1 t23 t67")
        self.assertEqual(output, expected)

    def test_numbers_59_num_and_str_separated_by_space(self):
        output = ['2', '3']
        expected = number_59("2 cats and 3 dogs")
        self.assertEqual(output, expected)

    def test_number_60_correct(self):
        self.assertEqual(number_60(), "hello world!")


if __name__ == '__main__':
    unittest.main()
