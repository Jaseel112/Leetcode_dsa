class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        while i>0:
            curr=nums[i]
            foll=nums[i-1]
            if foll<curr:
                nums[i:]=nums[len(nums)-1:i-1:-1]
                k=i
                while nums[k]<=foll:
                    k+=1
                nums[k],nums[i-1]=nums[i-1],nums[k]
                return
            i-=1
        nums.sort()