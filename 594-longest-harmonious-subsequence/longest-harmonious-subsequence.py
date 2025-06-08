class Solution(object):
    def findLHS(self, nums):
        if len(nums) == 0:
            return 0
        count = {}
        adj = []
        longest = 0
        for i in nums:
            count[i] = count.get(i,0) + 1   # If this item already exists, increase its count; if not, start it at 1
        for key in count:
            if key + 1 in count:
                adj.append((key, key+1))
            if key - 1 in count:
                adj.append((key, key-1))
        for tup in adj:
            longest = max(longest, count[tup[0]] + count[tup[1]])
        return longest