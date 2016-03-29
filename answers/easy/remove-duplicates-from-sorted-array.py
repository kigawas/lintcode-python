class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here
        if A == []:
            return 0
        index = 0
        for i in range(len(A)):
            if A[index] != A[i]:
                index += 1
                A[index] = A[i]
        return index + 1
