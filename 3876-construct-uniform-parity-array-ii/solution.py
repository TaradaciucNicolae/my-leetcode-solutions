class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        minimum = min(nums1)
        
        if minimum % 2 == 1: # If the minimum element is odd, we can make all elements odd
            return True
        else:
            # If the minimum is even, all elements must be even
            for num in nums1: 
                if num % 2 == 1: # if we find an odd number, it will be impossible to convert
                    return False
                    
        return True
