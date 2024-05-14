class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        prev1=1
        prev2=1
        curr=0
        for i in range(2,n):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr
        return curr

