class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """

    def fastPower(self, a, b, n):
        if n == 1:
            return a % b
        elif n == 0:
            return 1 % b
        elif n < 0:
            return -1

        product = self.fastPower(a, b, n / 2)
        product = (product * product) % b
        if n % 2 == 1:
            product = (product * a) % b

        return product
