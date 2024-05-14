class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        c=Counter(nums)
        return c.most_common(n)[-1][0]