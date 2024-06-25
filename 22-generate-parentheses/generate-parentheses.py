class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(left,right,s):
            if len(s)==n*2:
                res.append(s)
                return
            if left<n:
                generate(left+1,right,s+'(')
            if right<left:
                generate(left,right+1,s+')')
        res=[]
        generate(0,0,'')
        return res