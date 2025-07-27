class NumArray(object):

    def __init__(self, nums):
        self.prefix=[0]
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)        

    def sumRange(self, left, right):
        return self.prefix[right+1]-self.prefix[left]


commands = ["NumArray", "sumRange", "sumRange", "sumRange"]
arguments = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
