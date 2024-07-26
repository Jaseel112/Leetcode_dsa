class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def bfs(steps):
            if steps==0:
                return 1
            if steps<0:
                return 0
            
            return bfs(steps-1) + bfs(steps-2)
        return bfs(n)















