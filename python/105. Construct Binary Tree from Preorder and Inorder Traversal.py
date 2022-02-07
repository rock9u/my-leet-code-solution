# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ''' 
        get root: root is first preorder
        find next in the left side of inorder
            next node is right after this root, unless nothing in the right side of in order
        find next next in right side of inorder
            next next node at right side
        loop get root
        ''' 

        if not (preorder and inorder):
            return 

        root = TreeNode(preorder.pop(0))
        rootInOrderIndex = inorder.index(root.val)

        root.left = self.buildTree(preorder,inorder[:rootInOrderIndex])
        root.right = self.buildTree(preorder,inorder[rootInOrderIndex+1:])

        return root