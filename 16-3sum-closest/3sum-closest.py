class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        j=1
        r=k=len(nums)-1
        res=nums[0]+nums[1]+nums[k]
        while i!=k:
            j=i+1
            k=r
            while(j<k):
                s=nums[i]+nums[j]+nums[k]
                if s==target:
                    return s
                if abs(target-s)<abs(target-res):
                    res=s
                if s<target:
                    j+=1
                else:
                    k-=1
            i+=1
        return res
        