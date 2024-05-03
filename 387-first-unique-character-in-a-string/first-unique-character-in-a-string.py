class Solution:
    def firstUniqChar(self, s: str) -> int:
        t=list(s)
        l=len(s)
        i=0
        index=0
        while index<l:
            k=t.pop(i)
            if k not in t:
                return index
            index+=1
            t.append(k)   
        return -1