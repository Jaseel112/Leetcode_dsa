# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        temp=head
        while temp:
            i+=1
            temp=temp.next
        temp=head
        if i%2==0:
            k=(i/2)+1
        else:
            k=(i+1)/2
        i=1
        while temp:
            if i==k:
                return temp
            i+=1
            temp=temp.next