class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # out=[]
        # for i in arr2:
        #     while i in arr1:
        #         arr1.remove(i)
        #         out.append(i)
        # out+=sorted(arr1)
        # return out
        c=Counter(arr1)
        out=[]
        for i in arr2:
            out+=[i]*c.pop(i)
        out+=sorted(c.elements())
        return out