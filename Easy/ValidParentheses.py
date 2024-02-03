
'''
LeetCode
20.) Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
3.Every close bracket has a corresponding open bracket of the same type.
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''


# Input
s = "()[]{}"


# First Time
stack = []
lookup = {
    ")":"(",
    "}":"{",
    "]":"["
}



for P in s:
    if P in lookup.values():
        stack.append(P)
    elif stack and lookup[P] == stack[-1]:
        stack.pop()
    else:
        print (False)

print(stack == [])







