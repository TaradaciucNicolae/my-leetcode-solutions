class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        n= len(s)
        i = 0
        curr_char = s[i]
        new_s =""
        middle=""
        all_chars = [0] * 26

        for each_char in s[:n]:
            val = ord(each_char)
            all_chars[val-97] +=1

        for i in range(26):

            while all_chars[i] >= 3:
                new_s += chr(i+97)
                all_chars[i] -= 2


            if all_chars[i] == 1:
                middle = chr(i+97)
            
            if all_chars[i] == 2:
                new_s += chr(i+97)




        return new_s + middle + new_s[::-1]
