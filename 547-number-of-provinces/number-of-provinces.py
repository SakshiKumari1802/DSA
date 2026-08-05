class Solution(object):
    def dfs(self,node,adj_list,visited):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        V = len(isConnected[0])
        adj_list = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited = [False]*V
        count = 0
        for i in range(V):
            if not visited[i]:
                count += 1
                self.dfs(i, adj_list, visited)
        return count



        