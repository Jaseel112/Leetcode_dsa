class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=Counter(nums)
        res=[]
        ret=[]
        for x in mp.keys():
            res.append((mp[x],x))
        res.sort(reverse=True)
        for i in range(k):
            ret.append(res[i][1])
        return ret

        # import heapq
        # mp=Counter(nums)
        # heap=[]
        # ret=[]
        # for key,val in mp.items():
        #     heapq.heappush(heap,(val,key))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # for i in heap:
        #     ret.append(i[1])
        # return ret

            
        


