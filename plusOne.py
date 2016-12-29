class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        addListNums = True
        for item in digits:
            if item != 9:
                addListNums = False
        if addListNums:
            return [1] + [0] * len(digits)
        else:
            carry = False
            for i in range(0, len(digits))[::-1]:
                if i == (len(digits) -1):
                    digits[i] += 1
                    carry = True
                if carry and (digits[i] % 10) == 0:
                    digits[i] = 0
                    digits[i-1] += 1
                    if (digits[i-1] % 10) != 0:
                        carry = False
                else:
                    carry = False

        return digits
o = Solution()
print o.plusOne([1,0,0])
