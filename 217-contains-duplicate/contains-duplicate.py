class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist=set()
        for i in nums:
            if i in dist:
                return True
            dist.add(i)
        return False
        