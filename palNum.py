class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)[::-1]
        rev_x = int(s)
        if -2147483648 <= rev_x <= 2147483647:
            if rev_x == x:
                return True
            else:
                return False
        else:
            return False
o = Solution()
print o.isPalindrome(121)
