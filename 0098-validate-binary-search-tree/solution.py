# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float(-inf), float(inf))


    def validate(self, node, min_val, max_val):


        if node is None:
            return True
        
        if min_val >= node.val or max_val <= node.val:
            return False


        return (self.validate(node.left, min_val, node.val ) and
                self.validate(node.right, node.val, max_val)
        )





        # if root is None:
        #     return True

        # q = deque()
        # q.append((root, float("-inf"), float("inf")))

        # while q:

        #     for _ in range(len(q)):
        #         node, min_val, max_val= q.popleft()

        #         if node.val <= min_val or max_val <= node.val:
        #             return False



        #         if node.left:
        #             print("Node left:",node.left.val," si node.val:", node.val)
        #             q.append((node.left, min_val, node.val))
        #             if not node.left.val < node.val:
        #                 print("aci 1")
        #                 return False
                

        #         if node.right:
        #             q.append((node.right, node.val, max_val))
        #             print("Node right:",node.right.val," si node.val:", node.val)
        #             if not node.val < node.right.val:
        #                 print("aci 2")
        #                 return False
            
        
        # return True
