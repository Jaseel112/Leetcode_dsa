# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return True
        temp=head
        stack=[]
        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        i=len(stack)-1
        while temp:
            if temp.val!=stack[i]:
                return False
            temp=temp.next
            i-=1
        return True