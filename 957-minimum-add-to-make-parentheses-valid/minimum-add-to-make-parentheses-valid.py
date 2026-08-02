class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_brackets = 0
        close_brackets = 0
        for ch in s:
            if ch == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    close_brackets += 1
        return open_brackets + close_brackets
        