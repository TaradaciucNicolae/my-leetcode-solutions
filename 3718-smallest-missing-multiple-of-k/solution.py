class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            multiple = k * i

            if multiple not in nums:
                return multiple
            
            i += 1
