class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for i in s:
            if stack:
                if i=='B' or i=='D':
                    if ord(stack[-1])+1==ord(i):
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
            print(stack)
        return len(stack)