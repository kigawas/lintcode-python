class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        # write your code here
        return sorted(s) == sorted(t)
