class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        windowSize = n - k
        total = sum(cardPoints)
        windowSum = sum(cardPoints[:windowSize])
        minSum = windowSum
        for r in range(windowSize,n):
            windowSum += cardPoints[r]
            windowSum -= cardPoints[r-windowSize]
            minSum = min(minSum,windowSum)
        return total- minSum
        