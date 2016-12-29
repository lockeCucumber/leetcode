class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        result,dict_nums = 0, {}
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                tmp = A[i] + B[j]
                if not dict_nums.has_key(tmp):
                    dict_nums[tmp] = 1
                else:
                    dict_nums[tmp] += 1
        for i in xrange(len(C)):
            for j in xrange(len(D)):
                tmp = -C[i] - D[j]
                if dict_nums.has_key(tmp):
                    result += dict_nums[tmp]
        return result
