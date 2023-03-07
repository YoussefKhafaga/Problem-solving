class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        j = 0
        while(True):
            if i not in arr:
                k-=1
                if k == 0:
                    break
            i +=1
        return i