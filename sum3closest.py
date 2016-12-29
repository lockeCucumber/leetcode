class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        mix = abs(result - target)
        n = len(nums)
        for i in xrange(n-2):
            j,k = i+1,n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s < target:
                    j += 1
                else:
                    k -=1
                if abs(s-target) < mix:
                    mix = abs(s-target)
                    result = s
        return result
o = Solution()
print o.threeSumClosest([0,0,0], 1)
