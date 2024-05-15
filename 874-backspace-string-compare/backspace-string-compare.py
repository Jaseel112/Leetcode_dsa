class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks=[]
        stackt=[]
        for i in s:
            if i=='#':
                if stacks:
                 stacks.pop()
            else:
                stacks.append(i)
        for i in t:
            if i=='#':
                if stackt:
                    stackt.pop()
            else:
                stackt.append(i)
        if stacks==stackt:
            return True
        else:
            return False