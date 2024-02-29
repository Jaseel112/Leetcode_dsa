class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash={}
        k=0
        for i in range (len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=0
        for i in range (len(nums)):
            if nums[i] in hash and hash[nums[i]]==0:
                hash[nums[i]]=1
                nums[k]=nums[i]
                k+=1
        return k