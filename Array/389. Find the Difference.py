...
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_diff = sum(ord(char) for char in t) - sum(ord(char) for char in s)
        return chr(ascii_diff)







  
