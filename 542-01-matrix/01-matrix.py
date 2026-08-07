from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(mat)       # Number of rows
        m = len(mat[0])    # Number of columns

        # Visited matrix to track visited cells
        vis = [[0] * m for _ in range(n)]
        # Distance matrix to store result
        dist = [[0] * m for _ in range(n)]

        # Queue to perform BFS: stores (row, col, steps)
        q = deque()

        # Initialize queue with all cells containing 1
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))  # (row, col, distance)
                    vis[i][j] = 1       # Mark as visited
                else:
                    vis[i][j] = 0       # Mark as unvisited

        # Directions: Up, Right, Down, Left
        del_row = [-1, 0, 1, 0]
        del_col = [0, 1, 0, -1]

        # BFS traversal
        while q:
            row, col, steps = q.popleft()
            dist[row][col] = steps  # Assign distance

            # Explore all 4 directions
            for i in range(4):
                nrow = row + del_row[i]
                ncol = col + del_col[i]

                # Check for valid and unvisited cell
                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0:
                    vis[nrow][ncol] = 1  # Mark visited
                    q.append((nrow, ncol, steps + 1))  # Add with incremented distance

        return dist

        