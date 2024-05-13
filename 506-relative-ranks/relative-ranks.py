class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        data=[]
        n=len(score)
        rank=[""]*len(score)
        for i in range(n):
            data.append((score[i],i))
        data.sort(reverse=True)
        for k in range (n):
            i=data[k][1]
            if k==0:
                rank[i]="Gold Medal"
            elif k==1:
                rank[i]="Silver Medal"
            elif k==2:
                rank[i]="Bronze Medal"
            else:
                rank[i]=str(k+1)
        return rank
