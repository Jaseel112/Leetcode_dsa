class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=len(digits)-1
        n=0
        for i in range (len(digits)-1):
            l=digits[i]*10**k
            k-=1
            n+=l
        n+=digits[k-1]
        n+=1
        mylist=[n]
        digits= list(map(int, str(mylist[0])))
        return digits
        
        
      
