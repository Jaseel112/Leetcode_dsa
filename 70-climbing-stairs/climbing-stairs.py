class Solution:
    def climbStairs(self, n: int) -> int:

        # #memoisation technique
        # hashmap={}
        # def backtrack(steps):
        #     if steps in hashmap:
        #         return hashmap[steps]
        #     if steps==0:
        #         return 1
        #     if steps<0:
        #         return 0
        #     hashmap[steps]= backtrack(steps-1)+backtrack(steps-2)
        #     return hashmap[steps]
        
        # return backtrack(n)

        #more optimized code (fibanocci sequence)

        s=[0,1]

        for i in range(1,n+1):
            s.append(s[i-1]+s[i])
        return s[-1]

















