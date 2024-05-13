class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map={}
        l=s.split()
        if len(pattern)!=len(l):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map:
                map[pattern[i]]=l[i]
            if pattern[i] in map:
                if map[pattern[i]]!=l[i]:
                    print(map)
                    return False
        value=list(map.values())
        if len(value)!=len(set(value)):
            return False
        return True