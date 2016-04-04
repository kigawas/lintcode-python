"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""


class Solution:
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start > end:
            return
        root = SegmentTreeNode(start, end)
        self.createChild(root)
        return root

    def createChild(self, node):
        if node.start == node.end or node is None:
            return
        node.left = SegmentTreeNode(node.start, (node.start + node.end) / 2)
        node.right = SegmentTreeNode((node.start + node.end) / 2 + 1, node.end)
        self.createChild(node.left)
        self.createChild(node.right)
