class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        maxi = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                c += 1
            else:
                c = 0
            maxi = max(maxi,c)
        return maxi
        
        