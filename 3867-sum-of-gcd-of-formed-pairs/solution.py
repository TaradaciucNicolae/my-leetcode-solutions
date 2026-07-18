class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        max_so_far = 0

        # Construim array-ul prefixGcd
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefixGcd.append(gcd(num, max_so_far))

        # Sortăm prefixGcd
        prefixGcd.sort()

        # Facem perechi: cel mai mic cu cel mai mare
        left = 0
        right = len(prefixGcd) - 1
        total = 0

        while left < right:
            total += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return total
