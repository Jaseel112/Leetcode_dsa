class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        def convert(s:str):
            num=0
            p=0
            d={
                '0':0,
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9
            }
            for i in s:
                pr=d[i]*(10**p)
                p+=1
                num+=pr
            return num
        n1=convert(num1)
        n2=convert(num2)
        n3=n1*n2
        d={
                0:'0',
                1:'1',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'6',
                7:'7',
                8:'8',
                9:'9'
            }
        rem=0
        res=''
        if n3==0:
            return '0'
        while n3!=0:
            rem=n3%10
            res+=d[rem]
            n3=n3//10
        return res[::-1]