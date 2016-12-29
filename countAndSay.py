from collections import Counter
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        result = ''
        j = 0
        l =[]
        for i in range(0, len(s)):
            if i != (len(s) - 1) and s[i] != s[i+1]:
                result += str(i+1-j) + s[i]
                j = i + 1
            if i == len(s) - 1:
                result += str(len(s)-j) + s[i]
        return result

o = Solution()
print o.countAndSay(5)
# s = '1122'
# b = Counter(s)
# for i in b.iterkeys():
#     print i,b[i]
