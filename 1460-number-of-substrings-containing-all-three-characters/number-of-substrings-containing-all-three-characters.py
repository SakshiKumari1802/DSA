class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1,-1,-1]
        ans = 0
        for r in range(len(s)):
            last[ord(s[r])-ord('a')] = r
            if last[0]!=-1 or last[1] != -1 or last[2] != -1:
                 ans += min(last)+1
        return ans