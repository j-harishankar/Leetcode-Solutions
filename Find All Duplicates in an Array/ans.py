# using hash map space complexity not met time complexity O(N)
class Solution(object):
    def findDuplicates(self, nums):
        seen = {}
        l = []
        k = len(nums)
        for i in range(k):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]] = 1
        for i in seen:
            if seen[i]>1:
                l.append(i)
        return l