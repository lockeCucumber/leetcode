class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        l = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = ['']
        for i in digits:
            i = int(i)
            result = [x + y for x in result for y in l[i]]
        return result
o = Solution()
print o.letterCombinations("23")
