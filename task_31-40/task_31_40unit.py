import unittest
from task_31_40 import *

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_31_two_words_equal(self):
        output = number_31("katya nasya")
        expected = 'katya' + '\n' + 'nasya'
        self.assertEqual(output, expected)

    def test_number_31_more_than_two_words(self):
        output = "Please, input only two words"
        expected = number_31("katya nastya masha")
        self.assertEqual(output, expected)

    def test_number_31_empty_string(self):
        output = "Please, input two words"
        expected = number_31("")
        self.assertEqual(output, expected)

    def test_number_31_only_numbers(self):
        output = number_31("123 456")
        expected = '123' + '\n' + '456'
        self.assertEqual(output, expected)

    def test_number_31_with_numbers(self):
        output = number_31("hd2 ld5")
        expected = 'hd2' + '\n' + 'ld5'
        self.assertEqual(output, expected)

    def test_number_31_another_separator(self):
        output = number_31("hello, ddg")
        expected = "Please, input string separated by space"
        self.assertEqual(output, expected)

    def test_number_32_empty_string(self):
        output = number_32("")
        expected = "Please, type the value"
        self.assertEqual(output, expected)

    def test_number_32_zero(self):
        output = number_32("0")
        expected = "It is an even number"
        self.assertEqual(output, expected)

    def test_number_32_negative_even(self):
        output = number_32("-2")
        expected = "It is an even number"
        self.assertEqual(output, expected)

    def test_number_32_negative_odd(self):
        output = number_32("-1")
        expected = "It is an odd number"
        self.assertEqual(output, expected)

    def test_number_32_positive_odd(self):
        output = number_32("33")
        expected = "It is an odd number"
        self.assertEqual(output, expected)

    def test_number_32_positive_even(self):
        output = number_32("84")
        expected = "It is an even number"
        self.assertEqual(output, expected)

    def test_number_32_input_char(self):
        output = number_32("mum")
        expected = ValueError
        self.assertEqual(output, expected)

    def test_number_33_check_correct(self):
        output = number_33()
        expected = {1: 1, 2: 4, 3: 9}
        self.assertEqual(output, expected)

    def test_number_34_check_first(self):
        output = number_34()
        expected = 1
        self.assertEqual(output[1], expected)

    def test_number_34_check_last(self):
        output = number_34()
        expected = 400
        self.assertEqual(output[len(output)], expected)

    def test_number_34_check_middle(self):
        output = number_34()
        expected = 100
        self.assertEqual(output[len(output)//2], expected)

    def test_number_34_check_keys_range_last(self):
        self.assertNotIn(21, number_34().keys())

    def test_number_34_check_keys_range_first(self):
        self.assertNotIn(0, number_34().keys())

    def test_number_35_check_first(self):
        output = number_35()
        expected = 1
        self.assertIn(expected, output)

    def test_number_35_check_last(self):
        output = number_35()
        expected = 400
        self.assertIn(expected, output)

    def test_number_35_check_last_range(self):
        output = number_35()
        expected = 441
        self.assertNotIn(expected, output)

    def test_number_35_check_first_range(self):
        output = number_35()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_36_check_first(self):
        output = number_36()
        expected = 1
        self.assertIn(expected, output)

    def test_number_36_check_last(self):
        output = number_36()
        expected = 20
        self.assertIn(expected, output)

    def test_number_36_check_last_range(self):
        output = number_36()
        expected = 21
        self.assertNotIn(expected, output)

    def test_number_36_check_first_range(self):
        output = number_36()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_37_check_first(self):
        output = number_37()
        expected = 1
        self.assertIn(expected, output)

    def test_number_37_check_last(self):
        output = number_37()
        expected = 400
        self.assertIn(expected, output)

    def test_number_37_check_last_range(self):
        output = number_37()
        expected = 441
        self.assertNotIn(expected, output)

    def test_number_37_check_first_range(self):
        output = number_37()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_38_check_equality(self):
        self.assertEqual(number_38(), [1, 4, 9, 16, 25])

    def test_number_39_check_equality(self):
        self.assertEqual(number_39(), [256, 289, 324, 361, 400])

    def test_number_40_check_first(self):
        output = number_40()
        expected = 49
        self.assertIn(expected, output)

    def test_number_40_check_last(self):
        output = number_40()
        expected = 400
        self.assertIn(expected, output)

    def test_number_40_first_five_not_contain(self):
        output = number_40()
        expected = [1, 4, 9, 16, 25]
        self.assertNotIn(expected, output)

    def test_number_40_out_of_range(self):
        expected = 441
        output = number_40()
        self.assertNotIn(expected, output)




if __name__ == '__main__':
    unittest.main()
