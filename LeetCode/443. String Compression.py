class Solution(object):
    def compress(self, chars):
        string = ""
        currchar = chars[0]
        currsum = 0
        for char in chars:
            if char == currchar:
                currsum += 1
            else:
                if currsum != 1:
                    string = string + currchar + str(currsum)
                else:
                    string = string + currchar
                currchar = char
                currsum = 1
        if currsum != 1:
            string = string + currchar + str(currsum)
        else:
            string = string + currchar
        return len(string)
