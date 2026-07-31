class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        level = 0
        for char in s:
            if char == '(':
                if level > 0:
                    result += char
                level += 1
            elif char == ')':
                level -= 1
                if level > 0:
                    result += char
        return result
        