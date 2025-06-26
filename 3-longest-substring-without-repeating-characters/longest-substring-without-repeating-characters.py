class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset=set()
        left=0
        maxl=0
        for i in range(len(s)):
            if s[i] not in cset:
                cset.add(s[i])
                maxl=max(maxl,len(cset))
            else:
                while s[i] in cset:
                    cset.remove(s[left])
                    left+=1
                cset.add(s[i])
        return maxl
