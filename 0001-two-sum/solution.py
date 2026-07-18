class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for index_nr1, nr1 in enumerate(nums):
        #     for index_nr2, nr2 in enumerate(nums):
        #         if index_nr1 != index_nr2 and nr1+nr2==target:
        #             return [index_nr1 , index_nr2]
                        
                

        # Varianta mai buna

        map_of_num_positions = {}

        for i, num in enumerate(nums):

            celalalt_numar = target - num # practic e un fel de, ce numar imi lipseste sa ajung la target
            print("celalalt: ", celalalt_numar)

            if celalalt_numar in map_of_num_positions:
                return [map_of_num_positions[celalalt_numar], i]
            

            # iar daca nu e, il adaugam
            map_of_num_positions[num] = i
