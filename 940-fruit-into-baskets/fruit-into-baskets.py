class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = {}
        current = 0
        maxlen = 0
        l = 0
        r = 0

        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r],0)+1
            while  len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            current = r-l+1
            maxlen = max(maxlen,current)
        return maxlen
        