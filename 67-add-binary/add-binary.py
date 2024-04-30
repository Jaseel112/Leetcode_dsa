class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m=len(a)-1
        n=len(b)-1
        def binarytoint(k,s):
            l=0
            n1=0
            t=0
            while k>=0:
                t=int(s[k])*(2**l)
                l+=1
                k-=1
                n1+=t
            return n1
        a1=binarytoint(m,a)
        b1=binarytoint(n,b)
        print(a1+b1)
        sum=bin(a1+b1)[2:]
        return sum