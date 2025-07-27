class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height)-1
        max_water = 0
        while left <= right:
            width = right - left 
            min_height = min(height[left],height[right])
            area = min_height * (width)
            max_water = max(area,max_water)

            if min_height == height[left]:
                left += 1
            else:
                right -= 1
        return max_water