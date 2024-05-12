class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s1=sorted(s)
        # t1=sorted(t)
        # n=len(s)
        # for i in range (n):
        #     if s1[i]!=t1[i]:
        #         return t1[i]
        # return t1[n]
        s1=Counter(s)
        t1=Counter(t)
        return list((t1-s1).elements())[0]