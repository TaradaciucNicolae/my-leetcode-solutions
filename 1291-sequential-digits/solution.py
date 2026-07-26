class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
  
        result =[]

        max_length = len(str(high))
        for length in range(2, max_length + 1):

            max_start_digit = 10 - length
            for start_digit in range(1, max_start_digit + 1):
                number = 0
                digit = start_digit

                for _ in range(length):
                    number = number *10 + digit
                    digit +=1
                
                if low <= number <= high:
                    result.append(number)

            
        return result
