class Solution(object):

    def largestRectangleArea(self, heights):

        n = len(heights)
        stack = []

        maxArea = 0

        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:

                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                maxArea = max(maxArea, h * width)

            stack.append(i)

        # Remaining bars
        while stack:

            h = heights[stack.pop()]

            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1

            maxArea = max(maxArea, h * width)

        return maxArea