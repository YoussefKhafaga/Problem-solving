class Solution:
    def reorderSpaces(self, text: str) -> str:
        if len(text) < 2:
            return text
        final = ""
        space = 0
        extra = 0 
        for char in text:
            if char == " ":
                space += 1
        words = list(text.split())
        if len(words) == 1:
            final += words[0]
            for j in range(0, space):
                final += " "
            return final
        spaces = int(space / (len(words) - 1))
        if int((space) % (len(words)-1)) != 0:
            extra = int((space) % (len(words)-1))
        for j in range(len(words)):
            final += words[j]
            if j == len(words)-1:
                break
            for i in range(0, spaces):
                final += " "
        for i in range(0, extra):
            final += " "
        return final