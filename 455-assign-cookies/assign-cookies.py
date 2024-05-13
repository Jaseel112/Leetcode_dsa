class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        j=0
        for i in range(len(s)):
            if j<len(g):
                if s[i]>=g[j]:
                    j+=1          
        return j