import unittest
from task_11_20 import *


class Task20(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_11_on_nul(self):
        expected = ['0']
        actual = number_11("0")
        self.assertEqual(expected, actual)

    def test_number_11_on_one(self):
        expected = []
        actual = number_11("1")
        self.assertEqual(expected, actual)

    def test_number_11_on_one_divided_value(self):
        expected = ['1010']
        actual = number_11("0100,0011,1010,1001")
        self.assertEqual(expected, actual)

    def test_number_11_on_more_divided_values(self):
        expected = ['1010', '1010']
        actual = number_11("0100,0011,1010,1001,1010")
        self.assertEqual(expected, actual)

    def test_number_11_empty_input(self):
        expected = "Please, fill input"
        actual = number_11()
        self.assertEqual(expected, actual)

    def test_number_12_first_value(self):
        output = number_12()
        output = output.split(",")
        expected = 2000
        actual = int(output[0])
        self.assertEqual(expected, actual)

    def test_number_12_last_value(self):
        output = number_12()
        output = output.split(",")
        expected = 2888
        actual = int(output[len(output) - 1])
        self.assertEqual(expected, actual)

    def test_number_12_invalid(self):
        output = number_12()
        output = output.split(",")
        notIn = 2001
        self.assertNotIn(notIn, output)

    def test_number_13_correct_string(self):
        output = number_13("hello world! 123")
        expected = "LETTER 10" + "\n" + "NUMBERS 3"
        self.assertEqual(output, expected)

    def test_number_13_empty_string(self):
        output = number_13("")
        expected = "LETTER 0" + "\n" + "NUMBERS 0"
        self.assertEqual(output, expected)

    def test_number_13_only_char(self):
        output = number_13("tratata")
        expected = "LETTER 7" + "\n" + "NUMBERS 0"
        self.assertEqual(output, expected)

    def test_number_13_only_numbers(self):
        output = number_13("111")
        expected = "LETTER 0" + "\n" + "NUMBERS 3"
        self.assertEqual(output, expected)

    def test_number_13_negative_number(self):
        output = number_13("-1")
        expected = "LETTER 0" + "\n" + "NUMBERS 1"
        self.assertEqual(output, expected)

    def test_number_13_non_latin(self):
        output = number_13("укр")
        expected = "LETTER 3" + "\n" + "NUMBERS 0"
        self.assertEqual(output, expected)

    def test_number_13_non_latin_negative(self):
        output = number_13("укр-1")
        expected = "LETTER 3" + "\n" + "NUMBERS 1"
        self.assertEqual(output, expected)

    def test_number_14_correct_string(self):
        output = number_14("Hello world!")
        expected = "upper: 1" + "\n" + "lower: 9"
        self.assertEqual(output, expected)

    def test_number_14_empty_string(self):
        output = number_14("")
        expected = "upper: 0" + "\n" + "lower: 0"
        self.assertEqual(output, expected)

    def test_number_14_numbers(self):
        output = number_14("123")
        expected = "upper: 0" + "\n" + "lower: 0"
        self.assertEqual(output, expected)

    def test_number_14_only_special_char(self):
        output = number_14("!!!")
        expected = "upper: 0" + "\n" + "lower: 0"
        self.assertEqual(output, expected)

    def test_number_14_non_latin(self):
        output = number_14("Катя")
        expected = "upper: 1" + "\n" + "lower: 3"
        self.assertEqual(output, expected)

    def test_number_15_set_null(self):
        output = number_15("0")
        expected = 0
        self.assertEqual(output, expected)

    def test_number_15_set_negative(self):
        output = number_15("-1")
        expected = "Please, input positive number"
        self.assertEqual(output, expected)

    def test_number_15_set_positive(self):
        output = number_15("9")
        expected = 11106
        self.assertEqual(output, expected)

    def test_number_16_zero_value(self):
        output = "Please, input non-zero value"
        expected = number_16("0")
        self.assertEqual(output, expected)

    def test_number_16_negative_value(self):
        output = "1,9,25"
        expected = number_16("-1,-3,-5")
        self.assertEqual(output, expected)

    def test_number_16_invalid_type(self):
        output = ValueError
        expected = number_16("tratata")
        self.assertEqual(output, expected)

    def test_number_16_positive_value(self):
        output = "1,9,25,49,81"
        expected = number_16("1,2,3,4,5,6,7,8,9")
        self.assertEqual(output, expected)

    def test_number_18_all_invalid(self):
        output = "All passwords are invalid"
        expected = number_18("a F1#,2w3E*,2We3345")
        self.assertEqual(output, expected)

    def test_number_18_empty_string(self):
        output = "Please, input password"
        expected = number_18("")
        self.assertEqual(output, expected)

    def test_number_18_correct(self):
        output = "ABd1234@1"
        expected = number_18("ABd1234@1,a F1#,2w3E*,2We3345")
        self.assertEqual(output, expected)

    def test_number_19_check_equal_names_and_age(self):
        output = [('John', '20', '91'), ('John', '20', '90')]
        expected = number_19("John,20,91 John,20,90")
        self.assertEqual(output, expected)

    def test_number_19_check_equal_names_and_score(self):
        output = [('John', '20', '90'), ('John', '21', '90')]
        expected = number_19("John,21,90 John,20,90")
        self.assertEqual(output, expected)

    def test_number_19_empty(self):
        output = "Please, input string"
        expected = number_19("")
        self.assertEqual(output, expected)

    def test_number_20_correct(self):
        cl = Twenty()
        output = cl.number_20(20)
        expected = [0, 7, 14]
        self.assertEqual(output, expected)

    def test_number_20_null(self):
        cl = Twenty()
        output = cl.number_20(0)
        expected = [0]
        self.assertEqual(output, expected)

    def test_number_20_negative(self):
        cl = Twenty()
        output = cl.number_20(-7)
        expected = "Please, input positive character"
        self.assertEqual(output, expected)

