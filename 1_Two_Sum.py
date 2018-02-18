class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable={}
    
        for index,number in enumerate(nums):
            if target-number in hashtable:
                return [index,hashtable[target-number]]
            else:
                hashtable[number]=index