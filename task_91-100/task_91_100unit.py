import unittest
from task_91_100 import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_91_check_indexes(self):
        lst = [12, 24, 35, 70, 88, 120, 155]
        ind = [0, 4, 5]
        for i in ind:
            self.assertIn(lst[i], number_91())

    def test_number_92_24_not_present_in_result(self):
        expected = 24
        output = number_92()
        self.assertNotIn(expected, output)

    def test_number_92_check_another_values_present(self):
        expected = [12, 35, 88, 120, 155]
        output = number_92()
        self.assertNotIn(expected, output)

    def test_number_93_correct(self):
        expected = [35]
        output = number_93()
        self.assertEqual(expected, output)

    def test_number_94_counts(self):
        lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
        for i in lst:
            self.assertEqual(number_94().count(i), 1)

    def test_number_95_subclass_check_female(self):
        self.assertTrue(issubclass(Female, Person))

    def test_number_95_subclass_check_male(self):
        self.assertTrue(issubclass(Male, Person))

    def test_number_95_check_get_gender_person(self):
        person = Person()
        self.assertEqual("Unknown", person.getGender())

    def test_number_95_check_get_gender_male(self):
        person = Male()
        self.assertEqual("Male", person.getGender())

    def test_number_95_check_get_gender_female(self):
        person = Female()
        self.assertEqual("Female", person.getGender())

    def test_number_96_check_empty_string(self):
        expected = "Please, input string"
        output = number_96("")
        self.assertEqual(expected, output)

    def test_number_96_check_length(self):
        string = "abcdefgabc"
        expected = len(set(string))
        output = len(number_96("abcdefgabc"))
        self.assertEqual(expected, output)

    def test_number_96_check_numbers(self):
        output = number_96("1223")
        expected = [('1', 1), ('2', 2), ('3', 1)]
        self.assertEqual(expected, output)

    def test_number_96_check_words(self):
        output = number_96("abbc")
        expected = [('a', 1), ('b', 2), ('c', 1)]
        self.assertEqual(expected, output)

    def test_number_97_check_length(self):
        output = len(number_97("abc"))
        expected = 3
        self.assertEqual(expected, output)

    def test_number_97_check_belong(self):
        strin = "abc"
        for i in strin:
            self.assertIn(i, number_97(strin))

    def test_number_97_check_correct(self):
        expected = "cba"
        output = number_97("abc")
        self.assertEqual(expected, output)

    def test_number_98_check_even_indexes(self):
        strin = "H1e2l3l4o5w6o7r8l9d"
        for i in range(0, len(strin)):
            if i % 2 == 1:
                self.assertNotIn(strin[i], number_98(strin))

    def test_number_99_check_length(self):
        leng = 6
        self.assertEqual(leng, len(number_99()))

    def test_number_99_check_correct(self):
        expected = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
        output = number_99()
        self.assertEqual(expected, output)

    def test_number_100_check_correctness(self):
        expected = (12, 23)
        output = number_100()
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
