class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        left=intervals[0][0]
        right=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            if right in range(intervals[i][0],intervals[i][1]+1):
                right=intervals[i][1]
            elif intervals[i][1] in range(left,right):
                continue
            else:
                res.append([left,right])
                left=intervals[i][0]
                right=intervals[i][1]
        res.append([left,right])
        return res

                
            
