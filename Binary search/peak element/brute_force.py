class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        prev = 0
        if len(nums) == 1:
            return 0 
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0 
            else:
                return 1 
        for i in range(0,len(nums)):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            if i == len(nums) - 1 and nums[i] > nums[i-1]:
                return i  
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i 
            