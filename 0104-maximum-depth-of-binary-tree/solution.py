# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        q=deque()
        q.append(root)

        max_level=0

        while q:

            level=[]

            for _ in range(len(q)):

                node = q.popleft()
                level.append(node.val)
    
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            max_level +=1
        
        return max_level
