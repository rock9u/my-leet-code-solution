# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# more efficient as list.pop() is actually O(n)
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.levelOrder(deque([root]))
        return self.result
    
    def levelOrder(self, thisRowStack,isToRight=True):
        if len(thisRowStack) == 0 :
            return
        newRowStack = deque([])
        thisRowDisplay = []

        # print("entering levelOrder")
        while len(thisRowStack) > 0:
            node = thisRowStack.pop()
            if node:
                thisRowDisplay.append(node.val)
                if isToRight:
                    newRowStack.append(node.left)
                    newRowStack.append(node.right)
                else:
                    newRowStack.append(node.right)
                    newRowStack.append(node.left)
        if thisRowDisplay != []:
            self.result.append(thisRowDisplay)
        return self.levelOrder(newRowStack,not isToRight)