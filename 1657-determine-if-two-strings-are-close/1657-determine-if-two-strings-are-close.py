class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        frequency1 = Counter(word1)
        frequency2 = Counter(word2)

        sorted_word_1 = sorted(frequency1.values())
        sorted_word_2 = sorted(frequency2.values())

        keys_match = set(frequency1.keys()) == set(frequency2.keys())

        return sorted_word_1 == sorted_word_2 and keys_match