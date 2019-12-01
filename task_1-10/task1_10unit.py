import unittest
from unittest import mock
from unittest.mock import patch

from task_1_10 import *


class Task10(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_one_valid_1(self):
        expected_result = 2002
        actual_result = number_1()
        self.assertIn(expected_result, actual_result)

    def test_one_valid_2(self):
        expected_result = 2541
        actual_result = number_1()
        self.assertIn(expected_result, actual_result)

    def test_one_valid_3(self):
        expected_result = 3199
        actual_result = number_1()
        self.assertIn(expected_result, actual_result)

    def test_one_invalid(self):
        not_expected = 2007
        actual_result = number_1()
        self.assertNotIn(not_expected, actual_result)

    def test_one_invalid_1(self):
        not_expected = 1999
        actual_result = number_1()
        self.assertNotIn(not_expected, actual_result)

    def test_one_invalid_2(self):
        not_expected = 3202
        actual_result = number_1()
        self.assertNotIn(not_expected, actual_result)

    def test_two_on_zero(self):
        expected = 1
        actual = number_2(0)
        self.assertEqual(expected, actual)

    def test_two_on_minus(self):
        actual = number_2(-1)
        self.assertRaises(ValueError, actual)

    def test_two_on_positive(self):
        expected = 6
        actual = number_2(3)
        self.assertEqual(expected, actual)

    def test_three_on_zero(self):
        actual = number_3(0)
        self.assertEqual(ValueError, actual)

    def test_three_on_minus(self):
        actual = number_3(-1)
        self.assertRaises(ValueError, actual)

    def test_three_on_positive(self):
        actual = number_3(8)
        expected = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
        self.assertEqual(expected, actual)

    def test_four_positive(self):
        expected = print(['1', '2', '3']), print(('1', '2', '3'))
        actual = number_4("1,2,3")
        self.assertEqual(expected, actual)

    def test_four_check_tuple_representation(self):
        expected = print(['1']), print(('1',))
        actual = number_4("1")
        self.assertEqual(expected, actual)

    # def test_five(self):
    #     instance = Mystring().getString()

    def test_six_on_minus(self):
        expected = "Value should be positive"
        actual = number_6("-1")
        self.assertEqual(expected, actual)

    def test_six_one_positive_number(self):
        expected = "5"
        actual = number_6("8")
        self.assertEqual(actual, expected)

    def test_six_more_positive_numbers(self):
        expected = "18,22,24"
        actual = number_6("100,150,180")
        self.assertEqual(expected, actual)

    def test_six_positive_and_negative(self):
        expected = "All values should be positive"
        actual = number_6("100,150,180,-3")
        self.assertEqual(expected, actual)

    def test_seven_one_null(self):
        expected = "You should enter two values"
        actual = number_7("0")
        self.assertEqual(expected, actual)

    def test_seven_two_nulls(self):
        expected = []
        actual = number_7("0,0")
        self.assertEqual(expected, actual)

    def test_seven_minus_values(self):
        expected = "You'd enter positive numbers"
        actual = number_7("-1,-2")
        self.assertEqual(expected, actual)

    def test_seven_correct_values(self):
        expected = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
        actual = number_7("3,5")
        self.assertEqual(expected, actual)

    def test_eight_empty_string(self):
        expected = "Please, input full string"
        actual = number_8("")
        self.assertEqual(expected, actual)

    def test_eight_one_word(self):
        expected = "ok"
        actual = number_8("ok")
        self.assertEqual(expected, actual)

    def test_eight_non_latin(self):
        expected = "ананас,банан"
        actual = number_8("банан,ананас")
        self.assertEqual(expected, actual)

    def test_eight_latin(self):
        expected = "bag,hello,without,world"
        actual = number_8("without,hello,bag,world")
        self.assertEqual(expected, actual)

    def test_eight_if_first_letter_is_equal(self):
        expected = "fa,fu"
        actual = number_8("fu,fa")
        self.assertEqual(expected, actual)

    def test_nine_empty(self):
        expected = "Please, input full string"
        actual = number_9("")
        self.assertEqual(expected, actual)

    def test_nine_non_latin(self):
        expected = "АНАНАС,БАНАН"
        actual = number_9("ананас,банан")
        self.assertEqual(expected, actual)

    def test_nine_latin(self):
        expected = "HEY"
        actual = number_9("hey")
        self.assertEqual(expected, actual)

    def test_ten_empty(self):
        expected = "Please, input full string"
        actual = number_10("")
        self.assertEqual(expected, actual)

    def test_ten_check_duplicates(self):
        string = "hello hello again again"
        self.assertEqual(number_10(string).count("hello") + number_10(string).count("again"), 2)

    def test_ten_check_sorting(self):
        string = "hello hello again again"
        actual = number_10(string)
        expected = "again hello"
        self.assertEqual(expected, actual)

    def test_ten_if_first_letter_is_equal(self):
        expected = "fa fu"
        actual = number_10("fu fa")
        self.assertEqual(expected, actual)

    def test_ten_non_latin(self):
        expected = "ананас банан"
        actual = number_10("банан ананас банан")
        self.assertEqual(expected, actual)


if __name__ == 'main':
    unittest.main()
