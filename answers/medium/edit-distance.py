class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        if word1 == word2:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        m, n = len(word1), len(word2)
        d = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        for i in xrange(0, m + 1):
            d[i][0] = i
        for j in xrange(0, n + 1):
            d[0][j] = j
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1],
                                  d[i - 1][j - 1]) + 1
        return d[m][n]
