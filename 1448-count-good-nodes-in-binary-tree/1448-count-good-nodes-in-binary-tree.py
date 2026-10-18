# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(root, val):
            if root:
                k = check(root.left, max(val, root.val)) + check(root.right, max(val, root.val))

                if root.val >= val:
                    k+=1

                return k

            return 0

        return check(root, root.val)