class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
    
        nums = sorted(nums)

        missing =[]

        smallest = nums[0]
        biggest = nums[-1]

        index_nums=0

        for index_all in range(smallest, biggest+1):
            if index_all == nums[index_nums]:
                index_nums +=1
            else:
                missing.append(index_all)

        return missing
