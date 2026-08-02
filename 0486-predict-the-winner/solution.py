from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        left_border = 0
        right_border = len(nums) -1

        def maxDiff(left, right):

            # only one number left to choose from
            if left == right:
                return nums[left]


            pickLeft = nums[left] - maxDiff(left + 1, right) # if the player picks left - the advantga the other player would have

            pickRight = nums[right] - maxDiff(left, right - 1)

            return max(pickLeft, pickRight) # the player chooses the end that gives him the best advantage




        return maxDiff(left_border, right_border) >= 0 # if it's  >= 0, it means that the advantage of player 1 is >= advantage of player 2
