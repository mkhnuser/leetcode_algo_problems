import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        return round((math.log(n, 3)), 10).is_integer()


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        while n % 3 == 0:
            return self.isPowerOfThree(n / 3)

        return False
