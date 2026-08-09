class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        total_remaining_stones_from=[0] * (n+1)


        for i in range( n-1 , -1 ,-1):
            total_remaining_stones_from[i] = total_remaining_stones_from[i+1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i,m): # index in piles, M

            if 2* m >= n-i:

                return total_remaining_stones_from[i]

            best = 0

            for x in range(1, 2*m + 1):

                stones_opponent_will_take_optimally = dp(i+x, max(m, x))

                stones_left_for_me = total_remaining_stones_from[i] - stones_opponent_will_take_optimally

                best = max(best, stones_left_for_me)
            
            return best



        return dp(0,1)
