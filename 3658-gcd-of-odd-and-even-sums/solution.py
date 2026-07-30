import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        sumOdd = n * n
        sumEven = n * (n+1)
        
        return math.gcd(sumOdd, sumEven)



        # sumOdd = 0

        # sumEven = 0

        # i = 1
        
        # limit = n * 2

        # while i<= limit:

        #     if i % 2 == 0:
        #         sumEven += i
        #     else:
        #         sumOdd += i

        #     i += 1
        
        # return math.gcd(sumEven, sumOdd)
