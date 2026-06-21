# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.i = 0
        def build(bound):
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root
        return build(float('inf'))
