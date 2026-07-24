class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)

        pair_xor = set()

        triple_xor = set()

        for i in range(n):
            for j in range(i,n):
                    pair_xor.add(nums[i] ^ nums[j])


        for val in pair_xor:
            for j in range(n):
                triple_xor.add(val ^ nums[j])


        return len(triple_xor)
