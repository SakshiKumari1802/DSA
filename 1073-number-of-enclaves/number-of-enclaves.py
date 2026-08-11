from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not  grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        vis = [[False]*m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    if grid[i][j] == 1 and not vis[i][j]:
                        vis[i][j] = True
                        q.append((i,j))
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]
        while q:
            row,col = q.popleft()
            for k in range(4):
                nrow = row + delrow[k]
                ncol = col + delcol[k]
                if 0<=nrow<n and 0<=ncol<m and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                    vis[nrow][ncol] = True
                    q.append((nrow,ncol))
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    cnt += 1
        return cnt
    
        