class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find=nums.copy()
        # find.sort()
        # n=nums[0]
        # low=0
        # high=len(find)-1
        # k=0
        # while(low<=high):
        #     mid=(low+high)//2
        #     if find[mid]==n:
        #         k=mid
        #         break
        #     elif find[mid]>n:
        #         high=mid-1
        #     else:
        #         low=mid+1
        # if target>=nums[0]:
        #     low=0
        #     high=len(nums)-k-1
        # if target<nums[0]:
        #     low=len(nums)-k
        #     high=len(nums)-1
        # while(low<=high):
        #     mid=(low+high)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]>target:
        #         high=mid-1
        #     else:
        #         low=mid+1
        # return -1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1

