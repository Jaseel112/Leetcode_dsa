class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True
        if n<10:
            return False
        seen=set()
        while n!=1:
            n=sum(int(i)**2 for i in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True  
