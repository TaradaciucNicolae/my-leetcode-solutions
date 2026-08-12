class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_dict = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            current = nums[right]
            freq_dict[current] += 1

            while freq_dict[current] > k:
                freq_dict[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
