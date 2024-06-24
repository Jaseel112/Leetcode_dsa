class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if (dividend>=0 and divisor<0) or (dividend<0 and divisor>=0) else 1
        a=abs(dividend)
        b=abs(divisor)
        result=len(range(0,a-b+1,b))
        result=result*sign
        plusm=2**31-1
        minusm=-2**31
        return min(max(result,minusm),plusm)
                    


            
