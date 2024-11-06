from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k


def test_case():

    solution = Solution()

    nums = [3, 2, 2, 3]

    assert solution.removeElement(nums, 3) == 2
    assert nums == [2, 2, 2, 3]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    assert solution.removeElement(nums, 2) == 5
    assert nums == [0, 1, 3, 0, 4, 0, 4, 2]
