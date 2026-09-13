class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        sum = 0
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            if sum == 0:
               sum += num
            else: 
                sum *= num
    
        
        for i in range(len(nums)):
            if zero_count > 1:
                final.append(0)
            elif zero_count == 1:
                if nums[i] == 0:
                    final.append(sum)
                else:
                    final.append(0)
            else:
                final.append(int(sum/nums[i]))
        
        return final