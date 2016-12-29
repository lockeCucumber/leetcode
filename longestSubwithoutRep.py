class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        max = 1
        for i in range(len(s)-1):
            for j in range(i + 1, len(s) + 1):
                subs = s[i:j]
                if len(s) == j :
                    if max < len(subs):
                        max = len(subs)
                    break
                elif s[j] in subs:
                    if max < len(subs):
                        max = len(subs)
                    break
        return max
        
s1 = 'ad'
a = Solution()
print a.lengthOfLongestSubstring(s1)
# print a.lengthOfLongestSubstring(s2)
# print a.lengthOfLongestSubstring(s3)
for i in range(1,2):
    print i
