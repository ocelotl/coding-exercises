from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        m = None
        c = 0

        # This is the Boyer-Moore algorithm, used here to solve this problem in
        # O(1) space.
        for num in nums:
            if c == 0:
                m = num
                c = 1
            elif m == num:
                c += 1
            else:
                c -= 1

        return m


def test_case():

    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]

    assert solution.removeDuplicates(nums) == 5
    assert nums == [1, 1, 2, 2, 3]
