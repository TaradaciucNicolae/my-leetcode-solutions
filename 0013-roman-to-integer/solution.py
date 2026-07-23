class Solution:
    def romanToInt(self, s: str) -> int:

        
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }


        nr =0
        rev_s = s[::-1]
        n = len(rev_s)

        nr += roman_to_int[rev_s[0]]



        for i in range(1,n):

            if roman_to_int[rev_s[i]] < roman_to_int[rev_s[i-1]]:
                nr -= roman_to_int[rev_s[i]]
            else:
                nr += roman_to_int[rev_s[i]]




            
        return nr
