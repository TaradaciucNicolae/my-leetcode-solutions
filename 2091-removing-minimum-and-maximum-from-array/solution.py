class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        i_min = nums.index(min(nums))
        i_max = nums.index(max(nums))

        left = min(i_min, i_max)
        right = max(i_min, i_max)

        opt_1 = right + 1 # all from left
        opt_2 = n - left # all from right
        opt_3 = left + 1 + n - right # from both sides

        return min(opt_1, opt_2, opt_3)
