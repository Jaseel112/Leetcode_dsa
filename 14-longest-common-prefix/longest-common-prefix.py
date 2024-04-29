class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        string=sorted(strs)
        start=string[0]
        end=string[-1]
        for i in  range(min(len(start),len(end))):
            if start[i]!=end[i]:
                return prefix
            prefix+=start[i]
        return prefix