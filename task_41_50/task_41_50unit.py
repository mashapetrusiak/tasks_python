import unittest
from task_41_50 import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_41_check_first(self):
        output = number_41()
        expected = 1
        self.assertIn(expected, output)

    def test_number_41_check_last(self):
        output = number_41()
        expected = 400
        self.assertIn(expected, output)

    def test_number_41_check_last_range(self):
        output = number_41()
        expected = 441
        self.assertNotIn(expected, output)

    def test_number_41_check_first_range(self):
        output = number_41()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_42_check_equality(self):
        output = number_42()
        expected = "(1, 2, 3, 4, 5)" + '\n' + "(6, 7, 8, 9, 10)"
        self.assertEqual(expected, output)

    def test_number_43_check_first(self):
        output = number_43()
        expected = 2
        self.assertIn(expected, output)

    def test_number_43_check_last(self):
        output = number_43()
        expected = 10
        self.assertIn(expected, output)

    def test_number_43_check_not_in(self):
        output = number_43()
        expected = 3
        self.assertNotIn(expected, output)

    def test_number_43_check_range(self):
        output = number_43()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_43_check_range_end(self):
        output = number_43()
        expected = 11
        self.assertNotIn(expected, output)

    def test_number_44_check_yes(self):
        output = number_44("yes")
        expected = "Yes"
        self.assertEqual(output, expected)

    def test_number_44_check_Yes(self):
        output = number_44("Yes")
        expected = "Yes"
        self.assertEqual(output, expected)

    def test_number_44_check_YES(self):
        output = number_44("YES")
        expected = "Yes"
        self.assertEqual(output, expected)

    def test_number_44_check_no(self):
        output = number_44("no")
        expected = "No"
        self.assertEqual(output, expected)

    def test_number_44_check_another_value(self):
        output = number_44("12")
        expected = "No"
        self.assertEqual(output, expected)

    def test_number_44_check_another_value_word(self):
        output = number_44("tut")
        expected = "No"
        self.assertEqual(output, expected)

    def test_number_45_check_equality(self):
        output = number_45()
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(output, expected)

    def test_number_46_check_first(self):
        output = number_46()[0]
        expected = 1
        self.assertEqual(output, expected)

    def test_number_46_check_last(self):
        output = number_46()[len(number_46()) - 1]
        expected = 100
        self.assertEqual(output, expected)

    def test_number_46_check_range_first(self):
        output = number_46()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_46_check_range_last(self):
        output = number_46()
        expected = 121
        self.assertNotIn(expected, output)

    def test_number_47_check_equality(self):
        self.assertEqual(number_47(), [4, 16, 36, 64, 100])

    def test_number_48_check_first(self):
        output = number_48()[0]
        expected = 2
        self.assertEqual(output, expected)

    def test_number_48_check_last(self):
        output = number_48()[len(number_48()) - 1]
        expected = 20
        self.assertEqual(output, expected)

    def test_number_48_check_range_first(self):
        output = number_48()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_48_check_range_last(self):
        output = number_48()
        expected = 22
        self.assertNotIn(expected, output)

    def test_number_49_check_first(self):
        output = number_49()[0]
        expected = 1
        self.assertEqual(output, expected)

    def test_number_49_check_last(self):
        output = number_49()[len(number_49()) - 1]
        expected = 400
        self.assertEqual(output, expected)

    def test_number_49_check_range_first(self):
        output = number_49()
        expected = 0
        self.assertNotIn(expected, output)

    def test_number_49_check_range_last(self):
        output = number_49()
        expected = 441
        self.assertNotIn(expected, output)

    def test_number_50_check_method_as_instance(self):
        output = American().printNationality()
        expected = "I am American"
        self.assertEqual(output, expected)

    def test_number_50_check_method_as_class(self):
        output = American.printNationality()
        expected = "I am American"
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
