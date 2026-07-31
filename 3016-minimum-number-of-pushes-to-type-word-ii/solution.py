class Solution:
    def minimumPushes(self, word: str) -> int:


        total_cost = 0
        count_in_map = defaultdict(int)

        for each_ch in word:
            count_in_map[each_ch] +=1

        # Sorting
        freqs = sorted(count_in_map.values(), reverse = True)


        counter =0
        multiplier = 1

        for freq in freqs:

            if counter == 8:
                multiplier +=1
                counter = 0

            total_cost += freq * multiplier
            counter +=1

        return total_cost





        # total_cost = 0
        # count_in_map = defaultdict(int)

        # for each_ch in word:
        #     count_in_map[each_ch] +=1

        # # Sorting
        # count_in_map = dict(sorted(count_in_map.items(),  key=lambda item : item[1] ,reverse = True))

        # counter =0
        # multiplier = 1

        # for each_char in count_in_map:

        #     if counter == 8:
        #         multiplier +=1
        #         counter = 0

        #     total_cost += count_in_map[each_char] * multiplier

        #     counter +=1


        # return total_cost
