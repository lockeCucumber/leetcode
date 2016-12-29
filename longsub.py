class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        temp = []
        for item in s:
            if item in temp:
                if len(temp) > result:
                    result = len(temp)
                temp = temp[temp.index(item) + 1:]
                temp.append(item)
            else:
                temp.append(item)
        return max(result, len(temp))
a = Solution()
print a.lengthOfLongestSubstring('abcabcabcbb')
