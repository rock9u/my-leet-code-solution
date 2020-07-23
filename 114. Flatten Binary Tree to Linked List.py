# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        for root

            if left new Left = flatten(left)
            if right: flatten(right)
            inject left infront of right
            concate()
            
                1
               / \
              2   5
             / \   \
            3   4   6
            -----------        
            pre = 5
            cur = 4

                1
               / 
              2   
             / \   
            3   4
                 \
                  5
                   \
                    6
            -----------        
            pre = 4
            cur = 3

                1
               / 
              2   
             /   
            3 
             \
              4
               \
                5
                 \
                  6
            -----------        
            cur = 2
            pre = 3

                1
               / 
              2   
               \
                3 
                 \
                  4
                   \
                    5
                     \
                      6
            -----------        
            cur = 1
            pre = 2

            1
             \
              2
               \
                3
                 \
                  4
                   \
                    5
                     \
                      6
        '''
        if root == None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root