class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        # Write your code here
        import math
        MAX = 2147483647
        a = dividend
        b = divisor
        if a == 0:
            return 0
        if b == 1:
            return a
        if a == b:
            return 1
        if b == 2 or b == 4 or b == 8 or b == 16:
            return a >> int(math.log(b, 2))
        if b == 0:
            return MAX

        positive = True
        if a > 0 and b > 0:
            a = a
            b = b
        elif a < 0 and b < 0:
            a = -a
            b = -b
        elif a < 0 and b > 0:
            a = -a
            b = b
            positive = False
        else:
            a = a
            b = -b
            positive = False
        result = int(math.pow(2, math.log(a, 2) - math.log(b, 2)))
        if result > MAX:
            result = MAX
        if positive:
            return result
        else:
            return -result
