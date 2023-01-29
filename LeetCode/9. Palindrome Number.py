class Solution(object):
    def isPalindrome(self, x): 
        if x < 0:
            return False
        x = str(x)
        mid = int(floor(len(x)/2))
        for i in range(0 ,mid):
            if x[i] != x[len(x)-i-1]:
                return False
        return True
        