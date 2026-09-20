class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1 
        vol = 0 

        while l<r:
            width = abs(l-r)
            area = min(heights[l], heights[r])* width
            vol = max(vol, area )

            if heights[l] < heights[r]:
                l += 1   
            else:
                r -= 1 
        return vol
        