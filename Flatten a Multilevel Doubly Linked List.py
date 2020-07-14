"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
#https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/728346/Without-and-With-Stack-or-Two-Solution-or-Detailed-Explanation-with-example-dry-run

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        result = self.processLevel(head)
        return head
    
    def processLevel(self, head):
        headP = head
        while(headP != None and headP.val != None):
            if (headP.child != None):
                restP = self.insert(headP,headP.child)

                headP.next = restP.next
                headP.next.prev = headP
             
                return head
            headP = headP.next

        return head

    def insert(self, head, nextLevel):
        headP = head
        head.child = None
        nextP = nextLevel


        nextLevelHead = self.processLevel(nextP)


        endofNextLevel = nextLevelHead
        
        
        while(endofNextLevel.next != None):
            endofNextLevel = endofNextLevel.next
        if headP.next:
            endofNextLevel.next =  headP.next
            endofNextLevel.next.prev =endofNextLevel
        
        headP.next = nextLevelHead
        headP.next.prev = headP

        

        return head