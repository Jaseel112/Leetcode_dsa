class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left=right=1
        res=nums[0]
        l=0
        r=len(nums)-1
        while l<len(nums):
            left*=nums[l]
            right*=nums[r]
            res=max(left,right,res)
            if left==0:
                left=1
            if right==0:
                right=1
            l+=1
            r-=1
        return res
