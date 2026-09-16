class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums)):
            left, right = i + 1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total == 0:
                    result.append([nums[left], nums[right], nums[i]])
                    left +=1
                    right -=1
                    while left<right and nums[left] == nums[left-1]:
                        left +=1
            
                elif total > 0:
                    right -=1
                
                else:
                    left += 1
        return result
            


