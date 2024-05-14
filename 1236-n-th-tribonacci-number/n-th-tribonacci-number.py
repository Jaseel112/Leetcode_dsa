class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        prev1=0
        prev2=1
        prev3=1
        for i in range(2,n):
            curr=prev1+prev2+prev3
            prev1=prev2
            prev2=prev3
            prev3=curr
        return curr