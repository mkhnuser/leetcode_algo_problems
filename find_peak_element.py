from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lower_index = 0
        upper_index = len(nums) - 1
        output = None

        while lower_index <= upper_index:
            middle_index = (lower_index + upper_index) // 2
            if middle_index == 0 or nums[middle_index] >= nums[middle_index - 1]:
                output = middle_index
                lower_index = middle_index + 1
            else:
                upper_index = middle_index - 1

        return output if output is not None else -1
