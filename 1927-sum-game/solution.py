class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        half_1 = num[0:n//2]
        half_2 = num[n//2: n]
        q_in_1, sum_in_1, q_in_2, sum_in_2 = 0,0,0,0

        for each in half_1:
            if each == "?":
                q_in_1 +=1
            else:
                sum_in_1 += int(each)

        for each in half_2:
            if each == "?":
                q_in_2 +=1
            else:
                sum_in_2 += int(each)

        return (2 * sum_in_1 + q_in_1 * 9) != (2 * sum_in_2 + q_in_2 * 9)
