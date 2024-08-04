class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        res=0
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                res=max(res,count)
                count=1
        res=max(res,count)
        return res
                
