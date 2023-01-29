import math
class Solution(object):
    def secondHighest(self, s):
        res = set()
        for a in s:
            if a.isdigit():
                res.add(int(a))
        if len(res) <= 1:
            return -1
        return sorted(list(res))[-2]
    
