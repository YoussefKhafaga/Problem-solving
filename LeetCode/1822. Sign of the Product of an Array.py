class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        for num in nums:
            result *= num
        if result > 0:
            return 1
        elif result < 0:
            return -1
        else:
            return 0