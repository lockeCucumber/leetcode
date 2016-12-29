class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        elif len(nums) == 1:
            return [nums]
        res = []
        for p in self.permuteUnique(nums[1:]):
            for i in xrange(len(nums)):
                tmp = p[:i] + [nums[0]] + p[i:]
                if tmp not in res:
                    res.append(tmp)
        return res
