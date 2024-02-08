'''
Leetcode
387.) First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
 

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
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
    



















