class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        
        MOD = 10**9 + 7
        n = len(s)
        output=[]

        # pt      s = "1  0   2   0    3    0    0     4", 
        # prefixSum = [1, 1,  3,  3,   6,   6,   6,   10]  -> tinem ce suma am avea daca am aduna tot de la 0 la i
        #   prefixX = [1, 1, 12, 12, 123, 123, 123, 1234]  -> tinem ce nr concatenat avem la momentul i, dar fara 0
        # prefixCount=[1, 1,  2,  2,   3,   3,   3,    4]  -> numaram nr de cifre diferite de 0 pana la momentul i

        prefixSum = [0] * (n+1)
        prefixX = [0] * (n+1)
        prefixCount = [0] * (n+1)

        # prefixSum[0] = int(s[0])
        # prefixX[0] = int(s[0])
        # prefixCount[0] = 1 if int(s[0]) >0 else 0

        power10 = [1] * (n + 1)
        for i in range(1, n + 1):
            power10[i] = (power10[i - 1] * 10) % MOD

        for i, char in enumerate(s,1):

            digit = int(char)

            prefixSum[i] = prefixSum[i-1] + digit
            

            if digit>0:
                
                prefixX[i] = (  prefixX[i-1]*10 + digit )    % MOD

                prefixCount[i] = prefixCount[i-1] +1

            else:

                prefixX[i] = prefixX[i-1]
                prefixCount[i] = prefixCount[i-1]



        for a,b in queries:

        
            suma_interval = prefixSum[b+1] - prefixSum[a]
            nr_digits_interval = prefixCount[b+1] - prefixCount[a]
            concatenarea_intrevalului = ( prefixX[b+1] - prefixX[a] * power10[nr_digits_interval] ) % MOD




            output.append((concatenarea_intrevalului * suma_interval) % MOD)
            

    
        return output


        '''
        Complexitate timp: avem power10 si de acolo avem O(n) apoi construite prefixuri, iar O(n), apoi avem procesarea de queries si acolo ar fi un q, adica nr de queries si ar fi O(q), iar daca le adunam astea 3 va da O(2n +q) = O(n+q)


        complexitate spatiu:

        avem 4 arays de spatiu n+1, deci un O(n) la feicare si ar fi O(4n) adica = o(n), dar avem si la output q elemente, deci ar fi si acolo un O(q), deci total ar da O(n+q)
   

        '''
