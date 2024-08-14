# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # i=0
        # j=0
        # start=head
        # end=head.next
        # while end!=None:
        #     j+=1
        #     end=end.next
        # while start.next:
        #     end=start.next
        #     prev=start
        #     while end.next:
        #         prev=end
        #         end=end.next 
        #     if j-i<=1:
        #         break           
        #     end.next=start.next
        #     start.next=end  
        #     prev.next=None   
        #     start=end.next          
        #     i+=1
        #     j-=1   
        # return head

        if not head: return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next