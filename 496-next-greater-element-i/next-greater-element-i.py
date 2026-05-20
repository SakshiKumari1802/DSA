class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        mp = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                mp[smaller] = num
            stack.append(num)
        while stack:
            mp[stack.pop()] = -1
        ans = []
        for num in nums1:
            ans.append(mp[num])
        return ans 