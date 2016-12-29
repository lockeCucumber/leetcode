class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aNum = int(a, 2)
        bNum = int(b, 2)
        num = aNum + bNum
        return bin(num).replace('0b', '')
o = Solution()
print o.addBinary('0', '0')
