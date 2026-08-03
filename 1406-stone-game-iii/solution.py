from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def maxDiff(startIndex: int) -> int:
            if startIndex == n:
                return 0

            take_one = float("-inf")
            take_two = float("-inf")
            take_three = float("-inf")

            if startIndex < n:
                take_one = stoneValue[startIndex] - maxDiff(startIndex + 1)

            if startIndex + 1 < n:
                take_two = stoneValue[startIndex] + stoneValue[startIndex + 1] - maxDiff(startIndex + 2)

            if startIndex + 2 < n:
                take_three = stoneValue[startIndex] + stoneValue[startIndex + 1] + stoneValue[startIndex + 2] - maxDiff(startIndex + 3)


            return max(take_one, take_two, take_three)

        final_difference = maxDiff(0)

        if final_difference > 0:
            return "Alice"
        elif final_difference < 0:
            return "Bob"

        return "Tie"
