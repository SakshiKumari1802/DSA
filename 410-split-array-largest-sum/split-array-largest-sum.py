class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = max(nums)
        r = sum(nums)
        def ifpossible(maxSum):
            sA = 1
            cs = 0
            for num in nums:
                if cs + num <= maxSum:
                    cs += num
                else:
                    cs = num
                    sA += 1
            return sA <= k
        while l < r:
            mid = l+(r-l)//2
            if ifpossible(mid):
                r = mid
            else:
                l = mid + 1
        return l
        