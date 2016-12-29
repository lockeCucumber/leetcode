class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateParenthesisRec(s, left, right, parenthesis):
            if left:
                generateParenthesisRec(s + '(', left - 1, right, parenthesis)
            if left < right:
                generateParenthesisRec(s + ')', left, right - 1, parenthesis)
            if left == 0 and right == 0:
                parenthesis.append(s)
            return parenthesis
        return generateParenthesisRec('', n, n, [])
o = Solution()
print o.generateParenthesis(3)
