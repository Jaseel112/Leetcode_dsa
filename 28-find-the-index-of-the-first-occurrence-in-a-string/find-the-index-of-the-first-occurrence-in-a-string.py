class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        t=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:t+i]:
                return i
        return -1