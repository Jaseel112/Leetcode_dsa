class Solution:
    def findLHS(self, nums: List[int]) -> int:
        map=Counter(nums)
        ln=0
        for i,count in map.items():
            if i+1 in map:
                ln=max(ln,count+map[i+1])
        return ln