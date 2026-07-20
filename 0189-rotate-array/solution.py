class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k % n  # pt cazurile in care avem 5 in nums si cere sa rotim de 7 ori, practic rezultatul e identic ca si la k=2

        last_k_nums = nums[-k:]

        nums_without_last_k = nums[:-k]

        nums[:] = last_k_nums + nums_without_last_k
