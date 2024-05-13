class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nume=list(filter(lambda x:x%2==0,nums))
        numo=list(filter(lambda x:x%2!=0,nums))
        num=[]
        for i in range(len(nume)):
            num.append(nume[i])
            num.append(numo[i])
        return num