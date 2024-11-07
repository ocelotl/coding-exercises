from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        before_last = None
        last = None

        index_0 = 0
        index_1 = 0

        k = 0

        while True:

            if index_1 == len(nums):
                break

            num = nums[index_1]

            if before_last is None:
                before_last = num

                index_0 += 1
                index_1 += 1

                k += 1

            elif last is None:
                last = num

                index_0 += 1
                index_1 += 1

                k += 1

            elif num == before_last and num == last:

                index_1 += 1

            else:

                before_last = last
                last = num
                nums[index_0] = num
                index_0 += 1
                index_1 += 1

                k += 1

        for _ in range(len(nums) - k):
            nums.pop(-1)

        return k


def test_case():

    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]

    assert solution.removeDuplicates(nums) == 5
    assert nums == [1, 1, 2, 2, 3]
