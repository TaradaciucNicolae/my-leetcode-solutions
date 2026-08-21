class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def count(x):
            # returns how many numbers from 1 to x are a multiple of at least one coin
            result = 0
            
            for size in range(1, len(coins) + 1):  # size = 1, 2, 3, ... (individual, pairs, triplets, ...)
                for combo in combinations(coins, size):  # all subsets of current size
                    l = lcm(*combo)  # lcm of all coins in this subset
                    if size % 2 == 1:
                        result += x // l  # odd size → add (step 1, 3, 5, ...)
                    else:
                        result -= x // l  # even size → subtract (step 2, 4, 6, ...)
            
            return result


        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left+right) // 2

            if count(mid) >= k:
                right = mid  # if there are at least k valid numbers until mid, mid could be the answer, so we search lower
            else:
                left = mid + 1  # if there are less than k valid numbers until mid, the answer is higher

        
        return left
