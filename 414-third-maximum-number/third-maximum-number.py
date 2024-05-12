class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=sorted(nums,reverse=True)
        print(s)
        max=maxi=s[0]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                max=s[i]
                break
        for i in range(len(s)):
            if s[i]<max:
                return s[i]
        return maxi

