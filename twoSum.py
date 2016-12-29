class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsSorted = sorted(nums)
        i, j = 0, len(numsSorted) - 1
        while i < j:
            tmp = numsSorted[i] + numsSorted[j]
            if tmp == target:
                a = nums.index(numsSorted[i])
                b = nums.index(numsSorted[j])
                if a != b:
                    return [a,b]
                elif nums.count(nums[b]) > 1:
                    nums.remove(nums[b])
                    return [a,nums.index(numsSorted[j])+1]
            elif tmp < target:
                i += 1
            else:
                j -= 1
        return []
o = Solution()
print o.twoSum([0,4,3,0], 0)
