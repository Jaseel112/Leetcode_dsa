class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxarea=0
        while left<right:
            area=abs(right-left)*min(height[left],height[right])
            maxarea=max(maxarea,area)
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1
        return maxarea
            