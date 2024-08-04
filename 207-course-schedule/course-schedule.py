class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            mp[crs].append(pre)
        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            if mp[crs]==[]:
                return True
            visit.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            mp[crs]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True