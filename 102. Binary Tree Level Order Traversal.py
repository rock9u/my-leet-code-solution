# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = {}
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.doLevelOrder(root,0)
        return self.result.values()

    def doLevelOrder(self,node,level):
        if node == None:
            return
        self.result[level] = self.result.get(level,[]) +[node.val]
        self.doLevelOrder(node.left,level+1)
        self.doLevelOrder(node.right,level+1)
        return