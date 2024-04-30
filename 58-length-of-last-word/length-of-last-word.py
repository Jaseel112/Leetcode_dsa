class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)-1
        i=0
        while s[n]==' ':
            n-=1
        while s[n]!=' ' and n>=0:
            i+=1
            n-=1
        return i
        