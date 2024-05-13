class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # for i in range(k):
        #     nums.sort()
        #     nums[0]=-nums[0]
        # return sum(nums)
        nums=sorted(nums)
        for i in range(len(nums)):
            if k>0 and nums[i]<0:
                nums[i]=-nums[i]
                k-=1
        nums=sorted(nums)
        if k>0 and k%2!=0:
            nums[0]=-nums[0]
        return sum(nums)