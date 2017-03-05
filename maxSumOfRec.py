class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        res = -2147483648
        for i in xrange(m):
            for j in xrange(n):
                for a in xrange(i, m):
                    for b in xrange(j, n):
                        tmp = [[matrix[x][y] for y in xrange(j, b+1)] for x in xrange(i, a+1)]
                        tmp_sum = 0
                        for item in tmp:
                            tmp_sum += sum(item)
                        if tmp_sum > res and tmp_sum <= k:
                            # print tmp_sum
                            res = tmp_sum
        # print '#' * 10
        return res
o = Solution()
matrix = [
    [1, 0, 1],
    [0, -2, 3]
]
print o.maxSumSubmatrix(matrix, 2)
