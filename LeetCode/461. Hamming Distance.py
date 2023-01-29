class Solution(object):
    def hammingDistance(self, x, y):
        x = '{:032b}'.format(x)
        y = '{:032b}'.format(y)
        sum1 = 0
        i = len(x)-1
        while i >= 0:
            if x[i] != y[i]:
                sum1 += 1
            i -= 1
        return sum1 