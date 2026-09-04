class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(0,n):

            inst_score = max(nums[0:i +1]) - min(nums[i:n-1 +1])
            print(i,inst_score)
            if inst_score <= k:
                return i
        
        return -1
