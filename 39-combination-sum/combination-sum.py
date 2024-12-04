class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def check(start,path,target):
            if target==0:
                res.append(path)
                return
            for i in range(start,len(candidates)):
                if target-candidates[i]>=0:
                    check(i,path+[candidates[i]],target-candidates[i])
        res=[]
        check(0,[],target)
        return res












        
        def f(sum1,comb,j):
            if sum1==0:
                dp.append(comb)
                return
            for i in range(j,len(candidates)):
                if sum1-candidates[i]>=0:
                    f(sum1-candidates[i],comb+[candidates[i]],i)
        dp=[]
        f(target,[],0)
        return dp
