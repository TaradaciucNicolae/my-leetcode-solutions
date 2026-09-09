class Solution:
    def countCommas(self, n: int) -> int:

        left = 1 # we create a group, left - right
        right = 999
        commas = 0
        counter = 0 # commas in the current group

        while n > right:
            commas += counter * (right-left+1) # adding the whole group
            
            # changing to the next group
            left = right + 1
            right = right * 1000 + 999
            counter += 1

        # when n < right means we are at the final group and we add the rest of the numbers left
        commas += counter * (n-left+1)

        return commas
