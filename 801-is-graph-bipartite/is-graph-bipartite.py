class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [-1]*n
        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor] ==-1:
                    color[neighbor] = 1-color[node]
                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True
        


        for i in range(n):
            if color[i]==-1:
                color[i]=0
                if not dfs(i):
                    return False
        return True
        