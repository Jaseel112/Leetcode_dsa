class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s1=sorted(s)
        g1=sorted(g)
        j=0
        for i in range(len(s1)):
            if j<len(g1):
                if s1[i]>=g1[j]:
                    j+=1          
        return j