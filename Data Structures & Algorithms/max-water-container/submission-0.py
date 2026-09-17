class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = 0
        start = 0
        end = len(heights)-1

        while start < end:
            temp = (end-start) * min(heights[start], heights[end])
            if temp > max_value:
                max_value = temp
            
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        
        return max_value

            
