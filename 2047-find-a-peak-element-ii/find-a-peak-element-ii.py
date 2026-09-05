class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        l,r = 0,n-1
        while l <= r:
            mid = (l+r)//2
            row = 0
            for i in range(m):
                if mat[i][mid] > mat[row][mid]:
                    row = i
                
            if mid > 0 and mat[row][mid-1] > mat[row][mid]:
                r = mid -1 
            elif mid < n-1 and mat[row][mid + 1] > mat[row][mid]:
                l = mid + 1
            else:
                return [row,mid]
        