class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        n= len(nums)
        mx_for_each = -1
        prefixGcd = [0] *n

        for i in range(n):
            mx_for_each = max(mx_for_each, nums[i])
            prefixGcd[i] = math.gcd(mx_for_each, nums[i])

        prefixGcd = sorted(prefixGcd)

        sum_for_pairs = 0
        

        left = 0
        right = len(prefixGcd) - 1

        while left < right:
            sum_for_pairs += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return sum_for_pairs
