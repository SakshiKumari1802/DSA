# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        results =[]
        def traverse( currentNode):
             if currentNode is None:
                return
             results.append(currentNode.val)
             if currentNode.left is not None:
                traverse(currentNode.left)
             if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(root)
        return results
        