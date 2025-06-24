class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mp={}
        # for i in range(len(nums)):
        #     mp[nums[i]]=i
        # for i in range(len(nums)):
        #     if target-nums[i] in mp and mp[target-nums[i]]!=i:
        #         return [i,mp[target-nums[i]]]
        
        dic={}
        result=[]
        for i in range(len(nums)):
            dic[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in dic and dic[target-nums[i]]!=i:
                return [i,dic[target-nums[i]]]