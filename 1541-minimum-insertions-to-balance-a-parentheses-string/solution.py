class Solution:
    def minInsertions(self, s: str) -> int:
        
        opening_unmatched =0
        insertions = 0
        previous_char = ""

        for each in s:
            if each == "(":
                opening_unmatched += 1
                previous_char = ""

            elif each == ")" and previous_char == ")": # second ")"
                insertions -=1
                previous_char = ""


            elif each ==")" and opening_unmatched >= 1: # first ")" after a "("
                opening_unmatched -= 1
                insertions += 1 # assuming that the second ")" is missing
                previous_char = ")"
            
            else:
                insertions += 2  # first ")" and we miss both "(" and ")"
                previous_char = ")"

        return insertions + 2 * opening_unmatched
