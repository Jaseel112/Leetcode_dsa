class Solution:
    def isValid(self, s: str) -> bool:
        v=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                v.append(i)
            else:
                if len(v)==0:
                    return False
                else:
                    t=v.pop()
                    if i==')':
                        if t!='(':
                            return False
                    elif i=='}':
                        if t!='{':
                            return False
                    elif i==']':
                        if t!='[':
                            return False
        if len(v)==0:
            return True
        else:
            return False
            