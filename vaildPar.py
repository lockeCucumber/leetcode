class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or len(s) % 2 != 0:
            return False
        for item in s:
            if item not in '()[]{}':
                return False
        sBackUp = ''
        while s != sBackUp:
            sBackUp = s
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == '':
            return True
        else:
            return False
o = Solution()
print o.isValid("([])")
