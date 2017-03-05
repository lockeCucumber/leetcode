class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res = [], [-1]*len(nums)
        for index, item in enumerate(nums*2):
            while stack and nums[stack[-1]] < item:
                res[stack.pop()] = item
            if index < len(nums):
                stack.append(index)
        return res

o = Solution()
print o.nextGreaterElements([1, 2, 3, 4, 3])
print [1]*7
