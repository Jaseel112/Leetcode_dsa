class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s=set(nums)
        ln=0
        for i in s:
            if i+1 in s:
                ln=max(ln,(nums.count(i)+nums.count(i+1)))
        return ln