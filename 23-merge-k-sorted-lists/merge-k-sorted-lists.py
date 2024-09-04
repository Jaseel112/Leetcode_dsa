# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mp={}
        for x in lists:
            if x is not None:
                mp[x.val]=mp.get(x.val,[])+[x]
        dummy=ListNode(-1)
        temp=dummy
        while mp:
            small=mp[min(mp.keys())][-1]
            nxt=small.next
            temp.next=small
            mp[small.val].pop(-1)
            if nxt is not None:
                mp[nxt.val]=mp.get(nxt.val,[])+[nxt]
            if mp[small.val]==[]:
                mp.pop(small.val)
            temp=small
        return dummy.next

            