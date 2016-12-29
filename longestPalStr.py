# class Solution:
#     # @return a string
#     def longestPalindrome(self, s):
#         if len(s)==0:
#         	return ''
#         start = 0
#         maxLen = 1
#         for i in xrange(len(s)):
#             if i - maxLen - 1 >= 0 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
#                 start = i - maxLen - 1
#                 maxLen += 2
#
#             if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
#                 start = i - maxLen
#                 maxLen += 1
#         return s[start: start + maxLen]
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        nums = [''] * len(s)
        nums[0] = s[0]
        for i in xrange(1, len(s)):
            
o = Solution()
print o.longestPalindrome('abanaba')
