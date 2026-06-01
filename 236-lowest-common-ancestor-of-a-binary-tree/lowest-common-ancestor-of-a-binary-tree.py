
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base case
        if root is None or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Result
        if left is None:
            return right
        elif right is None:
            return left
        else: # Both left and right are not null, we found our result
            return root