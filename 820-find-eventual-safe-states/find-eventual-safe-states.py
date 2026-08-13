from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        adj = graph
        V = len(graph)
        adjRev = [[] for _ in range(V)]
        indegree = [0]*V
        for i in range(V):
            for neighbor in adj[i]:
                adjRev[neighbor].append(i)
                indegree[i] += 1
        q = deque()
        SafeNodes = []
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            SafeNodes.append(node)
            for parent in adjRev[node]:
                indegree[parent] -= 1
                if indegree[parent] == 0:
                    q.append(parent)
        SafeNodes.sort()
        return SafeNodes