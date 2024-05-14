class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans=[0]
        # for i in range(1,n+1):
        #     if i==1:
        #         ans.append(1)
        #         continue
        #     b=bin(i)[2:]
        #     ans.append(b.count('1'))
        # return ans

        result = [0]

        for i in range(1, n + 1):
            result.append(result[i // 2] + i % 2)

        return result