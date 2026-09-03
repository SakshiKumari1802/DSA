class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = l + (r - l) // 2

            days_used = 1
            curr = 0

            for w in weights:
                if curr + w <= mid:
                    curr += w
                else:
                    days_used += 1
                    curr = w

            if days_used <= days:
                r = mid
            else:
                l = mid + 1

        return l