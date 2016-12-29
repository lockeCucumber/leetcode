class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        dup = 0
        i = count = 0
        while count < n - 1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
            count += 1
        return len(nums)
o = Solution()
a = [1,1,2,2,3]
print o.removeDuplicates(a)
print a 
