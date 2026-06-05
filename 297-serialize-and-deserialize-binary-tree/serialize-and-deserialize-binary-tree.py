# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result = ""
        q = deque()
        q.append(root)
        while q:
            curr_node = q.popleft()
            if curr_node is None:
                result += "#,"
            else:
                result += str(curr_node.val)+","
                q.append(curr_node.left)
                q.append(curr_node.right)
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        node = data.split(",")
        root = TreeNode(int(node[0]))
        q = deque()
        q.append(root)
        i = 1
        while q and i< len(node)-1:
            curr = q.popleft()
            if (node[i] != "#"):
                left = TreeNode(int(node[i]))
                curr.left = left
                q.append(left)
            i += 1
            if node[i] != "#":
                right = TreeNode(int(node[i]))
                curr.right = right
                q.append(right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))