class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        map1={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def result(i,comb):
            if i==len(digits):
                res.append(comb)
                return
            for item in map1[digits[i]]:
                result(i+1,comb+item)
        res=[]
        result(0,"")
        return res

