class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        word_list_one = []
        word_list_two = []

        for word in s:
            word_list_one.append(word)

        for word_two in t:
            word_list_two.append(word_two)
        
        return sorted(word_list_one) == sorted(word_list_two)

        
        