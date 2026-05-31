class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        n = abs(x)

        s = 0

        while n:
            d = n % 10
            s = s * 10 + d
            n //= 10

        s *= sign

        if s < -2**31 or s > 2**31 - 1:
            return 0

        return s