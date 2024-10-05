class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        element1, element2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            if element1 == num:
                count1 +=1
            elif element2 == num:
                count2 +=1
            elif count1 == 0:
                element1 , count1 = num, 1
            elif count2 == 0:
                element2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        result = []
        count1 = nums.count(element1)
        count2 = nums.count(element2)
        
        if count1 > len(nums) //3:
            result.append(element1)
        if element1 != element2 and count2 > len(nums) //3:
            result.append(element2)
        
        return result