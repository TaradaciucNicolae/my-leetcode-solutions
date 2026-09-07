class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        total = 0

        ending_with = {} # ending_with['a'] = how many distinct subsequences currently end with 'a'

        for letter in s:

            duplicates = ending_with.get(letter, 0)   # 0 if the letter was never seen
            # every old string ending in "letter" gets rebuilt identically:
            # "ba" is "b" + 'a', and "b" still exists. So ending_with[letter] is exactly the duplicate count

            n_of_subseq = total + 1 - duplicates # if we had ( a, b, ab ) now we have ( ac, bc, abc, c ) and we add it to our total

            # The group for this letter grows by the new strings we just made.
            ending_with[letter] = ending_with.get(letter, 0) + n_of_subseq

            total = total + n_of_subseq

        return total % MOD
