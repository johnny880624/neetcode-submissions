class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        stack = []

        for i in range(len(pair)):
            time = (target-pair[i][0])/pair[i][1]
            if not stack:
                stack.append(time)
            if stack and time > stack[-1]:
                stack.append(time)
        
        return len(stack)
            

            
        