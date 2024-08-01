class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mp={}
        def f(i,j):
            if (i,j) in mp:
                return mp[(i,j)]
            if i==n-1 and j==m-1:
                return 1
            if j>=m or i>=n:
                return 0
            a=f(i,j+1)            
            b=f(i+1,j)
            mp[(i,j)]=a+b
            return mp[(i,j)]
        return f(0,0)


        # abrow=[1]*n

        # for _ in range(m-1):
        #     curr=[1]*n
        #     for i in range(1,n):
        #         curr[i]=abrow[i]+curr[i-1]
        #     abrow=curr
        
        # return abrow[-1]

