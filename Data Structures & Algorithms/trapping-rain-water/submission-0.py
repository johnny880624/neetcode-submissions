class Solution:
    def trap(self, height: List[int]) -> int:
        prefix =[]
        suffix = []
        final = 0
        temp = 0
        for i in range(len(height)):
            if i == 0:
                prefix.append(0)    
                continue
            if height[i-1] > temp:
                temp = height[i-1]

            prefix.append(temp)

        temp = 0
        for i in range(len(height)-1,-1, -1):
            if i == (len(height)-1):
                suffix.append(0)
                continue
            if height[i+1] > temp:
                temp = height[i+1]
        
            suffix.append(temp)
        suffix = suffix[::-1] 
        
        for i in range(len(height)):
            temp_result = min(suffix[i],prefix[i]) - height[i]
            if temp_result > 0:
                final += temp_result
        
        return final
