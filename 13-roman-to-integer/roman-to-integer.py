class Solution:
    def romanToInt(self, s: str) -> int:
        mydict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        for i in range(len(s)-1):
            if s[i] in mydict:
                if mydict[s[i]]>=mydict[s[i+1]]:
                    num+=mydict[s[i]]
                else:
                    num-=mydict[s[i]]
        num+=mydict[s[len(s)-1]]
        return num
                