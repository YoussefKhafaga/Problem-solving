class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            sumbefore = sum(nums[:i])
            sumafter = sum(nums[i+1:])
            print(i, sumbefore,sumafter)
            if sumbefore == sumafter:
                return i
        return -1