class Solution(object):
    def minSubArrayLen(self, target, nums):
        l,total = 0,0
        min_len = float("inf")
        j=len(nums)
        for r in range(j):
            total += nums[r]
            while total>=target:
                k = r-l+1
                min_len = min(k,min_len)
                total -= nums[l]
                l+=1
        return 0 if min_len==float("inf") else min_len
