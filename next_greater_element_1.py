class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        res = []
        for num in nums:
            while stack and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)
        return [dic.get(num, -1) for num in findNums]

o = Solution()
print o.nextGreaterElement([2, 4], [1, 2, -1, 4, 3])
