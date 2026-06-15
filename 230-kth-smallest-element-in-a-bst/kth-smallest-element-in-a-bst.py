class Solution(object):

    def kthSmallest(self, root, k):

        self.count = 0
        self.ans = None

        def inorder(node):

            if not node or self.ans is not None:
                return

            inorder(node.left)

            self.count += 1

            if self.count == k:
                self.ans = node.val
                return

            inorder(node.right)

        inorder(root)

        return self.ans