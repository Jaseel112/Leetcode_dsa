class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        if s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        def f(i):
            if i>=len(s):
                return 1
            if s[i]=='0':
                return 0
            if i in dp:
                return dp[i]
            take=f(i+1)
            not_take=0
            if i+1<=len(s)-1 and int(s[i:i+2])<27:
                not_take=f(i+2)
            dp[i]=take+not_take
            return dp[i]
        
        return f(0)
                
            