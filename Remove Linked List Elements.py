# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0,head)
        p = dummy 
        while p != None and p.next != None:
            if p.next.val == val:
                p.next = p.next.next
                continue

            p = p.next
        return dummy.next