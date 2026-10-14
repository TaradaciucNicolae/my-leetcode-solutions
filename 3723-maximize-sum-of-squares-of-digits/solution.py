class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        if sum > 9 * num:
            return ""

        nines = sum // 9 # how many nines fit in sum
        rest = sum % 9 # what is left after the nines

        result = "9" * nines # we're adding the nines first

        if rest > 0:
            result += str(rest) # adding the rest

        result += "0" * (num - len(result)) # if we still did not get to the length requested, we're adding 0's
        return result


        # TLE ↓
        #     
        # for value in range(10**num - 1, 10**(num-1) -1, -1):
        #     sum_of_digits = 0
        #     x = value

        #     while x > 0:
        #         digit = x % 10
        #         sum_of_digits += digit
        #         x //=10

        #     if(sum_of_digits == sum):
        #         return str(value)
        

        # return ""
