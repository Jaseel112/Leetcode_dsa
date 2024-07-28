class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # @cache
        # def f(index):
        #     if index>=len(nums)-1:
        #         return True           
        #     fl=False
        #     for i in range(1,nums[index]+1):
        #          fl=fl or f(index+i)
        #          if fl==True:
        #             break
        #     return fl
        # return f(0)

        goal=len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return goal==0