class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        output = []

        for each in nums:
            if each not in output:
                output.append(each)

        
        nums[:] = output
        return len(output)
