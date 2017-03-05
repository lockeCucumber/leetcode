#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def sort(self, nums):
        """
        归并排序 nlgn
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        nums_a = self.sort(nums[0:n/2])
        nums_b = self.sort(nums[n/2::])
        res = []
        while nums_a and nums_b:
            min_num = min([nums_a[0], nums_b[0]])
            res.append(min_num)
            if min_num == nums_a[0]:
                nums_a.pop(0)
            else:
                nums_b.pop(0)
        res += nums_a + nums_b
        return res

    def sort_pop(self, nums):
        """
        冒泡排序 n^2
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
        return nums

    def sort_insert(self, nums):
        """
        插入排序 n^2
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(1, n):
            tmp = nums[i]
            j = i - 1
            while j >= 0 and tmp < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = tmp
        return nums



o = Solution()
print o.sort_insert([9, 8, 7, 6, 5, 4, 3, 2, 1])
