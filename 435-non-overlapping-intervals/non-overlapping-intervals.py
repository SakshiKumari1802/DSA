class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()   # sort by start time

        remove = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= prev_end:
                prev_end = end
            else:
                remove += 1
                prev_end = min(prev_end, end)

        return remove
        