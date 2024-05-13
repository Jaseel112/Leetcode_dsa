class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num=list(x*x for x in nums)
        num.sort()
        return num