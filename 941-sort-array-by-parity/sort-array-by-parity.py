class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p=list(filter(lambda x:x%2==0,nums))
        n=list(filter(lambda x:x%2!=0,nums))
        print(p)
        nums1=[]
        for i in p:
            nums1.append(i)
        for i in n:
            nums1.append(i)
        return nums1