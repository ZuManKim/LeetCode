# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = nodeToInsert = head
        
        while head and head.next:
            if head.val > head.next.val:
                
                nodeToInsert = head.next
                nodeToInsertPrev = dummy
                
                while nodeToInsertPrev.next.val < nodeToInsert.val:
                    nodeToInsertPrev = nodeToInsertPrev.next
                
                head.next = nodeToInsert.next
                
                nodeToInsert.next = nodeToInsertPrev.next
                nodeToInsertPrev.next = nodeToInsert
                
            else:
                head = head.next
        
        return dummy.next