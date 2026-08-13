class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        text = list(s)              # convert to list so we can modify characters
        n = len(text)

        # Each segment tree node stores information about its segment:
        prefixRun  = [0] * (4 * n)  # longest run that STARTS at the left edge of the segment
        suffixRun  = [0] * (4 * n)  # longest run that ENDS at the right edge
        bestRun    = [0] * (4 * n)  # longest run anywhere in the segment (the answer we want)
        leftChar   = [0] * (4 * n)  # character at the left end of the segment
        rightChar  = [0] * (4 * n)  # character at the right end of the segment
        segLength  = [0] * (4 * n)  # length of the segment (how many characters it covers)

        # Combine two children (left + right) into their parent.
        # This is where all the "magic" happens: we check if the runs at the border merge.
        def merge(node):
            left  = 2 * node
            right = 2 * node + 1

            # Parent's ends = left end of left child and right end of right child
            leftChar[node]  = leftChar[left]
            rightChar[node] = rightChar[right]
            segLength[node] = segLength[left] + segLength[right]

            # Initial candidate: best run from each child, taken separately
            bestRun[node] = max(bestRun[left], bestRun[right])

            # Parent's prefix and suffix start from the border children
            prefixRun[node] = prefixRun[left]
            suffixRun[node] = suffixRun[right]

            # If the border has the same character (right of left child == left of right child),
            # the runs in the middle can join into a longer one.
            if rightChar[left] == leftChar[right]:
                # New candidate: left suffix + right prefix, glued together
                bestRun[node] = max(bestRun[node], suffixRun[left] + prefixRun[right])

                # If the ENTIRE left child is a single character, the prefix extends into the right
                if prefixRun[left] == segLength[left]:
                    prefixRun[node] = prefixRun[left] + prefixRun[right]

                # If the ENTIRE right child is a single character, the suffix extends into the left
                if suffixRun[right] == segLength[right]:
                    suffixRun[node] = suffixRun[right] + suffixRun[left]

        # Build the tree from text (done once, at the start).
        def build(node, lo, hi):
            if lo == hi:
                # Leaf: a single character, so all runs have length 1
                leftChar[node] = rightChar[node] = text[lo]
                prefixRun[node] = suffixRun[node] = bestRun[node] = 1
                segLength[node] = 1
                return
            mid = (lo + hi) // 2
            build(2 * node,     lo,      mid)
            build(2 * node + 1, mid + 1, hi)
            merge(node)

        # Change a single character (at position idx) and recompute on the way up to the root.
        def update(node, lo, hi, idx, newChar):
            if lo == hi:
                leftChar[node] = rightChar[node] = newChar
                return
            mid = (lo + hi) // 2
            if idx <= mid:
                update(2 * node,     lo,      mid, idx, newChar)
            else:
                update(2 * node + 1, mid + 1, hi,  idx, newChar)
            merge(node)  # after update, re-merge to propagate the change upward

        build(1, 0, n - 1)

        result = []
        for newChar, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, newChar)
            result.append(bestRun[1])   # bestRun[1] = root = longest run in the whole text
        return result
