import unittest
from task_81_90 import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_number_81_check_boundaries(self):
        self.assertTrue(7 <= number_81() <= 15)

    def test_number_81_is_int(self):
        self.assertIsInstance(number_81(), int)

    def test_number_86(self):
        correct = [['I', 'Play', 'Hockey'], ['I', 'Play', 'Football'], ['I', 'Love', 'Hockey'],
                   ['I', 'Love', 'Football'], ['You', 'Play', 'Hockey'], ['You', 'Play', 'Football'],
                   ['You', 'Love', 'Hockey'], ['You', 'Love', 'Football']]
        self.assertEqual(correct, number_86())

    def test_number_87_check_odd(self):
        output = number_87()
        for i in output:
            self.assertTrue(i % 2 != 0)

    def test_number_87_check_belong(self):
        output = number_87()
        for i in output:
            self.assertIn(i, [5,6,77,45,22,12,24])

    def test_number_88_check_divisible(self):
        output = number_88()
        for i in output:
            self.assertTrue(i % 5 != 0 and i % 7 != 0)

    def test_number_88_check_belong(self):
        output = number_88()
        for i in output:
            self.assertIn(i, [12,24,35,70,88,120,155])

    def test_number_89_check_indexes(self):
        lst = [12, 24, 35, 70, 88, 120, 155]
        ind = [0,2,4,6]
        for i in ind:
            self.assertIn(lst[i] , number_89())

    def test_number_90_first_dimension(self):
        expected = 3
        out = len(number_90())
        self.assertEqual(expected, out)

    def test_number_90_second_dimension(self):
        expected = 5
        out = len(number_90()[0])
        self.assertEqual(expected, out)

    def test_number_90_third_dimension(self):
        expected = 8
        out = len(number_90()[0][0])
        self.assertEqual(expected, out)







if __name__ == '__main__':
    unittest.main()
