...
Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

#
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
        
