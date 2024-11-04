from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m_: int, nums2: List[int], n_: int
    ) -> None:

        from ipdb import set_trace
        set_trace

        result = []

        index_nums1 = 0
        index_nums2 = 0

        nums1_ = nums1[:m_]

        if not nums1 or not nums1_:
            for element in nums2:
                nums1.append(element)

            return

        if not nums2:
            return

        while True:

            nums1_element = nums1_[index_nums1]
            nums2_element = nums2[index_nums2]

            if nums1_element < nums2_element:
                result.append(nums1_element)
                index_nums1 += 1

            elif nums1_element > nums2_element:
                result.append(nums2_element)
                index_nums2 += 1

            else:
                result.append(nums1_element)
                result.append(nums2_element)

                index_nums1 += 1
                index_nums2 += 1

            if index_nums1 == m_:
                for element in nums2[index_nums2:]:
                    result.append(element)
                break

            if index_nums2 == n_:
                for element in nums1_[index_nums1:]:
                    result.append(element)
                break

        for index, element in enumerate(result):
            nums1[index] = element


def test_case():

    solution = Solution()

    nums1 = [0]
    solution.merge(nums1, 0, [1], 1) == [1]
    assert nums1 == [1]

    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [2, 0]
    solution.merge(nums1, 1, [1], 1)
    assert nums1 == [1, 2]
