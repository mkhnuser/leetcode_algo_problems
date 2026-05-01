from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recurse_search(
            nums, target, lower_index=0, upper_index=len(nums) - 1
        )

    def recurse_search(self, nums, target, lower_index, upper_index):
        # NOTE: [5, 6, 7, 0, 1, 2, 3, 4]. target = 4, middle_element = 1.

        if lower_index > upper_index:
            return -1

        middle_index = (lower_index + upper_index) // 2
        middle_element = nums[middle_index]
        leftmost_element = nums[0]

        if middle_element == target:
            return middle_index

        # NOTE: middle_element != target at this point.

        if middle_element >= leftmost_element:
            # NOTE: Middle index is located in the bigger half.
            if target >= leftmost_element and target < middle_element:
                # NOTE: Recurse left.
                return self.recurse_search(
                    nums, target, lower_index=lower_index, upper_index=middle_index - 1
                )
            # NOTE: Recurse right.
            return self.recurse_search(
                nums, target, lower_index=middle_index + 1, upper_index=upper_index
            )

        else:  # NOTE: middle_element < leftmost_element:
            # NOTE: We are in a lower half.
            if target < leftmost_element and target > middle_element:
                # NOTE: Recurse right.
                return self.recurse_search(
                    nums, target, lower_index=middle_index + 1, upper_index=upper_index
                )
            # NOTE: Recurse left.
            return self.recurse_search(
                nums, target, lower_index=lower_index, upper_index=middle_index - 1
            )
