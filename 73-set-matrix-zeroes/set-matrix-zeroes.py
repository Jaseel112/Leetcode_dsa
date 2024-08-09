class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mp={}
        mp1={}
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    if i not in mp:
                        mp[i]=1
                    if j not in mp1:
                        mp1[j]=1
        # print(mp)
        # print(mp1)
        for x in mp.keys():
            for i in range(c):
                    matrix[x][i]=0
        for x in mp1.keys():
            for i in range(r):
                matrix[i][x]=0
        # return matrix