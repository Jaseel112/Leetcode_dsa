class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap={}
        def bfs(steps):
            if steps in hashmap:
                return hashmap[steps]
            if steps==0:
                return 1
            if steps<0:
                return 0
            hashmap[steps]=bfs(steps-1) + bfs(steps-2)
            return hashmap[steps]
        return bfs(n)















