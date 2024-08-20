class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj=collections.defaultdict(list)
        if endWord not in wordList: 
            return 0
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+'*'+word[j+1:]
                adj[pattern].append(word)
        visit=set()
        q=[beginWord]
        res=1
        while q:
            for i in range(len(q)):
                word=q.pop(0)
                visit.add(word)
                if word==endWord:
                    return res
                for i in range(len(word)):
                    pattern=word[:i]+'*'+word[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
            res+=1
        return 0