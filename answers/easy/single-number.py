class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        return reduce(lambda x, y: x ^ y, A) if A != [] else 0
