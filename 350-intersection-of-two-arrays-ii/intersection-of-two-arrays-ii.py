class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # inter=[]
        # for i in nums1:
        #     if i in nums2:
        #         inter.append(i)
        #         nums2.remove(i)
        #         # r=nums2.index(i)
        #         # del nums2[r]
        # return inter
        x1=Counter(nums1)
        x2=Counter(nums2)
        return (x1&x2).elements()
