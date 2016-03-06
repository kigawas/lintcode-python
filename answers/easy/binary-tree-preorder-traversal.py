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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        cur = root
        res = []
        if cur:
            s = []
            s.append(cur)
            while s != []:
                cur = s.pop()
                res.append(cur.val)
                if cur.right:
                    s.append(cur.right)
                if cur.left:
                    s.append(cur.left)
        return res