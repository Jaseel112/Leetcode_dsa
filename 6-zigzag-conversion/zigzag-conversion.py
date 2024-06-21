class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        r=[""]*numRows
        row=0
        inc=1
        for i in s:
            r[row]+=i
            if row==0:
                inc=1
            elif row==numRows-1:
                inc =-1
            row+=inc
        return "".join(r)

        
