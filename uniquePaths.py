class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
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
        if m == 1:
            return 1
        if n == 1:
            return 1
        a = b = 1
        res = 1
        while a < m and b < n:
            res += self.uniquePaths(a + 1, b) + self.uniquePaths(a, b + 1)
            a += 1
            b += 1
        # if a == m and b < n:
        #     res += 1
        # if b == n and a < m:
        #     res += 1
        return res
o = Solution()
print o.uniquePaths(3, 3)
