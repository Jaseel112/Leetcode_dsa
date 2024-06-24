# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        temp=dummy
        temp1=dummy
        for _ in range(n+1):
            temp=temp.next
        while temp!=None:
            temp=temp.next
            temp1=temp1.next
        temp1.next=temp1.next.next
        return dummy.next
        
        
