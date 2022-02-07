# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        maxN = float('inf')
        minN = float('-inf')
        # print(maxN,minN)
        return self.validate(root,minN,maxN)


    def validate(self,node, lowerBound,upperBound):
        if node == None:
            return True
        # print(node.val, lowerBound,upperBound)
        if (node.val > lowerBound and node.val < upperBound):
            return self.validate(node.left, lowerBound,node.val) and \
                self.validate(node.right, node.val,upperBound)

        else:
            return False