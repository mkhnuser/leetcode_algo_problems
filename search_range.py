from typing import List


NOT_FOUND = [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return NOT_FOUND

        return [
            self.find_the_first_occurrence(nums, target),
            self.find_the_last_occurrence(nums, target),
        ]

    def find_the_first_occurrence(self, nums, target):
        lower_index = 0
        upper_index = len(nums) - 1
        min_index = None

        while lower_index <= upper_index:
            middle_index = (lower_index + upper_index) // 2
            middle_element = nums[middle_index]

            if middle_element > target:
                upper_index = middle_index - 1
            elif middle_element < target:
                lower_index = middle_index + 1
            else:
                min_index = middle_index
                upper_index = middle_index - 1

        return min_index if min_index is not None else -1

    def find_the_last_occurrence(self, nums, target):
        lower_index = 0
        upper_index = len(nums) - 1
        max_index = None

        while lower_index <= upper_index:
            middle_index = (lower_index + upper_index) // 2
            middle_element = nums[middle_index]

            if middle_element > target:
                upper_index = middle_index - 1
            elif middle_element < target:
                lower_index = middle_index + 1
            else:
                max_index = middle_index
                lower_index = middle_index + 1

        return max_index if max_index is not None else -1
