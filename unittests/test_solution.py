from burst_baloons import solution
from unittest import TestCase


# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an
# array nums. You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of
# bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.


class _TestSuite(TestCase):
    def setUp(self) -> None:
        self.SUT = solution.Solution.maxCoins


class TestSolution(_TestSuite):
    # Example 1:
    # Input: nums = [3, 1, 5, 8]
    # Output: 167
    def test_burst_baloons_4_nums(self):
        nums = [3, 1, 5, 8]
        expected = 167

        self.assertEqual(self.SUT(self, nums), expected)

    # Example 2:
    # Input: nums = [1, 5]
    # Output: 10
    def test_burst_baloons_2_nums(self):
        nums = [1, 5]
        expected = 10

        self.assertEqual(self.SUT(self, nums), expected)


class TestInputNumsCountValidation(_TestSuite):

    # 1 <= n <= 300
    def test_nums_count_equals_1(self):
        nums = [1]
        expected = 1

        self.assertEqual(self.SUT(self, nums), expected)

    def test_nums_count_greater_than_1(self):
        nums = [1, 1]
        expected = 2

        self.assertEqual(self.SUT(self, nums), expected)

    def test_nums_count_less_than_1(self):
        nums = []

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_nums_count_less_than_300(self):
        nums = [1 for _ in range(299)]
        expected = 299

        self.assertEqual(self.SUT(self, nums), expected)

    def test_nums_count_equals_300(self):
        nums = [1 for _ in range(300)]
        expected = 300

        self.assertEqual(self.SUT(self, nums), expected)

    def test_nums_count_greater_than_300(self):
        nums = [1 for _ in range(301)]

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_nums_count_in_valid_range(self):
        nums = [1 for _ in range(100)]
        expected = 100

        self.assertEqual(self.SUT(self, nums), expected)


class TestInputNumValidation(_TestSuite):

    # 0 <= nums[i] <= 100
    def test_num_value_equals_0(self):
        nums = [0]
        expected = 0

        self.assertEqual(self.SUT(self, nums), expected)

    def test_num_value_greater_than_0(self):
        nums = [1]
        expected = 1

        self.assertEqual(self.SUT(self, nums), expected)

    def test_num_value_less_than_0(self):
        nums = [-1]

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_num_value_in_valid_range(self):
        nums = [10]
        expected = 10

        self.assertEqual(self.SUT(self, nums), expected)

    def test_num_value_less_than_100(self):
        nums = [99]
        expected = 99

        self.assertEqual(self.SUT(self, nums), expected)

    def test_num_value_equals_100(self):
        nums = [100]
        expected = 100

        self.assertEqual(self.SUT(self, nums), expected)

    def test_num_value_greater_than_100(self):
        nums = [101]

        with self.assertRaises(ValueError):
            self.SUT(self, nums)


class TestNumberIsNumber(_TestSuite):
    def test_number_is_int(self):
        nums = [1, 1, 1]
        expected = 3

        self.assertEqual(self.SUT(self, nums), expected)

    def test_number_is_float(self):
        nums = [1.5]
        expected = 1.5

        self.assertEqual(self.SUT(self, nums), expected)

    def test_number_is_char(self):
        nums = ['a']

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_number_is_string(self):
        nums = ['str']

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_number_is_unicode(self):
        nums = ['℮']

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_number_is_ascii(self):
        nums = ["!@#"]

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_number_is_emoji(self):
        nums = ['💀']

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_number_is_list(self):
        nums = [[]]

        with self.assertRaises(ValueError):
            self.SUT(self, nums)


class TestListIsList(_TestSuite):
    def test_list_is_list(self):
        nums = [1, 1, 1]
        expected = 3

        self.assertEqual(self.SUT(self, nums), expected)

    def test_list_is_dict(self):
        nums = {1: 2}

        with self.assertRaises(ValueError):
            self.SUT(self, nums)

    def test_list_is_not_list(self):
        nums = 1

        with self.assertRaises(ValueError):
            self.SUT(self, nums)
