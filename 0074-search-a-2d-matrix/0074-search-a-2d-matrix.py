class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return false
        
        m,n = len(matrix) , len(matrix[0])
        left , right = 0 , m*n-1
        
        while left <= right:
            mid = (left+right) //2
            row = mid // n
            col = mid % n
            matrix_value = matrix[row][col]
            
            if matrix_value == target:
                return True
            elif matrix_value < target:
                left = mid+1
            else:
                right = mid-1
            
        return False