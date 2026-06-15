# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        new_node = TreeNode(val)
        if not root:
            return new_node
        curr = root
        while True:
            if new_node.val < curr.val:

                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
            
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break

        return root


        