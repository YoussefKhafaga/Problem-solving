class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        i = 0
        while i < len(word1):
            result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        while i < len(word2):
            result += word2[i]
            i += 1
        return result