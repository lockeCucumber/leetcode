class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        nums_neg = []
        ans = []
        for item in nums:
            nums_neg.append(-item)
        for i in xrange(n):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                c = a + b
                if c in nums_neg[j+1:n]:
                    if [a, b, -a-b] not in ans:
                        ans.append([a, b, -c])
        return ans
l = [-1, 0, 1, 2, -1, -4]
o = Solution()
print o.threeSum(l)
if l.index(5):
    print 3
