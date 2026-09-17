class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        res, tot, i = n + 1, 0, 0

        dp = [n] * (n + 1)

        for j in range(n):
            tot += arr[j]

            while tot > target:
                tot -= arr[i]
                i += 1
                
            dp[j + 1] = dp[j]

            if tot == target:
                Len = j - i + 1

                res = min(res, Len + dp[i])
                dp[j + 1] = min(dp[j], Len)
                
        return -1 if res == n + 1 else res
