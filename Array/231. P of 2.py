...
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
      
