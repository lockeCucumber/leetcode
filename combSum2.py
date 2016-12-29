class Solution(object):
    def combinationSum2(self, candidates, target):
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
                    if i > index and nums[i] == nums[i-1]:
                        continue
                    dfs(nums, target - nums[i], i + 1, stack + [nums[i]], res)
        dfs(candidates, target, 0, [], res)
        return res

o = Solution()
print o.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
