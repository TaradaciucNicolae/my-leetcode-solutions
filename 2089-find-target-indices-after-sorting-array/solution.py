class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(nums)
        list_of_indices =[]

        for i in range(len(nums)):
            
            if nums[i] == target:
                list_of_indices.append(i)

        return list_of_indices
