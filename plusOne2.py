class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(0, len(digits))[::-1]:
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            return [1] + digits
        return digits

o = Solution()
print o.plusOne([1,0,0])
