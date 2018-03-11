import re


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s = re.sub(r'(\d+)\[(\w+)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s
o = Solution()
print o.decodeString('3[a2[c]]')
