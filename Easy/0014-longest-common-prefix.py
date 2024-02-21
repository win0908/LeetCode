class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        base = strs[0]

        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or base[i] != word[i]: 
                    return base[0:i]
        
        return strs[0]
