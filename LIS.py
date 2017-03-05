class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            tmp = [1]
            tmp += [dp[j] + 1 for j in xrange(i) if nums[j] < nums[i]]
            dp[i] = max(tmp)
        return max(dp)
o = Solution()
print o.lengthOfLIS([])
