class Solution:
    def countFreq(self, arr, target):

        left = self.helper(target,arr,True)
        right = self.helper(target,arr,False)
        if left == -1 or right == -1:  # target not found
            return 0
        return (right - left ) + 1
    def helper(self,target,arr,left):
        l,r = 0,len(arr)-1
        ans = -1 

        while l<=r:
            mid = (l+r) // 2
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1 
            else:
                ans = mid
                if left:
                    r= mid - 1 
                else:
                    l = mid+1 
        return ans 
