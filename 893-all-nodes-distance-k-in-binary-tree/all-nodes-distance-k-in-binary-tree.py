# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        parent_map = {}
        self.map_parents(root, parent_map)
        return self.bfs_from_target(target, parent_map, k)
    def map_parents(self, root, parent_map):
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
    def bfs_from_target(self,target,parent_map,k):
        queue = deque()
        visited = set()
        queue.append(target)
        visited.add(target)
        current_level = 0
        while queue:
            if current_level == k:
                break
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
            current_level += 1
        return [node.val for node in queue]
                        

        