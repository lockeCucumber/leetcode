class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            s = str(x)[::-1]
            if -2147483648 <= int(s) <= 2147483647:
                return int(s)
            else:
                return 0
        elif 0 == x:
            return 0
        else:
            s = str(x)[1:]
            unit_s = s[::-1]
            if -2147483648 <= (0 - int(unit_s)) <= 2147483647:
                return 0 - int(unit_s)
            else:
                return 0
s = Solution()
print s.reverse(10100)
