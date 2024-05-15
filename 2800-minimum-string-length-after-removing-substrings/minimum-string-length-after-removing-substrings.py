class Solution:
    def minLength(self, s: str) -> int:
        stack=[s[0]]
        for i in s[1:]:
            if i=='B' or i=='D':
                if stack:
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