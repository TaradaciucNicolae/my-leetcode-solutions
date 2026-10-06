class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_opening = 0  # how many "(" need closing
        unmatched_closing = 0  # how many ")" need opening

        for each in s:
            if each == '(':
                unmatched_opening += 1

            elif unmatched_opening > 0:
                unmatched_opening -= 1   # this ")" closes an open "("
                
            else:
                unmatched_closing += 1   # unmatched ")"

        return unmatched_opening + unmatched_closing
