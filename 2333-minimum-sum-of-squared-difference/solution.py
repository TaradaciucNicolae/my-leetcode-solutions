class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2

        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        diffs.sort() # Sorting so the biggest differences are at the end

        level = diffs[n-1]  # current biggest difference
        count = 1           # how many differences are currently equal to level
        
        remainder = 0       # how many differences in the group drop, to level - 1

                            # Example: 3 differences of 7, only 2 operations left
                            #          -> two become 6, one stays 7 -> remainder = 2

                            # If we never get into that situation, it stays 0

        while level > 0:

            # Differences that reached the same value as level join the counter
            # The first difference to the left of the group(at level) is at index n - count - 1
            while count < n and diffs[n-count-1] == level:
                count += 1

            # Lowering the whole group by 1 costs count operations (one per difference)
            # If we have fewer operations than that, we can only lower k of them by 1
            # Example: 3 differences of 7 and k = 2 -> two become 6, one stays 7 -> remainder = 2
            if k < count:
                remainder = k
                break

            # We have enough operations: lower the whole group by 1
            k -= count
            level -= 1


        for i in range(n - count, n):
            diffs[i] = level

        for i in range(n - count, n - count + remainder):
            diffs[i] = level - 1

        return sum(x*x for x in diffs)
