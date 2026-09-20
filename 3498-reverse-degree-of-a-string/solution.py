class Solution:
    def reverseDegree(self, s: str) -> int:
        output = 0
        i=1
        for char in s:
            output += i * abs( ord(char) - 123)
            i +=1

        return output
