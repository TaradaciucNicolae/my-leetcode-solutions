# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        self.matching_nodes = 0

        def dfs(node):

            if node is None:
                return 0,0
            
            # Get info
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            # Current node
            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count +1

            if node.val == subtree_sum // subtree_count:
                self.matching_nodes += 1
        
            return subtree_sum, subtree_count
        
        dfs(root)
        return self.matching_nodes
