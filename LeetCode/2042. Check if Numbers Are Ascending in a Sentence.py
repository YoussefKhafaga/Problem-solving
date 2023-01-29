class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ints = []
        s = s.split()
        for k in s:
            if k.isdigit():
                ints.append(int(k))
        for i in range(1, len(ints)):
            if ints[i-1] >= ints[i]:
                return False
        return True