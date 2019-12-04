import unittest
from task_61_70 import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_61_62_empty_string(self):
        output = number_61_62("")
        expected = "input string"
        self.assertEqual(expected, output)

    def test_number_61_62_correct(self):
        output = number_61_62("hello")
        expected = b'hello'
        self.assertEqual(expected, output)

    def test_number_63_zero(self):
        output = number_63(0)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_63_negative_value(self):
        output = number_63(-1)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_63_correct_value(self):
        output = number_63(5)
        expected = 3.55
        self.assertEqual(expected, output)

    def test_number_64_zero(self):
        output = number_64(0)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_64_negative_value(self):
        output = number_64(-1)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_64_correct_value(self):
        output = number_64(5)
        expected = 500
        self.assertEqual(expected, output)

    def test_number_65_66_negative_value(self):
        output = number_65_66(-1)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_65_66_correct_value(self):
        output = number_65_66(7)
        expected = 13
        self.assertEqual(expected, output)

    def test_number_69_negative(self):
        output = number_69(-1)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_69_zero(self):
        output = number_69(0)
        expected = "number should be more that zero"
        self.assertEqual(expected, output)

    def test_number_69_positive(self):
        output = number_69(100)
        expected = "0,35,70"
        self.assertEqual(expected, output)




if __name__ == '__main__':
    unittest.main()
