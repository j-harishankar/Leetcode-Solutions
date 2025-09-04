class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.pivot_element(nums)
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if target>=nums[pivot] and target<= nums[len(nums)-1]:
            return self.helper(nums,target,pivot,len(nums)-1)
        else:    
            return self.helper(nums,target,0,pivot-1)

    def pivot_element(self,nums):
        l=0
        r=len(nums)-1
        if nums[l] <= nums[r]:
            return 0 
        while l<=r:
            mid = (l+r) // 2
            if nums[mid] < nums[mid-1]:
                return mid
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[mid] < nums[l]:
                r = mid -1 
            else:
                l = mid + 1
    def helper(self,nums,target,l,r):
        while l<=r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1