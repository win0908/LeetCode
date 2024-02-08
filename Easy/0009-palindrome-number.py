class Solution:
    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        if len(x) <= 1:
            return True

        a = 0
        b = len(x) - 1
        while a < b:
            if x[a] != x[b]:
                return False 
            a+=1
            b-=1

        return True

        
        # using String
        '''
        s = str(x)
        return ( s == s[::-1] )
        '''
