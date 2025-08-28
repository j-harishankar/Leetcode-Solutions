class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        while l<=r:
            mid = (l+r) // 2
            if mid*mid < x:
                result = mid
                l = mid+1
            elif mid*mid > x:
                r = mid-1
            elif  mid*mid == x:
                return mid
        return result