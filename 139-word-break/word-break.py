class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s=0
        # for i in wordDict:
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
            
            
            

            