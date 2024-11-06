from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # We can do this instead of having a set that gathers all the seen
        # numbers because the numbers in nums are sorted incrementally.
        last = None

        k = 0

        for num in nums:

            if num != last:
                nums[k] = num
                last = num
                k += 1

        return k


def test_case():

    solution = Solution()

    nums = [1, 1, 2]

    assert solution.removeDuplicates(nums) == 2
    assert nums == [1, 2, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    assert solution.removeDuplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
