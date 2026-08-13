'''Example:
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''
#Link:https://leetcode.com/problems/length-of-last-word/description/
#Code:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string=s.strip()
        w=string.split()
        last_word=w[-1]
        return(len(last_word))
