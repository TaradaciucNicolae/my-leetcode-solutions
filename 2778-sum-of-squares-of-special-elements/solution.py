class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_sq = 0

        for i in range(1,n+1):
            if n % i == 0:
                sum_of_sq += nums[i-1] ** 2
    
        return sum_of_sq
