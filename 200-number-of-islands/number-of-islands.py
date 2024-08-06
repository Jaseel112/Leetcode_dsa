class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        # if not grid:
        #     return 0
        row,column=len(grid),len(grid[0])
        q=[]
        visited=set()
        def bfs(r,c):
            q.append((r,c))
            visited.add((r,c))
            dire=[[-1,0],[0,-1],[1,0],[0,1]]
            while q:
                r,c=q.pop(0)
                for d in dire:
                    i,j=r+d[0],c+d[1]
                    if i in range(row) and j in range(column) and grid[i][j]=="1" and (i,j) not in visited:
                        q.append((i,j))
                        visited.add((i,j))

        for i in range(row):
            for j in range(column):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    count+=1
        return count

        