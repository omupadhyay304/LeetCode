class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element , count = 0,0

        for n in nums:
            if count == 0:
                element = n
            if n == element:
                count += 1
            else:
                count -= 1
        return element
