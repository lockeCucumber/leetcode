class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st = []
        for i in num:
            while k and st and int(st[-1]) > int(i):
                st.pop()
                k = k - 1
            else:
                st.append(i)
        while st and k:
            st.pop()
            k = k - 1
        return ''.join(st).lstrip('0') or '0'
