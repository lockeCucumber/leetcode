class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        len_strs = []
        for s in strs:
            len_strs.append(len(s))
        min_len = min(len_strs)
        num = min_len
        for i in xrange(min_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    num = i
                    break
            if num != min_len:
                break
        return strs[0][0:num]

o = Solution()
print o.longestCommonPrefix(["flower","flow","flight"])
