class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        if A is None or B is None or len(A) != len(B):
            return 2.0000
        s = 0
        for a, b in zip(A, B):
            s += a * b
        sA = sum([x * x for x in A])**0.5
        sB = sum([x * x for x in B])**0.5
        if sA == 0 or sB == 0:
            return 2.0000
        return s / (sA * sB)
