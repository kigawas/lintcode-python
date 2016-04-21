class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        if nums == []:
            return
        N = len(nums)
        return N * (N + 1) / 2 - sum(nums)
