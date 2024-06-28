class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c,m,M,res=Counter(nums),min(nums),max(nums),[]
        for i in range(m,M+1):
            res.extend([i]*c[i])
        return res