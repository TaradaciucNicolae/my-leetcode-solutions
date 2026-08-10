class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n + 1)   # dp[i] means if player has i stones left in the pile, does he win ?


        dp[0] = False # you can't win if it's your turn and there are no more stones left

        for i in range(1, n+1):
           
            k =1
            while k*k <= i: # we check the squares
                if dp[i - k*k] == False: # we check which moves are " the finishing moves"
                    dp[i] = True
                    break
                k+=1

        
        return dp[n]
