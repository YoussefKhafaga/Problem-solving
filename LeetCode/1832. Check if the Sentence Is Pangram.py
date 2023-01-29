class Solution(object):
    def checkIfPangram(self, sentence):
        dict = {}
        for letter in sentence:
            if letter not in dict:
                dict[letter] = 1
        if len(dict) == 26:
            return True
        else:
            return False
        