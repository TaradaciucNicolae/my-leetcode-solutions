int minMoves(int* nums, int numsSize) {

    int max = 0, moves = 0;

    for(int i =0 ; i< numsSize; i++)
    {
        if(nums[i] > max)
        {
            max = nums[i];
        }
    }

    for (int i = 0; i < numsSize; i++)
    {
        moves = moves + (max - nums[i]);
    }
    
    return moves;
}
