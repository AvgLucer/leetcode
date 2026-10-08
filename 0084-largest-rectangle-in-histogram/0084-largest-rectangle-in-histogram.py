class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0
        
        heights.append(0)
        
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()] 
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea,height*width)

            stack.append(i)

        return maxArea
         