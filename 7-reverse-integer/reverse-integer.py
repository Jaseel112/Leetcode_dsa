class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if s[0]=='-':
            k=s[0]
            k+=s[::-1]
            s=k[:len(k)-1]
        else:
            s=s[::-1]
        x=int(s)
        if x<-2147483647 or x>2147483647:
            return 0
        else:
            return x