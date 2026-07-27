class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # n=len(nums)
        # max_comb=0

        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         max_comb = max(max_comb, (nums[i] - 1) * (nums[j] - 1) )
        
        # return max_comb


        biggest = 0
        second_biggest = 0

        for val in nums:

            if val >= biggest:

                second_biggest = biggest

                biggest = val
            
            elif val < biggest and val > second_biggest:

                second_biggest = val

        
        return (biggest -1) * ( second_biggest -1)
