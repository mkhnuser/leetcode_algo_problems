class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # NOTE: n >= 2 at this point.

        a, b = 0, 1
        n -= 2

        while n >= 0:
            a, b = b, a + b
            n -= 1

        return b
