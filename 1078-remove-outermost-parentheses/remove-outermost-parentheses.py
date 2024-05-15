class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened=0
        o=''
        for i in s:
            if i=='(':
                opened+=1
                if opened>1:
                    o+=i
            else:
                opened-=1
                if opened>0:
                    o+=i
        return o
