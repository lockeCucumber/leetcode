class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        result_list = [[1 for i in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            if obstacleGrid[i][0] == 1:
                for j in xrange(i, m):
                    result_list[j][0] = 0
                break
        for j in xrange(n):
            if obstacleGrid[0][j] == 1:
                for i in xrange(j, n):
                    result_list[0][i] = 0
                break

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    result_list[i][j] = 0
                else:
                    result_list[i][j] = result_list[i-1][j]
                    + result_list[i][j-1]
        return result_list[-1][-1]
o = Solution()
a = [
  [1],
  [0],
]
print o.uniquePathsWithObstacles(a)
