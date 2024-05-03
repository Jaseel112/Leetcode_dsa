class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        t=len(needle)
        for i in range(len(haystack)-t+1):
            if needle==haystack[i:t+i]:
                return i
        return -1
        # return haystack.find(needle)