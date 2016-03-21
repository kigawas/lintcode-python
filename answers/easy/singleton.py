class Solution:
    # @return: The same instance of this class every time
    class __Solution:
        pass
    ins = None

    @classmethod
    def getInstance(cls):
        # write your code here
        if not Solution.ins:
            Solution.ins = Solution.__Solution()
        return Solution.ins
