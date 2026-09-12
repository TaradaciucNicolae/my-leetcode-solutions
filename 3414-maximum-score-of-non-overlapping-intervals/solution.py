import bisect
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        MAX_PICKS = 4
        n = len(intervals)

        # Sort by right end, but remember where each interval came from
        items = [(l, r, w, pos) for pos, (l, r, w) in enumerate(intervals)]
        items.sort(key=lambda item: item[1])
        right_ends = [item[1] for item in items]

        # safe_count[i] = how many intervals sit fully to the LEFT of items[i]
        # bisect_left gives the first index with right_end >= left
        safe_count = [bisect.bisect_left(right_ends, items[i][0]) for i in range(n)]


        best = [[(0, []) for _ in range(MAX_PICKS + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            left, right, weight, position = items[i - 1]
            safe_block = safe_count[i - 1]

            for k in range(1, MAX_PICKS + 1):
                # Leave it out: the answer is whatever we already had.
                skip_score, skip_list = best[i - 1][k]

                # Take it: add its weight, spend one pick, and continue from
                # the safe block, skipping everything that would overlap.
                base_score, base_list = best[safe_block][k - 1]
                take_score = base_score + weight
                take_list = sorted(base_list + [position])

                # Bigger score wins, ties go to the smaller list of positions.
                if take_score > skip_score:
                    best[i][k] = (take_score, take_list)
                elif take_score < skip_score:
                    best[i][k] = (skip_score, skip_list)
                elif take_list < skip_list:
                    best[i][k] = (take_score, take_list)
                else:
                    best[i][k] = (skip_score, skip_list)

        return best[n][MAX_PICKS][1]
