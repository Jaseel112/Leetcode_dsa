class Solution:
    def rob(self, nums: List[int]) -> int:
        # length=0
        # dp={}
        # def f(i):
        #     if i>=len(nums):
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     dp[i]=nums[i]+f(i+2)
        #     return dp[i]
        # for i in range(len(nums)):
        #     len1=nums[i]+f(i+2)
        #     length=max(length,len1)
        # return length



        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]
