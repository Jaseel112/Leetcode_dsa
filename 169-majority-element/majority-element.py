class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        k1=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=nums[i-1]:
                k1=1
            else:
                k1+=1
                if k1>=n/2:
                    return nums[i]