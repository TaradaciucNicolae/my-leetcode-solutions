class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s =0
        p =1
        n2=n

        while n:
            each = n % 10
            n=n // 10
            s +=each
            p *=each
        
        if n2 % (s+p) == 0:
            return True
        else:
            return False
