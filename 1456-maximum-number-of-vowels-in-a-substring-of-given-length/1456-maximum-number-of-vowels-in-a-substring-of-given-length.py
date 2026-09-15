class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = {'a', 'e', 'i', 'o', 'u'}
        max_vowel = 0
        current_vowel = 0
        left = 0

        for i in range(k):
            if s[i] in vowel:
                current_vowel+=1

        max_vowel = max(max_vowel, current_vowel)

        for i in range(k, len(s)):
            if s[left] in vowel:
                current_vowel-=1
                left+=1
            else:
                left+=1
            
            if s[i] in vowel:
                current_vowel+=1

            max_vowel = max(max_vowel, current_vowel)

        return max_vowel