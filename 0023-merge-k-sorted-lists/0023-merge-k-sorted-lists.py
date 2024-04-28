# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        dummy = ListNode(None)
        curr = dummy
        for idx, node in enumerate(lists):
            if node:
                q.put((node.val, idx, node))
        while q.qsize():
            _, idx, curr.next = q.get()
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, idx, curr.next))
        return dummy.next