class Solution:
    def mySqrt(self, x: int) -> int:

        L = 0
        R = x
        while L <= R:
            M = (L + R) // 2
            if M * M == x:
                return M
            elif M * M > x:
                R = M - 1
            elif M * M < x:
                L = M + 1
        return R