class Solution(object):
    def maxPathSum(self, root):

        maxi = [float('-inf')]

        def maxPath(node):

            if not node:
                return 0

            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))

            maxi[0] = max(
                maxi[0],
                left + right + node.val
            )

            return node.val + max(left, right)

        maxPath(root)

        return maxi[0]