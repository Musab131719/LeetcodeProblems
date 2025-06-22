class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        def isPerfectSquare(num: int) -> bool:
            l = 0
            r = num
            while l <= r:
                m = (l + r) // 2
                if m*m == num:
                    return True
                elif m*m < num:
                    l = m + 1
                elif m*m > num:
                    r = m - 1
            return False
        
        if isPerfectSquare(c) == True:
            return True

        L = 0
        R = c
        root_c = 0 
        while L <= R:
            M = (L + R) // 2
            if M * M == c:
                root_c = M
                break
            elif M * M > c:
                R = M - 1
            elif M * M < c:
                L = M + 1
        root_c = R if root_c == 0 else root_c 
        print(root_c)
        
        
        arr = list(range(1, root_c + 1))
        print(arr)
        for number in arr:
            print(c - number*number, isPerfectSquare(c - number*number))
            if isPerfectSquare(c - number*number) == True:
                return True
            else: continue
        return False