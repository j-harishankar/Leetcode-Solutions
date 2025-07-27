class Solution(object):
    def moveZeroes(self, nums):
        left = 0 
        for i in range(len(nums)):
            right = i 
            if nums[i]!=0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        return nums