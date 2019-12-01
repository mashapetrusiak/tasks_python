import unittest
from task_1_10 import *

class Task10(unittest.TestCase):

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
        expected = print(['1']),print(('1',))
        actual = number_4("1")
        self.assertEqual(expected, actual)
