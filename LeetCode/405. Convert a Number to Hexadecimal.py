class Solution(object):
    def toHex(self, num):
        if num < 0:
            num += 4294967296
        return format(num, 'x')
        