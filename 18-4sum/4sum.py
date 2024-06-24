class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)==4:
            if nums[0]+nums[1]+nums[2]+nums[3]==target:
                return [[nums[0],nums[1],nums[2],nums[3]]]
            else:
                return []
        res=[]
        i=0
        l=r=len(nums)-1
        nums.sort()
        while i<=r-3:
            j=i+1
            while j!=l:
                k=j+1
                l=r
                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s>target:
                        l-=1
                    elif s<target:
                        k+=1
                    elif target==s:
                        if [nums[i],nums[j],nums[k],nums[l]] not in res:
                            res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        while nums[k]==nums[k-1] and k<l:
                            k+=1
                j+=1
            i+=1
        return res

