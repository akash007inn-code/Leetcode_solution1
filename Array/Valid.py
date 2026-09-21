...
Example 1:
Input: word = "234Adas"
Output: true
#
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum():
            return False
            
        word_set = set(word)
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        
        return not word_set.isdisjoint(vowels) and not word_set.isdisjoint(consonants)
