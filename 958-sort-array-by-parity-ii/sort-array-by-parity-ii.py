class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # nume=list(filter(lambda x:x%2==0,nums))
        # numo=list(filter(lambda x:x%2!=0,nums))
        # num=[]
        # for i in range(len(nume)):
        #     num.append(nume[i])
        #     num.append(numo[i])
        # return num
        j=0
        k=1
        num=[0]*len(nums)
        for i in nums:
            if i%2==0:
                num[j]=i
                j+=2
            else:
                num[k]=i
                k+=2
        return num