class Solution(object):
    def findMaxAverage(self, nums, k):
        L = 0
        n = len(nums)
        max_avg = sum(nums[:k])/float(k)
        curr_sum = sum(nums[:k])

        if n <= k:
            return sum(nums)/float(k)

        for i in range(k,n):
            L += 1
            curr_sum += nums[i] - nums[i-k]
            max_avg = max(max_avg, curr_sum/float(k))
        return max_avg
    