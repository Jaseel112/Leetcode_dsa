class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        if n==0:
            return True
        j=0
        for i in t:
            if i==s[j]:
                j+=1
            if j==n:
                break
        if j<n:
            return False
        else:
            return True