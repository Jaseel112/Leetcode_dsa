class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # result = []
        # for i in range(len(prices)):
        #     discount = 0
        #     for j in range(i+1,len(prices)):
        #         if prices[j] <= prices[i]:
        #             discount = prices[j]
        #             break
        #     result.append(prices[i]-discount)
        # return result
        stack=[]
        out=[0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1]>prices[i]:
                stack.pop()
            out[i]=prices[i] if not stack else prices[i]-stack[-1]
            stack.append(prices[i])
        return out
            