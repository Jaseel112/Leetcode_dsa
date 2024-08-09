class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(i,j):
            count=0
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                # print(s[i:j+1])
                i-=1
                j+=1
            return count
        odd=even=0
        for i in range(len(s)):
            odd+=check(i,i)
            even+=check(i,i+1)
        return odd+even