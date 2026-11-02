#include <stdlib.h>

// sort integers in ascending order.
int compare(const void *a, const void *b)
{
    // 'a' and 'b' are generic pointers (void pointers).
    // We first cast them to pointers to integers (const int *).
    // Then, we dereference them (*) to get the actual values.

    int x = *(const int *)a;
    int y = *(const int *)b;

    // Return a negative value if x < y.
    // Return zero if x == y.
    // Return a positive value if x > y.

    return (x > y) - (x < y);
}

int minMoves2(int* nums, int numsSize)
{
    int mid = 0;
    int sum = 0;

    // Sort the array in ascending order.
    //
    // nums       -> pointer to the first element
    // numsSize   -> number of elements
    // sizeof(int)-> size of one element in bytes
    // compare    -> function used to compare two elements

    qsort(nums, numsSize, sizeof(int), compare);

    // Find the median of the sorted array.
    // Integer division gives the middle index.

    mid = nums[numsSize / 2];

    for (int i = 0; i < numsSize; i++)
    {
        sum += abs(nums[i] - mid);
    }

    return sum;
}
