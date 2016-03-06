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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        p = root
        s = []
        res = []
        while s != [] or p:
            if p:
                s.append(p)
                p = p.left
            else:
                p = s.pop()
                res.append(p.val)
                p = p.right
        return res