class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         count=0
#         # if not grid:
#         #     return 0
#         row,column=len(grid),len(grid[0])
#         q=[]
#         visited=set()
#         def bfs(r,c):
#             q.append((r,c))
#             visited.add((r,c))
#             dire=[[-1,0],[0,-1],[1,0],[0,1]]
#             while q:
#                 r,c=q.pop(0)
#                 for d in dire:
#                     i,j=r+d[0],c+d[1]
#                     if i in range(row) and j in range(column) and grid[i][j]=="1" and (i,j) not in visited:
#                         q.append((i,j))
#                         visited.add((i,j))

#         for i in range(row):
#             for j in range(column):
#                 if grid[i][j]=="1" and (i,j) not in visited:
#                     bfs(i,j)
#                     count+=1
#         return count
        def dfs(r,c):
            if grid[r][c]=="1" and (r,c) not in visited:
                visited.add((r,c))
                dir=[[1,0],[-1,0],[0,1],[0,-1]]
                for i,j in dir:
                    print(i,j)
                    if r+i in range(len(grid)) and c+j in range(len(grid[0])):
                        dfs(r+i,c+j)
                return
            else:
                return

        count=0
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        return count