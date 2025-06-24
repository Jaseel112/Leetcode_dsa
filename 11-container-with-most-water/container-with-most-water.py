class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left=0
        # right=len(height)-1
        # maxa=-0
        # while left<right:
        #     area=(right-left)*min(height[left],height[right])
        #     maxa=max(area,maxa)
        #     if height[left]<height[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return maxa















        h=height
        left=0
        right=len(h)-1
        area=min(h[left],h[right]) * (right-left)
        while left<right:
            area=max(min(h[left],h[right]) * (right-left),area)
            if h[left]<h[right]:
                left+=1
            else:
                right-=1
        return area



            