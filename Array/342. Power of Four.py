...
Example 1:

Input: n = 16
Output: true ...
#Comment
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return false
        while n%4==0:
            n//=4
        return n==1
