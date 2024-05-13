class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k=max(nums)
        for i in range(len(nums)):
            if nums[i]==k:
                index=i
            if nums[i]!=k and nums[i]*2>k:
                return -1
        return index