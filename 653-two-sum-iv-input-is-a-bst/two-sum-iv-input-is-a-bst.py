# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, node, reverse):
        self.stack = []
        self.reverse = reverse
        self.pushAll(node)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left

    def next(self):
        node = self.stack.pop()

        if self.reverse:
            self.pushAll(node.left)
        else:
            self.pushAll(node.right)

        return node.val


class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False

        left = BSTIterator(root, False)
        right = BSTIterator(root, True)

        i = left.next()
        j = right.next()

        while i < j:
            s = i + j

            if s == k:
                return True
            elif s < k:
                i = left.next()
            else:
                j = right.next()

        return False
        