class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        diffl=[]
        for i in range(1,len(arr)):
            diffl.append(arr[i]-arr[i-1])
        diff=min(diffl)
        out=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==diff:
                out.append([arr[i-1],arr[i]])
        return out