class Solution:
    def countAndSay(self, n: int) -> str:
        say='1'
        for _ in range(2,n+1):
            num=say[0]
            temp=''
            count=1
            for i in range(1,len(say)):
                curr=say[i]
                if curr==num:
                    count+=1
                else:
                    temp+=str(count)+str(num)
                    num=curr
                    count=1
            temp+=str(count)+str(num)
            say=temp
        return say