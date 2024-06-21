class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res=0
        curr=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                res+=customers[i]
        for i in range(minutes):
            if grumpy[i]==1:
                curr+=customers[i]
        addi=curr
        for i in range(minutes,len(customers)):
            if grumpy[i-minutes]==1:
                curr-=customers[i-minutes]
            if grumpy[i]==1:
                curr+=customers[i]
            addi=max(curr,addi)
        return res+addi

