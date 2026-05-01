class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.is_sqrt(num)

    def is_sqrt(self, num):
        # NOTE: Both recursive and iterative solutions are possible.
        # return self.recurse_is_sqrt(num, lower=0, upper=num)
        return self.iterate_is_sqrt(num)

    def iterate_is_sqrt(self, num):
        lower = 0
        upper = num

        while lower <= upper:
            middle = (lower + upper) // 2
            exp = middle**2

            if exp == num:
                return True
            elif exp > num:
                upper = middle - 1
            else:
                lower = middle + 1

        return False

    def recurse_is_sqrt(self, num, lower, upper):
        if lower > upper:
            return False

        middle = (lower + upper) // 2
        exp = middle**2

        if exp == num:
            return True
        elif exp < num:
            return self.recurse_is_sqrt(num, lower=middle + 1, upper=upper)
        # NOTE: exp > num.
        return self.recurse_is_sqrt(num, lower=lower, upper=middle - 1)
