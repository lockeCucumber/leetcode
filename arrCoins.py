import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(long(n)*2 + 1/4.0) - 1/2.0)
o = Solution()
print o.arrangeCoins(5)
