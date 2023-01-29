class Solution(object):
    def countCharacters(self, words, chars):
        dict1 = {}
        sum1 = 0
        for char in chars:
            if char in dict1.keys():
                dict1[char] = dict1[char] + 1
            else:
                dict1[char] = 1
        print(dict1)
        for word in words:
            found = 1
            dict2 = {}
            for char in word:
                if char in dict1.keys() and char not in dict2.keys():
                    dict2[char] = 1
                    continue
                elif char in dict1.keys() and char in dict2.keys():
                    dict2[char] = dict2[char] + 1
                else:
                    found = 0
            print(dict2)
            for char in dict2.keys():
                if dict2[char] > dict1[char]:
                    found = 0
            if found == 1:
                sum1 += len(word)
        return sum1