...
Example 1:

Input: nums = [2,2,1]

Output: 1
#Comment
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
