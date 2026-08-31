# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:


        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        n = len(values)
        
        crit_points_index = []
        
        for i in range(1, n - 1):
            prev_val = values[i - 1]
            curr_val = values[i]
            next_val = values[i + 1]
            
            is_local_max = curr_val > prev_val and curr_val > next_val
            is_local_min = curr_val < prev_val and curr_val < next_val
            
            if is_local_max or is_local_min:
                crit_points_index.append(i)
        

        if len(crit_points_index) < 2:
            return [-1, -1]

        max_dist = crit_points_index[-1] - crit_points_index[0]

        min_dist = float('inf')
        for i in range(1, len(crit_points_index)):
            min_dist = min(min_dist, crit_points_index[i] - crit_points_index[i - 1])

        return [min_dist, max_dist]
