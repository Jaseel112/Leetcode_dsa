class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # s=0
        # # for i in wordDict:
        @cache
        def dfs(ch,i):
            if i==len(s)-1:
                if ch in wordDict:
                    return True
                else:
                    return False
            else:
                if ch in wordDict:
                    return (dfs(s[i+1],i+1) or dfs(ch+s[i+1],i+1))
                else:
                    return dfs(ch+s[i+1],i+1)
            
        return dfs(s[0],0)

        # def f(index):
        #     if index==len(s):
        #         return  True
        #     if dp[index]!=None:
        #         return dp[index]
        #     for i in wordDict:
        #         if s[index:index+len(i)]==i:
        #             if f(index+len(i)):
        #                 dp[index]=True
        #                 return True
        #     dp[index]=False
        #     return False
        # dp=[None for _ in range(len(s))]
        # return f(0)

            
            
            
            
            
            

            