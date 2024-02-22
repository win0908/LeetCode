class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = int(a,2)
        b = int(b,2)
        sum = int(a) + int(b)
        return "{0:b}".format(int(sum))
