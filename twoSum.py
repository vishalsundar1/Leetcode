class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #the regular way of solving twoSum
        for i in range (0, len(nums)):
            for j in range (i+1, len(nums)):
                b = nums[i] + nums[j]
                if (b == target):
                    return [i, j]   
        
