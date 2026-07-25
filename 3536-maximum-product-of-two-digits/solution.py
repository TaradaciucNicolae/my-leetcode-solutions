class Solution:
    def maxProduct(self, n: int) -> int:
        
        max_pair = 0

        for i, each_1 in enumerate(str(n)):

            val_1 = int(each_1)

            for j, each_2 in enumerate(str(n)):

                val_2 = int(each_2)

                if i != j:
                    max_pair = max(max_pair, val_1 * val_2)

        
        return max_pair
