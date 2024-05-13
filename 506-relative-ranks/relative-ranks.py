class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        data=sorted(enumerate(score),key=lambda x:x[1],reverse=True)
        rank=[0]*len(score)
        j=0
        for i in data:
            if j==0:
             rank[i[0]]="Gold Medal"
             j+=1
            elif j==1:
                rank[i[0]]="Silver Medal"
                j+=1 
            elif j==2:
                rank[i[0]]="Bronze Medal"
                j+=1  
                print(rank)
            else:
                rank[i[0]]=str(data.index(i)+1)
        return rank
