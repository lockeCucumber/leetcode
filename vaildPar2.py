class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or len(s) % 2 != 0:
            return False
        stack = []
        d = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in '{[(':
                stack.append(i)
            elif i in '}])':
                if stack != [] and d[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack

o = Solution()
print o.isValid("([])")
print [][-1]
