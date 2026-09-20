class NumArray:

    def __init__(self, nums: list[int]):
        n=len(nums)
        self.preArray=[0]*(n+1)
        for i in range(n):
            self.preArray[i+1]=self.preArray[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.preArray[right+1]-self.preArray[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)