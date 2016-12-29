class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = [p for p in path.split('/') if p != '.' and p != '']
        for item in paths:
            if item != '..':
                stack.append(item)
            else:
                if len(stack) > 0:
                    stack.pop()
        return '/' + '/'.join(stack)
o = Solution()
print o.simplifyPath("/a/./b/../../c/")
