class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        groups = set()
        for i, val_1 in enumerate(digits):
            for j, val_2 in enumerate(digits):
                for k, val_3 in enumerate(digits):
                    if (i != j and j != k and i != k   and val_1 != 0   and val_3 % 2 == 0):
                        groups.add((val_1, val_2, val_3))

        return len(groups)
