import unittest
from task_71_80 import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_71_empty_string(self):
        expected = "input string"
        output = number_71("")
        self.assertEqual(expected, output)

    def test_number_71_correct(self):
        expected = 5
        output = number_71("8-3")
        self.assertEqual(expected, output)

    def test_number_72_empty_list(self):
        expected = "input list"
        output = number_72_73([], 0)
        self.assertEqual(expected, output)

    def test_number_72_empty_element(self):
        expected = "input element to search for"
        output = number_72_73([1, 2, 3], None)
        self.assertEqual(expected, output)

    def test_number_72_empty_all(self):
        expected = "input element and list"
        output = number_72_73([], None)
        self.assertEqual(expected, output)

    def test_number_72_correct(self):
        expected = 4
        output = number_72_73([2, 5, 7, 9, 11, 17, 222],11)
        self.assertEqual(expected, output)

    def test_number_74_check(self):
        self.assertTrue(10 <= number_74() <= 100)

    def test_number_75_check(self):
        self.assertTrue(5 <= number_75() <= 95)

    def test_number_76(self):
        lst = [0, 2, 4, 6, 8, 10]
        self.assertIn(number_76(), lst)

    def test_number_77_boundary(self):
        self.assertTrue(0 <= number_77() <= 11)

    def test_number_77_is_zero(self):
        self.assertEqual(0, number_77())

    def test_number_78_length(self):
        expected = 5
        output = len(number_78())
        self.assertEqual(output, expected)

    def test_number_78_boundary(self):
        output = number_78()
        for i in output:
            self.assertTrue(100 <= i <= 201)

    def test_number_79_length(self):
        expected = 5
        output = len(number_79())
        self.assertEqual(output, expected)

    def test_number_79_boundary(self):
        output = number_79()
        for i in output:
            self.assertTrue(100 <= i <= 201)

    def test_number_79_even(self):
        output = number_79()
        for i in output:
            self.assertTrue(i % 2 == 0)

    def test_number_80_length(self):
        expected = 5
        output = len(number_80())
        self.assertEqual(output, expected)

    def test_number_80_boundary(self):
        output = number_80()
        for i in output:
            self.assertTrue(1 <= i <= 1001)

    def test_number_80_divisible(self):
        output = number_80()
        for i in output:
            self.assertTrue(i % 5 == 0 and i % 7 == 0)


if __name__ == '__main__':
    unittest.main()
