class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I':1,'a':4,'V':5,'b':9,'X':10,'c':40,'L':50,\
        'd':90,'C':100,'e':400,'D':500,'f':900,'M':1000}
        s = s.replace('IV','a').replace('IX','b').replace('XL','c').replace('XC','d')\
        .replace('CD','e').replace('CM','f')
        result = 0
        for i in list(s):
            result += roman_dict[i]
        return result
o = Solution()
print o.romanToInt('DCXXI')
