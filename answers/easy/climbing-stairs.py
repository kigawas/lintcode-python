class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n < 1:
            return 1
        a = 1
        b = 1
        for i in xrange(n):
            a, b = b, a+b
        return a
