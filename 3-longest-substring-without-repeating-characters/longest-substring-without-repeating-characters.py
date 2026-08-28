class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = [-1]*256
        l = 0
        r = 0
        maxlen = 0
        current = 0
        
        while r < len(s):
            if hash[ord(s[r])] != -1:
                l = max((hash[ord(s[r])])+1,l)
            current = r+1-l
            maxlen = max(current,maxlen) 
            hash[ord(s[r])] = r
            r += 1
        return maxlen
    
                 