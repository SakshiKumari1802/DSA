# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.rightDFS(root, 0, res)
        return res
    def rightDFS(self,node,level,res):

        if node is None:
            return
        if len(res) == level:
            res.append(node.val)
        self.rightDFS(node.right, level+1, res)
        self.rightDFS(node.left, level+1, res)
    
        