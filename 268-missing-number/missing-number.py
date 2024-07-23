class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # x=Counter(nums)
        # n=len(nums)
        # s1=(n*(n+1))/2
        # s2=sum(key for key in x)
        # return int(s1-s2)
        n=len(nums)
        s1=(n*(n+1))//2
        s2=sum(nums)
        return int(s1-s2)