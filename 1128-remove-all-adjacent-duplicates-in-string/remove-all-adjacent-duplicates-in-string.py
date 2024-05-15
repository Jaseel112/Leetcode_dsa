class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=list()
        stack.append(s[0])
        for i in s[1:]:
            if len(stack)==0 or stack[-1]!=i:
                stack.append(i)
            else:
                stack.pop()      
        return "".join(stack)          

