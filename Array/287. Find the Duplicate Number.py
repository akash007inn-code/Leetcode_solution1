...
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

#
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low

  
