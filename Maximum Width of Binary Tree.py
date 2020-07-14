# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/728346/Without-and-With-Stack-or-Two-Solution-or-Detailed-Explanation-with-example-dry-run
class nodeLevel:
    def __init__(self,levelNum,start):
        self.num=levelNum
        self.start = start
        self.end = start
        self.len = 1

    def setEnd(self,end):
        self.end = end
        self.len = end-self.start+1

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        #brute, travese, have levels, and counter for each level, get the highest level
        #level search, and update th emax value as finsih each level
        #goes down to the botton
        
        # edge case, 
        self.levels=[] 
        self.levelTraverse(0,root,0)
        self.levels.sort(key=lambda x:x.len,reverse=True)

        return self.levels[0].len

    def levelTraverse(self,levelNum,node,position):
        if node != None:
            self.updateLevel(levelNum,position)

            self.levelTraverse(levelNum+1,node.left,position*2)
            self.levelTraverse(levelNum+1,node.right,position*2+1)

    def updateLevel(self,levelNum,position):
        if len(self.levels)<=levelNum:
            self.levels.append(nodeLevel(levelNum,position))
        else:
            self.levels[levelNum].setEnd(position)