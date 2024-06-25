class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def binary(nums,target,flag):
            low=0
            high=len(nums)-1
            idx=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    idx=mid
                    if flag:
                        high=mid-1
                    else:
                        low=mid+1
            return idx

        
        left=binary(nums,target,True)
        right=binary(nums,target,False)
        return [left,right]