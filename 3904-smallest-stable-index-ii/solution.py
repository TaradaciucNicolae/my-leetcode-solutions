class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # mn[i] = minimum from nums[i:] (sufix)
        mn = [0] * n
        mn[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            mn[i] = min(nums[i], mn[i + 1])

        # mx = max from nums[0:i+1] (prefix)
        mx = float('-inf')
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - mn[i] <= k:
                return i

        return -1
