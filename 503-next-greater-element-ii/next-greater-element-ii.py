class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack =[]
        n = len(nums)
        res = [-1]*n
        for i in range(2*n):
         current = nums[i%n]

         while stack and nums[stack[-1]]< current:
            index = stack.pop()
            res[index] = current
        
         if i<n:
            stack.append(i)
        return res