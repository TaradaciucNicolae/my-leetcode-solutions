class Solution:
    def minimumPushes(self, word: str) -> int:
        
        n = len(word)
        print(n)

        total = 0
        count = 1

        while n != 0:

            if n > 8:
                total  = total + 8 * count
                n -= 8
                count  += 1
                
            elif n <= 8:
                total = total + n * count
                n = 0
        
        return total
