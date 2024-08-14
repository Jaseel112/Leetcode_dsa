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
        i=0
        j=0
        start=head
        end=head.next
        while end!=None:
            j+=1
            end=end.next
        n=j
        while start.next:
            end=start
            prev=None
            while end.next:
                prev=end
                end=end.next 
            if j-i<=1:
                break           
            end.next=start.next
            start.next=end  
            prev.next=None   
            start=end.next          
            i+=1
            j-=1   
        return head