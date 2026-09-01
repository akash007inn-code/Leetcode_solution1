...
Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33

#
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1




