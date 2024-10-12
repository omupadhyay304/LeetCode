class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}
        
        for i, nums in enumerate(nums):
            complement = target - nums
            
            if complement in d:
                return(d[complement],i)
            
            d[nums] = i
                
                
                