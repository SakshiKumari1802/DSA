from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        rotten = deque()
        total = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    rotten.append((i,j))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        days = 0
        while rotten:
            K = len(rotten)
            count += K
            for _ in range(K):
                x,y = rotten.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or ny <0 or nx >=m or ny >=n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    rotten.append((nx,ny))
            if rotten:
                days += 1
        return days if total == count else -1


        