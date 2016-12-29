class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        return len(s.split(' ')[-1])

s = 'dfa '
o = Solution()
print o.lengthOfLastWord(s)
