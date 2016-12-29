class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= (len(s) - 1):
            return s
        l = [''] * numRows
        index, step = 0, 1
        for x in s:
            l[index] += x
            if index == 0:
                step = 1
            if index == (numRows - 1):
                step = -1
            index += step
        return ''.join(l)
c = Solution()
print c.convert('abc',1)
