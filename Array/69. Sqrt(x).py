...
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        ans = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

