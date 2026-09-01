class Solution(object):
    def minWindow(self, s, t):
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        l = 0
        have = 0
        needCount = len(need)

        minLen = float('inf')
        start = 0

        for r in range(len(s)):

            ch = s[r]

            if ch in need:
                window[ch] = window.get(ch, 0) + 1

                if window[ch] == need[ch]:
                    have += 1

            while have == needCount:

                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    start = l

                leftChar = s[l]

                if leftChar in need:
                    window[leftChar] -= 1

                    if window[leftChar] < need[leftChar]:
                        have -= 1

                l += 1

        if minLen == float('inf'):
            return ""

        return s[start:start + minLen] 