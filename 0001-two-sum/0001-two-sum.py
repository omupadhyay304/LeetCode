class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dickshionary = {}
        
        for i, nums in enumerate(nums):
            complement = target - nums
            
            if complement in dickshionary:
                return(dickshionary[complement],i)
            
            dickshionary[nums] = i
                
                
                