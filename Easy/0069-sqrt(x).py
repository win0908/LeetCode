class Solution:
    def mySqrt(self, x: int) -> int:

        return int(abs(x)**0.5)
        
        # i = 1
        # count = 0
        
        # while x > 0:
        #     x -= i
        #     i+=2
        #     count += 1
        
        # if x < 0: return count-1
        # else: return count
        
