# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l3=ListNode()
        rem=0
        while(l1!=None or l2!=None or rem!=0):
            num1=l1.val if l1 is not None else 0
            num2=l2.val if l2 is not None else 0
            tot=num1+num2+rem
            num=tot%10
            rem=tot//10
            l3.val=num
            l1=l1.next if l1 is not None else None
            l2=l2.next if l2 is not None else None
            if l1!=None or l2!=None or rem!=0:
                l3.next=ListNode()
                l3=l3.next
        return head
        