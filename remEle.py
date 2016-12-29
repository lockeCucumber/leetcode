class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums[:]:
            if i == val:
                nums.remove(val)
        return len(nums)
o = Solution()
print o.removeElement([1,2,3,3,2], 3)
