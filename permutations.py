class Solution(object):
    def permute(self, nums):
        if nums == []:
            return [[]]
        elif len(nums) == 1:
            return [nums]
        return [p[:i] + [nums[0]] + p[i:]
            for p in self.permute(nums[1:]) for i in range(0,len(nums))]
o = Solution()
print o.permute([1,1,2])
