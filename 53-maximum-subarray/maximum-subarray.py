class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        su=nums[0]
        for i in range(len(nums)):
            s+=nums[i]
            su=max(su,s)
            if s<0:
                s=0
        return su