class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        n = len(nums)
        L = 0
        for R in range(n):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
            
        