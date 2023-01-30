class Solution(object):
    def lengthOfLongestSubstring(self, s):
        string = ''
        maxx = 0
        for char in s:
            if char not in string:
                string += char
            else:
                string = string[string.index(char) + 1:] + char
            if len(string) > maxx:
                maxx = len(string)
        return maxx