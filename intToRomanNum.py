class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,\
        'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        d = {}
        for (k, v) in roman_dict.items():
            d[v] = k
        l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        for i in l:
            while num / i > 0:
                result += d[i] * (num / i)
                num = num - i * (num / i)
        return result

o = Solution()
print o.intToRoman(621)
# print 'e' * 3
