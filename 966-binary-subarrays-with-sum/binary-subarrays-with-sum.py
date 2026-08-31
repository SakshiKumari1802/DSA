class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atmost(k):
            if k < 0:
                return 0
            l =0
            r = 0
            count = 0
            total = 0
            for r in range(len(nums)):
                total += nums[r]
                while total > k:
                    total -= nums[l]
                    l += 1
                count += r-l+1
            return count


        return atmost(goal)-atmost(goal-1)
        