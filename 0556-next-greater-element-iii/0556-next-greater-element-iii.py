class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > digits[i - 1]:
                break
        else:
            return -1

        for j in range(len(digits) - 1, i - 1, -1):
            if digits[j] > digits[i - 1]:
                digits[i - 1], digits[j] = digits[j], digits[i - 1]
                break

        digits[i:] = sorted(digits[i:])
        result = int(''.join(map(str, digits)))

        if result > 2**31 - 1:
            return -1
        else:
            return result