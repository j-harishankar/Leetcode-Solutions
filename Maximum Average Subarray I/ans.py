class Solution(object):
    def findMaxAverage(self, nums, k):
        sum_s = 0
        for i in range(k):
            sum_s += nums[i]
        max_s = sum_s
        for r in range(k,len(nums)):
            sum_s = sum_s + nums[r] - nums[r-k]
            max_s = max(max_s,sum_s)
        return float(max_s)/k