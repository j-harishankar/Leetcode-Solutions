class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        if len(nums) == 1:
            if target in nums:
                return [0,0]
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                while i<len(nums) and nums[i]==target: 
                    i+=1
                return [start,i-1]
        return lst