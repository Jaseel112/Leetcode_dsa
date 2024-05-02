class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hasht={}
        for i in range(len(nums)):
            if nums[i] in hasht:
                for j in hasht[nums[i]]:
                    if abs(i-j)<=k:
                        return True
                hasht[nums[i]].append(i)
            else:
                hasht[nums[i]]=[i]
        print(hasht)
        return False