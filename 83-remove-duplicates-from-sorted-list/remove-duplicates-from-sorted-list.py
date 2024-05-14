# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        map=[]
        temp=head
        prev=head
        while temp:
            if temp.val not in map:
                map.append(temp.val)
                prev=temp
            elif temp.val in map:
                prev.next=temp.next
            temp=temp.next

        return head