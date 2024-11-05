from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        result = [0] * len(nums)

        k = 0

        for index in range(len(nums)):
            if nums[index] != val:
                result[k] = nums[index]

                k += 1

        for index in range(len(result)):
            nums[index] = result[index]

        return k


def test_case():

    solution = Solution()

    nums = [3, 2, 2, 3]

    assert solution.removeElement(nums, 3) == 2
    assert nums == [2, 2, 0, 0]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    assert solution.removeElement(nums, 2) == 5
    assert nums == [0, 1, 3, 0, 4, 0, 0, 0]
