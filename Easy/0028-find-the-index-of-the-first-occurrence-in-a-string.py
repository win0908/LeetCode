class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack) - len(needle) + 1):
            
            n = 0
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    n+=1 
                if n == len(needle): return i

        return -1
