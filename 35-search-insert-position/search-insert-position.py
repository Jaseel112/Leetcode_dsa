class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=0
        for i in nums:
            if target<=i:
                return k
            k+=1
        return k
            