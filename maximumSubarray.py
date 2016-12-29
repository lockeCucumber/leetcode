class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        dp = [0] * n
        res = dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            res = max(dp[i], res)
        return res
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        res = tmp = nums[0]
        for i in range(1,n):
            tmp = nums[i] + (tmp if tmp > 0 else 0)
            res = max(tmp, res)
        return res
    def maxSubArray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+ nums[i-1])
        return max(nums)
nums = [-2,1,-3,4,-1,2,1,-5,4]
o = Solution()
print o.maxSubArray3(nums)
