class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        from collections import deque
        shifts_sum = deque(shifts)
        res = ""
        n = sum(shifts_sum)        
        
        for i in range(len(s)):
            shift = n % 26
            value = ord(s[i]) + shift
            res += chr((value - 97) % 26 + 97)
            n -= shifts_sum[0]
            shifts_sum.popleft()
        return res