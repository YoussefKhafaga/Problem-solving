class Solution(object):
    def singleNumber(self, nums):
        res = 0
        #xor each res to get the final single number
        for n in nums:
            res = n ^ res
            
        return res
