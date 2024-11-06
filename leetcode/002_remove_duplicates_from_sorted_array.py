from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        last = None

        result = [0] * len(nums)

        k = 0

        for index in range(len(nums)):

            if nums[index] != last:
                last = nums[index]
                result[k] = nums[index]
                k += 1

        for index in range(len(result)):
            nums[index] = result[index]

        return k


def test_case():

    solution = Solution()

    nums = [1, 1, 2]

    assert solution.removeDuplicates(nums) == 2
    assert nums == [1, 2, 0]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    assert solution.removeDuplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]
