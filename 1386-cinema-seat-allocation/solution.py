class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        

        rows = {}
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = [0] * 10 # we add only the rows mentioned
            rows[row][seat - 1] = 1


        output = (n - len(rows)) * 2 # the rest of the rows not mentioned are full of zeroes => 2 free blocks

        for seat_list in rows.values(): # we take each row

            b1_is_empty = True
            for column in [2, 3, 4, 5]:
                if seat_list[column - 1] != 0:
                    b1_is_empty = False
                    break

            b2_is_empty = True
            for column in [4, 5, 6, 7]:
                if seat_list[column - 1] != 0:
                    b2_is_empty = False
                    break

            b3_is_empty = True
            for column in [6, 7, 8, 9]:
                if seat_list[column - 1] != 0:
                    b3_is_empty = False
                    break

            if b1_is_empty:
                output += 1
            if b3_is_empty:
                output += 1
            if not b1_is_empty and not b3_is_empty and b2_is_empty:
                output += 1

        return output
