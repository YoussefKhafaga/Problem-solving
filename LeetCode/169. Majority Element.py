class Solution(object):
    def majorityElement(self, nums):
        dict1 = {}
        for num in nums:
            if num in dict1.keys():
                dict1[num] = dict1[num] + 1
            else:
                dict1[num] = 1
        for num in dict1:
            if dict1[num] > (len(nums)/2):
                return num