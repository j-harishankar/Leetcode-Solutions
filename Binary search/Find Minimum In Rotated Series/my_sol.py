def findMin(self, nums: List[int]) -> int:
    l,r =0,len(nums)-1
    if nums[l]<=nums[r]:
        return nums[l] 
    else:
        return self.pivot(nums,l,r)
def pivot(self,nums,l,r):
    while l<=r:
        mid = (l+r)//2
        if nums[mid]<nums[mid-1]:
            return nums[mid]
        elif nums[mid]<nums[0]:
            r = mid - 1
        else:
            l = mid + 1 