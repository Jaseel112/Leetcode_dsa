class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       #memoization

        lst=[1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    lst[i]=max(lst[j]+1,lst[i])
        return max(lst)

        # #dfs with cache

        # def f()