class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        if numRows==0:
            return output
        for i in range(numRows):
            if i==0:
                prev=[1]
                output.append(prev)
            else:
                j=1
                curr=[1]
                while j<i:
                    curr.append(prev[j-1]+prev[j])
                    j+=1
                curr.append(1)
                prev=curr
                output.append(curr)
        return output