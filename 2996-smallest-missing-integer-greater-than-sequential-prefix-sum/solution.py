class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_current = nums[0]
        sum_of_biggest_list = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == num_current + 1:
                num_current = nums[i]
                sum_of_biggest_list += nums[i]
            else:
                break

        # Now we look for the smallest x >= prefix sum that does not exist in nums
        nums_set = set(nums)
        x = sum_of_biggest_list

        while x in nums_set:
            x += 1

        return x
