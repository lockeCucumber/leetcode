class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     this way is OK but it takes too much time
    #     """
    #     if m == 1:
    #         return 1
    #     if n == 1:
    #         return 1
    #     while m and n:
    #         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result_list = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                result_list[i][j] = result_list[i-1][j] + result_list[i][j-1]
        return result_list[-1][-1]
o = Solution()
print o.uniquePaths(3, 2)
