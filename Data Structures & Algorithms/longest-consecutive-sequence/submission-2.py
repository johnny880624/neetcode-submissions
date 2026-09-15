class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        value, max_v = nums[0], 1
        temp = 1

        for i in range(len(nums)-1):
            if nums[i+1] ==nums[i]:
                continue
            if nums[i+1] -1 == nums[i]:
                temp += 1
            else:
                temp = 1
            if temp > max_v:
                max_v = temp
        return max_v

