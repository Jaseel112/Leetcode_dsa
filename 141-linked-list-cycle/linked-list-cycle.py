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

        # hare=head
        # tort=head

        # while hare and hare.next:
        #     tort=tort.next if tort else None
        #     hare=hare.next.next if hare and hare.next else None
        #     if hare==tort:
        #         return True
        # return False