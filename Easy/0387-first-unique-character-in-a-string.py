
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1 :
            return 0

        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1


        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
    
