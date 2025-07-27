class Solution(object):
    def twoSum(self, numbers, target):
        right = len(numbers) - 1
        left = 0 
        while left < right: 
            sumo = numbers[left]+numbers[right] 
            if sumo == target:
                return [left+1,right+1]
            elif sumo < target:
                left += 1
            else:
                right -= 1 