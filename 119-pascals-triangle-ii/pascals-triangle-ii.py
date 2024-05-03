class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        if n==0:
            return [1]
        if n==1:
            return [1,1]
        else:
            prev=[1,1]
            for i in range(2,n+1):
                curr=[1]
                j=1
                while j<i:
                    curr.append(prev[j-1]+prev[j])
                    j+=1
                curr.append(1)
                if i==n:
                    return curr
                prev=curr