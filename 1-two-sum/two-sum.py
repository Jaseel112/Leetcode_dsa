class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range (len(nums)):
            hash[nums[i]]=i
        for i in range (len(nums)-1):
            diff=target-nums[i]
            if diff in hash and hash[diff]!=i:
                return [i,hash[diff]]
        