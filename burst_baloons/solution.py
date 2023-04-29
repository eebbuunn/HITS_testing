from typing import List


class Solution:
    def maxCoins(self, nums: List[int or float]) -> int or float:

        _check_is_list_of_nums(nums)

        _check_is_nums_count_is_valid(nums)

        _check_is_nums_are_valid(nums)

        cache = {}
        nums = [1] + nums + [1]

        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)


def _check_is_nums_are_valid(nums):
    if not all(map(lambda num: 0 <= num <= 100, nums)):
        raise ValueError


def _check_is_nums_count_is_valid(nums):
    if not 1 <= len(nums) <= 300:
        raise ValueError


def _check_is_list_of_nums(nums):
    if not isinstance(nums, list) or not all(map(lambda num: isinstance(num, int), nums)) and not all(
            map(lambda num: isinstance(num, float), nums)):
        raise ValueError

