class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i=="C":
                stack.pop()
            elif i=="D":
                r=stack[-1]
                stack.append(2*r)
            elif i=="+":
                r=stack[-1]
                k=stack[-2]
                stack.append(k+r)
            else:
                stack.append(int(i))
        out=sum(stack)
        return out