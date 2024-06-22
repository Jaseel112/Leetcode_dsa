class Solution:
    def myAtoi(self, s: str) -> int:
        z=True
        k=''
        for i in s:
            if i==' ' and len(k)==0:
                continue
            elif (i in '+-' or i.isnumeric()) and len(k)==0:
                k+=i
            elif i.isnumeric():
                k+=i
            else:
                break
        if k=='' or k in '-+':
            return 0
        if int(k)>2**31-1:
            return 2**31-1
        if int(k)<-2**31:
            return -2**31
        return int(k)