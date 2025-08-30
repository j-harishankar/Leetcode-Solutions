class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.helper(nums,target,True)
        right = self.helper(nums,target,False)
        return [left,right]
    def helper(self,nums,target,leftBias):
        l,r = 0 ,len(nums)-1
        index = -1
        while(l<=r):
            mid = (l+r) // 2
            if nums[mid] < target: 
                l = mid+1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index  = mid
                if leftBias:
                    r = mid-1 
                else:
                    l = mid+1
        return index