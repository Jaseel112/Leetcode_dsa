class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col=len(heights),len(heights[0])
        def dfs(r,c,prevh,visit):
            if r not in range(row) or c not in range(col) or (r,c) in visit or heights[r][c]<prevh:
                return 
            visit.add((r,c))
            dfs(r,c-1,heights[r][c],visit)
            dfs(r,c+1,heights[r][c],visit)
            dfs(r+1,c,heights[r][c],visit)
            dfs(r-1,c,heights[r][c],visit)

        atl,pac=set(),set()
        for i in range(row):
            dfs(i,col-1,heights[i][col-1],atl)
            dfs(i,0,heights[i][0],pac)
        for i in range(col):
            dfs(row-1,i,heights[row-1][i],atl)
            dfs(0,i,heights[0][i],pac)
        return atl.intersection(pac)