class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dist=set()
        # for i in nums:
        #     if i in dist:
        #         return True
        #     dist.add(i)
        # return False
        # dist=set(nums)
        # if len(nums)!=len(dist):
        #     return True
        # return False
















        result=set(nums)
        return len(nums)!=len(result)