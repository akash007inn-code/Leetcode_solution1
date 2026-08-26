...
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
#
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = [char.lower() for char in s if char.isalnum()]
        cleaned_string = "".join(cleaned_chars)
        reversed_string = cleaned_string[::-1]
        return cleaned_string == reversed_string



