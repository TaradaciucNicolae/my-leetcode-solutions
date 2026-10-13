class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        nums = [abs(number) for number in nums]
        nums=sorted(nums, reverse = True)
        n=len(nums)
        score = 0

        if n % 2 == 0:
            mid = int(n /2) -1
        else:
            mid = int(n /2)

        for i in range(n):
            if i <= mid:
                score += nums[i] ** 2
            else:
                score -= nums[i] ** 2

        return score
