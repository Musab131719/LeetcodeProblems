class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        L = 0
        R = len(height) - 1
        while L != R:
            m = min(height[L], height[R])
            result = max(result, m * (R - L))
            if m == height[L]:
                L += 1 
            else:
                R -= 1
        return result

'''Critical to understand that we can just move the minimum of the pointers along since it is limiting the result'''