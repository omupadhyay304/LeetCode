from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        # Dictionary to store the frequency of each element
        frequency = {}
        
        # Count the frequency of each element
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # List to store the duplicates
        duplicates = []
        
        # Collect elements that occur more than once
        for num, count in frequency.items():
            if count > 1:
                duplicates.append(num)
        
        # Sort the list of duplicates in ascending order
        duplicates.sort()
        
        # If no duplicates found, return [-1]
        if not duplicates:
            return [-1]
        
        return duplicates



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends