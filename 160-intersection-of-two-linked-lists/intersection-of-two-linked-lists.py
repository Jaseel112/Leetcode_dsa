# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1=set()
        curr=headA
        while curr:
            list1.add(curr)
            curr=curr.next
        curr=headB
        while curr:
            if curr in list1:
                print(curr)
                return curr
            curr=curr.next
        return None