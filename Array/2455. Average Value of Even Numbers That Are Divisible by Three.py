'''Example:
Example 1:
Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.'''
#link
https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
#code
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total_sum = 0
        count = 0
        for x in nums:
            if x % 6 == 0:
                total_sum = total_sum+x
                count = count+1
        if count == 0:
            return 0
        return total_sum // count
