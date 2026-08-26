class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        output=""
        n=len(s)

        for i in range(n):
            search=""
            counter=0

            for j in range(i,n):

                search += s[j]
                if s[j] == "1":
                    counter += 1

                if counter == k:
                    if output == "": # first finding
                        output = search

                    elif len(search) < len(output):#found sth better
                        output = search
                    
                    elif len(search) == len(output) and search < output: #found sth with same len that's lexicographically smaller
                        output = search

                    break

        return output
