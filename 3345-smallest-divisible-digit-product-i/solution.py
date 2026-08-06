class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:

            product = 1
            new_n = n

            while new_n:
                
                digit = new_n % 10
                new_n = new_n // 10
                product *= digit

            if product % t == 0:
                return n

            n +=1
