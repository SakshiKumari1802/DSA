class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l = 1
        r = max(nums)
        while l < r:
            mid = l+(r-l)//2
            sum = 0
            for num in nums:
                sum += (num + mid - 1)//mid
            if sum > threshold:
                l = mid +1
            else:
                r = mid
        return l
        