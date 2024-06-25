# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        head2=ListNode(0,head.next)
        temp=head
        prev=None
        nx=None
        while temp and temp.next:
            nx=temp.next
            nx.next,temp.next=temp,nx.next
            if prev:
                prev.next=nx
            prev=temp
            temp=temp.next
        return head2.next