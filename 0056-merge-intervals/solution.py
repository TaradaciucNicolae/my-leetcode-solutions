class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        #print(intervals)
        

        while intervals:

            if merged == []:
                interval_extras = intervals.pop(0)
                merged.append(interval_extras)
                print(merged[0][1])
            else:
            

                interval_extras = intervals.pop(0)

                # apoi verifica ultimul din merged cu cel extras daca fac overlap, daca fac overlap, il scoatem pe cel din merged, il adaugam pe cel din functie,
                # iar daca  nu fac overlap, nu mai scoatem nimic si doar il adaugam pe celalat
                bool_Overlap, interval_de_adaugat = self.overlap(merged[-1], interval_extras)
            
                if bool_Overlap == True:
                    merged.pop()
                    merged.append(interval_de_adaugat)
                else:
                    merged.append(interval_de_adaugat)

        return merged

    
    def overlap(self, interval1, interval2):
        
        #prima data verificam care e intervalul mai mic
        if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
            interval_overlap = [interval1[0],max(interval2[1], interval1[1])]
            bool_Overlap = True
        else:
            interval_overlap = interval2
            bool_Overlap = False



        return bool_Overlap, interval_overlap # sau intervalul 2
