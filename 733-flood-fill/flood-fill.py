from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m,n = len(image), len(image[0])
        original = image[sr][sc]
        if original == color:
            return image
        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx= x+dx
                ny = y+dy
                if nx < 0 or ny < 0 or nx>=m or ny>=n:
                    continue
                if image[nx][ny]== original:
                    image[nx][ny] = color
                    queue.append((nx,ny))
        return image


                



        