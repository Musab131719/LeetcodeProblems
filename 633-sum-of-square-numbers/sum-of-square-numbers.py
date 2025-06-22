class Solution(object):
    def judgeSquareSum(self, c):
        
        def sq_root(num):
            l = 0
            r = num
            res = 0
            while l <= r:
                m = (l + r) // 2
                if m*m == num:
                    return m
                elif m*m < num:
                    l = m + 1
                elif m*m > num:
                    r = m - 1
            return r
        
        if sq_root(c)**2 == c:
            return True

        L = 0
        R = sq_root(c)
        print(R)
        while L <= R:
            s = L * L + R * R
            if s > c:
                R -= 1
            elif s < c:
                L += 1
            else:
                return True
        return False
        