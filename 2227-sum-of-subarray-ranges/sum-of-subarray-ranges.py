class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        left = [0] * n
        right = [0] * n

        stack = []

        # Previous Smaller
        for i in range(n):

            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]

            stack.append(i)

        stack = []

        # Next Smaller
        for i in range(n - 1, -1, -1):

            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i

            stack.append(i)

        minSub = 0

        for i in range(n):
            minSub += nums[i] * left[i] * right[i]
            

        stack =[]
        left = [0]*n
        right = [0]*n

         # Previous Smaller
        for i in range(n):

            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]

            stack.append(i)

        stack = []

        # Next Smaller
        for i in range(n - 1, -1, -1):

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i

            stack.append(i)
        maxSub = 0

        for i in range(n):

            maxSub += nums[i] * left[i] * right[i]
            
        
        return maxSub-minSub


        