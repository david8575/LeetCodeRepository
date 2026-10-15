# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        list1 = []
        list2 = []

        self.check(root1, list1)
        self.check(root2, list2)

        return list1 == list2

    def check(self, root, lists):
        if root is None:
            return

        if root.left is None and root.right is None:
            lists.append(root.val)

        self.check(root.left, lists)
        self.check(root.right, lists)