class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        if n == 1:
            return 1
        if n == 2:
            return 2
            
        for i in range(n-1):
            temp = a
            a += b
            b = temp
        return a
