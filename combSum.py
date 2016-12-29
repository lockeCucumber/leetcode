class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def dfs(nums, target, index, stack, res):
            if target < 0:
                return
            elif target == 0:
                res.append(stack)
                return
            else:
                for i in range(index, len(nums)):
                    dfs(nums, target - nums[i], i, stack + [nums[i]], res)
        dfs(candidates, target, 0, [], res)
        return res


o = Solution()
print o.combinationSum([2,3,6,7], 7)
