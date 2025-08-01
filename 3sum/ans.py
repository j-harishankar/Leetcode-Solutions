class Solution(object):
    def threeSum(self, nums):
        result = set()
        nums.sort()
        k = len(nums)
        lst=[]
        for i in range(k-2):
            left = i+1
            right = k-1
            while(left<right):
                sumf = nums[i]+nums[left]+nums[right]
                if sumf == 0:
                    t = (nums[i],nums[left],nums[right])
                    result.add(t)
                    left+=1
                    right-=1
                elif sumf<0:
                    left+=1
                else:
                    right-=1
        return [list(triplet) for triplet in result]