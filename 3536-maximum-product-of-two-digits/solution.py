class Solution:
    def maxProduct(self, n: int) -> int:
        
        # max_pair = 0

        # for i, each_1 in enumerate(str(n)):

        #     val_1 = int(each_1)

        #     for j, each_2 in enumerate(str(n)):

        #         val_2 = int(each_2)

        #         if i != j:
        #             max_pair = max(max_pair, val_1 * val_2)

        
        # return max_pair



        # Because it's a pair, we can search for the 2 biggest digits


        first = 0
        second = 0

        while n > 0:

            digit = n % 10

            if digit >= first:
                second = first
                first = digit   

            elif digit > second:
                second = digit

            n  =  n // 10

        return first*second
