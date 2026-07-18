from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # freq[x] = de câte ori apare x în nums
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        # gcd_count[g] = câte perechi au GCD exact g
        gcd_count = [0] * (max_val + 1)

        # Mergem descrescător ca să putem scădea multiplii deja calculați
        for g in range(max_val, 0, -1):
            count = 0

            # Numărăm câte numere sunt divizibile cu g
            for multiple in range(g, max_val + 1, g):
                count += freq[multiple]

            # Toate perechile unde ambele numere sunt divizibile cu g
            total_pairs = count * (count - 1) // 2

            # Scădem perechile care au GCD exact 2g, 3g, 4g...
            for multiple in range(2 * g, max_val + 1, g):
                total_pairs -= gcd_count[multiple]

            gcd_count[g] = total_pairs

        # prefix[g] = câte perechi au GCD <= g
        prefix = [0] * (max_val + 1)

        for g in range(1, max_val + 1):
            prefix[g] = prefix[g - 1] + gcd_count[g]

        answer = []

        for q in queries:
            # q este index 0-based.
            # Căutăm primul g unde prefix[g] > q
            ans = bisect_right(prefix, q)
            answer.append(ans)

        return answer
