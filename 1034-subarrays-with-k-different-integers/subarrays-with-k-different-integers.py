class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(p):
            n = len(nums)
            l = 0
            ch = {}
            count = 0
            for r in range(n):
                ch[nums[r]] = ch.get(nums[r],0)+1
                while len(ch)>p:
                    ch[nums[l]] -= 1
                    if ch[nums[l]] == 0:
                        del ch[nums[l]]
                    l += 1
                count += r-l+1
            return count
        return atmost(k)-atmost(k-1)
        