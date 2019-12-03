import unittest
from task_21_30 import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_21_empty_string(self):
        expected = "Please, fill the string"
        output = number_21("")
        self.assertEqual(expected, output)

    def test_number_21_all_equal(self):
        expected = 0
        output = number_21("UP 5 DOWN 5 LEFT 5 RIGHT 5")
        self.assertEqual(expected, output)

    def test_number_21_negative_numbers(self):
        expected = 2
        output = number_21("UP -5 DOWN -3 LEFT -3 RIGHT -2")
        self.assertEqual(expected, output)

    def test_number_22_empty_string(self):
        expected = "Please, fill the string"
        output = number_22("")
        self.assertEqual(expected, output)

    def test_number_22_only_number(self):
        expected = [('12', 1), ('23', 1), ('45', 2)]
        output = number_22("12 23 45 45")
        self.assertEqual(expected, output)

    def test_number_22_only_words(self):
        expected = [('e', 1), ('r', 2), ('w', 1)]
        output = number_22("w r r e")
        self.assertEqual(expected, output)

    def test_number_22_non_latin(self):
        expected = [('ааа', 1), ('ффф', 2)]
        output = number_22("ффф ффф ааа")
        self.assertEqual(expected, output)

    def test_number_22_words_and_digits(self):
        expected = [('111', 1), ('222', 1), ('ааа', 1)]
        output = number_22("111 ааа 222")
        self.assertEqual(expected, output)

    def test_number_23_empty(self):
        expected = ValueError
        output = number_22("")
        self.assertEqual(expected, output)

    def test_number_23_positive(self):
        expected = 9
        output = number_22(3)
        self.assertEqual(expected, output)

    def test_number_23_negative(self):
        expected = 1
        output = number_23(-1)
        self.assertEqual(expected, output)

    def test_number_23_zero(self):
        expected = 0
        output = number_23(0)
        self.assertEqual(expected, output)

    def test_number_26_zeros(self):
        expected = 0
        output = number_26(0,0)
        self.assertEqual(expected, output)

    def test_number_26_negative(self):
        expected = 1
        output = number_26(-1,2)
        self.assertEqual(expected, output)

    def test_number_26_all_negative(self):
        expected = -8
        output = number_26(-5,-3)
        self.assertEqual(expected, output)

    def test_number_27_28_set_str(self):
        expected = "lol"
        output = number_27_28("lol")
        self.assertEqual(expected, output)

    def test_number_27_28_set_int(self):
        expected = "8"
        output = number_27_28(8)
        self.assertEqual(expected, output)

    def test_number_27_28_negative(self):
        expected = "-1"
        output = number_27_28(-1)
        self.assertEqual(expected, output)

    def test_number_29_zeros(self):
        expected = 0
        output = number_29("0","0")
        self.assertEqual(expected, output)

    def test_number_29_negative(self):
        expected = 1
        output = number_29("-1","2")
        self.assertEqual(expected, output)

    def test_number_29_all_negative(self):
        expected = -8
        output = number_29("-5","-3")
        self.assertEqual(expected, output)

    def test_number_30_empty_string(self):
        expected = "Please, input strings"
        output = number_30("", "")
        self.assertEqual(expected, output)

    def test_number_30_negative(self):
        expected = "-123"
        output = number_30("-12", "3")
        self.assertEqual(expected, output)

    def test_number_30_positive(self):
        expected = "123"
        output = number_30("12", "3")
        self.assertEqual(expected, output)




if __name__ == '__main__':
    unittest.main()
