# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp=head
        prev=head
        if head==None:
            return head
        while temp:
            if temp.val==val:
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
        if head.val==val:
            head=head.next
        return head