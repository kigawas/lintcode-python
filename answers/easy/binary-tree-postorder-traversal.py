"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        cur = root
        res = []
        if cur:
            s1 = []
            s2 = []
            s1.append(cur)
            while s1 != []:
                cur = s1.pop()
                s2.append(cur)
                if cur.left:
                    s1.append(cur.left)
                if cur.right:
                    s1.append(cur.right)
            while s2 != []:
                res.append(s2.pop().val)
        return res
