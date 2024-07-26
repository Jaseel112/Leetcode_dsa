class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap={}
        def backtrack(steps):
            if steps in hashmap:
                return hashmap[steps]
            if steps==0:
                return 1
            if steps<0:
                return 0
            hashmap[steps]= backtrack(steps-1)+backtrack(steps-2)
            return hashmap[steps]
        
        return backtrack(n)















