class Solution:
    def numDecodings(self, s: str) -> int:
        # dp={}
        # if s[0]=="0":
        #     return 0
        # if len(s)==1:
        #     return 1
        # def f(i):
        #     if i>=len(s):
        #         return 1
        #     if s[i]=='0':
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     take=f(i+1)
        #     not_take=0
        #     if i+1<=len(s)-1 and int(s[i:i+2])<27:
        #         not_take=f(i+2)
        #     dp[i]=take+not_take
        #     return dp[i]
        
        # return f(0)
        if s[0]=='0':
            return 0
        n=len(s)
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[-1]=1
        for i in range(n-1,-1,-1):
            if s[i]!='0':
                if i==n-1:
                    dp[i]=dp[i+1]
                else:
                    if int(s[i:i+2])<27:
                        dp[i]=dp[i+1]+dp[i+2]
                    else:
                        dp[i]=dp[i+1]
        return dp[0]
            

                
            