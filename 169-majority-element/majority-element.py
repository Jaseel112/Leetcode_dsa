class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        x=Counter(nums)
        for i in nums:
            if x[i]>n/2:
                return i
