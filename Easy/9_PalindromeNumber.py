
'''
LeetCode
9.) Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:
-231 <= x <= 231 - 1


Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

# Input
x = 121


# First Time
x = str(x)
txt = ''
for i in range(len(x)):
    txt += x[len(x)-1-i]

if txt == x: print(True)
else: print(False)
'''
Runtime: 43ms
Memory:  13.19MB
'''



# using String
s = str(x)
print( s == s[::-1] )
'''
Runtime: 19ms
Memory:  13.22MB
'''




