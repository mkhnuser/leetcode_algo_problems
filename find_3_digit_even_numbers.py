from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        output = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue

                    # NOTE: Base-ten system usage.
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        output.add(num)

        res = sorted(list(output))
        return res
