class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nume=list(filter(lambda x:x%2==0,nums))
        numo=list(filter(lambda x:x%2!=0,nums))
        num=[]
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0:
                num.append(nume[j])
                j+=1
            else:
                num.append(numo[k])
                k+=1
        return num