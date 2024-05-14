# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map={}
        temp=head
        while temp:
            if temp not in map:
                map[temp]=1
            elif temp in map:
                return True
            temp=temp.next
        return False